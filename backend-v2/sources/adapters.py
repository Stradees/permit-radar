"""
Adapters — um por TIPO de sistema de permits, não por cidade.

Cada cidade vira só uma entrada em registry.yaml. Os adapters sabem conversar
com a plataforma (CKAN, Socrata, ArcGIS) e traduzem os campos de cada cidade
para o formato padrão do Permit Radar.

Versão 2.3: os adapters descobrem sozinhos os nomes das colunas (tentam vários
nomes comuns). Para ver colunas e tipos de permit no log, defina PERMIT_DEBUG=1.
"""

from __future__ import annotations

import os
import re
from datetime import date, datetime, timedelta, timezone

import requests

DEBUG = bool(os.environ.get("PERMIT_DEBUG"))

HEADERS = {"User-Agent": "PermitRadar/1.0 (public permit data aggregator)"}

# Nomes comuns de colunas, em ordem de preferência. O primeiro que existir vence.
DEFAULT_CANDIDATES = {
    "permit_number": ["permit_number", "permitnumber", "permit_no", "record_number",
                      "permit_id", "plannumber", "id"],
    "address": ["address", "full_address", "site_address", "street_address",
                "project_address", "location_address", "location"],
    "permit_type": ["permit_type", "permittypedescr", "permit_type_description",
                    "record_type", "worktype", "type"],
    "status": ["status", "permit_status", "current_status"],
    "estimated_value": ["estimated_cost", "declared_valuation", "total_project_cost",
                        "total_cost_of_construction", "total_cost", "project_value",
                        "estimated_value", "valuation", "building_cost", "cost"],
    "issue_date": ["issue_date", "issued_date", "date_issued", "permit_issue_date",
                   "issuance_date"],
    "description": ["description", "comments", "project_description",
                    "work_description", "scope_of_work", "description_of_work",
                    "detailed_description_of_work", "isd_approved_description"],
    "owner": ["owner", "owner_name", "property_owner", "owner_legal_name"],
    "applicant": ["applicant", "applicant_name"],
    "contractor": ["contractor", "contractor_name", "general_contractor", "firm_name",
                   "licensed_name", "gc_name", "licensed_contractor"],
}

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}")


def _http_get(url: str, params: dict | None = None):
    """GET que, em caso de erro, devolve a explicação que o servidor deu."""
    resp = requests.get(url, params=params, headers=HEADERS, timeout=60)
    if resp.status_code >= 400:
        raise RuntimeError(f"HTTP {resp.status_code} — resposta do servidor: {resp.text[:400]}")
    return resp


class BaseAdapter:
    STANDARD_FIELDS = list(DEFAULT_CANDIDATES.keys())

    def __init__(self, city: str, state: str, config: dict, field_map: dict | None, source_link: str = ""):
        self.city = city
        self.state = state
        self.config = config or {}
        self.field_map = field_map or {}
        self.source_link = source_link

    # ---- a ser implementado por cada plataforma ----
    def fetch_raw(self, days_back: int) -> list[dict]:
        raise NotImplementedError

    # ---- utilidades comuns ----
    def _pick(self, raw: dict, std_field: str):
        lower = {str(k).lower(): k for k in raw}
        configured = self.field_map.get(std_field)
        if isinstance(configured, list):
            candidates = list(configured)
        elif configured:
            candidates = [configured]
        else:
            candidates = []
        candidates += DEFAULT_CANDIDATES.get(std_field, [])
        for name in candidates:
            key = lower.get(str(name).lower())
            if key is not None and raw.get(key) not in (None, ""):
                return raw[key]
        return None

    def normalize(self, raw_records: list[dict]) -> list[dict]:
        out = []
        for raw in raw_records:
            rec = {"source_city": self.city, "source_state": self.state,
                   "source_link": self.source_link, "city": self.city}
            clean = {k: v for k, v in raw.items() if k != "_dataset_label"}
            for std_field in self.STANDARD_FIELDS:
                rec[std_field] = self._pick(clean, std_field)
            rec["estimated_value"] = self._to_float(rec["estimated_value"])
            rec["issue_date"] = self._to_date(rec["issue_date"])
            if not rec.get("permit_type"):
                rec["permit_type"] = raw.get("_dataset_label")
            if rec.get("permit_number") is not None:
                rec["permit_number"] = str(rec["permit_number"])
            out.append(rec)
        return [r for r in out if r.get("permit_number") and r.get("address")]

    def fetch(self, days_back: int = 2) -> list[dict]:
        return self.normalize(self.fetch_raw(days_back))

    @staticmethod
    def _to_float(v):
        if v is None:
            return None
        try:
            return float(str(v).replace(",", "").replace("$", ""))
        except (TypeError, ValueError):
            return None

    @staticmethod
    def _to_date(v):
        """Converte vários formatos de data para AAAA-MM-DD."""
        if v is None or v == "":
            return None
        if isinstance(v, (int, float)):
            seconds = v / 1000 if v > 1e11 else v
            try:
                return datetime.fromtimestamp(seconds, tz=timezone.utc).date().isoformat()
            except (OverflowError, OSError, ValueError):
                return None
        s = str(v).strip()
        if ISO_DATE.match(s):
            return s[:10]
        m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})", s)
        if m:
            return f"{m.group(3)}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
        return s


class CKANAdapter(BaseAdapter):
    """CKAN datastore_search_sql — usado por Boston (data.boston.gov)."""

    def fetch_raw(self, days_back: int) -> list[dict]:
        base_url = self.config["base_url"]
        resource_id = self.config["resource_id"]
        date_field = self.config.get("date_field", "issued_date")
        since = (date.today() - timedelta(days=days_back)).isoformat()
        sql = (f'SELECT * FROM "{resource_id}" WHERE {date_field} >= \'{since}\' '
               f'ORDER BY {date_field} DESC LIMIT 1000')
        data = _http_get(base_url, {"sql": sql}).json()
        if not data.get("success"):
            raise RuntimeError(f"CKAN API error ({self.city}): {data}")
        return data["result"]["records"]


class SocrataAdapter(BaseAdapter):
    """Socrata SODA API — usado por Cambridge e muitas outras cidades dos EUA."""

    def fetch(self, days_back: int = 2) -> list[dict]:
        records = self.normalize(self.fetch_raw(days_back))
        # Proteção final: só devolve permits cuja data de emissão seja recente
        # (evita tratar permits antigos como "novos" quando o filtro do servidor não pôde ser usado).
        since = (date.today() - timedelta(days=days_back)).isoformat()
        return [r for r in records if r.get("issue_date") and r["issue_date"] >= since]

    def _pick_date_field(self, columns: list[str], sample: dict) -> str | None:
        lowered = {c.lower(): c for c in columns}
        preferred = self.config.get("date_field")
        candidates = ([preferred] if preferred else []) + DEFAULT_CANDIDATES["issue_date"]
        chosen = None
        for name in candidates:
            if name and name.lower() in lowered:
                chosen = lowered[name.lower()]
                break
        if chosen is None:
            for c in columns:
                if "issue" in c.lower() and "date" in c.lower():
                    chosen = c
                    break
        # Só filtramos por data no servidor se a coluna for uma data de verdade (AAAA-MM-DD...).
        if chosen and ISO_DATE.match(str(sample.get(chosen, ""))):
            return chosen
        return None

    def _log_schema(self, label: str, dataset_id: str, rows: list[dict]):
        if not DEBUG:
            return
        if not rows:
            print(f"[info] {self.city} / {label} ({dataset_id}): sem linhas de amostra")
            return
        print(f"[info] {self.city} / {label} ({dataset_id}) COLUNAS: {sorted(rows[0].keys())}")
        sample = {k: (str(v)[:60]) for k, v in rows[0].items()}
        print(f"[info] {self.city} / {label} EXEMPLO: {sample}")

    def _log_freshness(self, url: str, label: str, date_field: str | None):
        """Escreve no log a data do permit mais recente do conjunto."""
        if not date_field:
            return
        try:
            res = _http_get(url, {"$select": f"max({date_field}) as latest"}).json()
            print(f"[info] {self.city} / {label}: permit mais recente emitido em: {res}")
        except Exception as e:  # noqa: BLE001
            print(f"[info] {self.city} / {label}: não consegui medir a data mais recente: {e}")

    def _log_types(self, url: str, label: str):
        """Escreve no log os tipos de permit mais frequentes do conjunto."""
        try:
            res = _http_get(url, {"$select": "permit_type, count(*) as n",
                                  "$group": "permit_type", "$order": "n DESC",
                                  "$limit": 40}).json()
            print(f"[info] {self.city} / {label}: TIPOS DE PERMIT: {res}")
        except Exception as e:  # noqa: BLE001
            print(f"[info] {self.city} / {label}: não consegui listar tipos: {e}")

    def fetch_raw(self, days_back: int) -> list[dict]:
        domain = self.config["domain"]
        since = (date.today() - timedelta(days=days_back)).isoformat()

        # Conjuntos só para "espiar" as colunas (não entram nos resultados). Só roda em modo depuração.
        inspect = (self.config.get("inspect_datasets") or {}) if DEBUG else {}
        for label, dataset_id in inspect.items():
            try:
                url = f"https://{domain}/resource/{dataset_id}.json"
                rows = _http_get(url, {"$limit": 2}).json()
                self._log_schema(label, dataset_id, rows)
                if rows:
                    self._log_freshness(url, label, self._pick_date_field(list(rows[0].keys()), rows[0]))
                self._log_types(url, label)
            except Exception as e:  # noqa: BLE001
                print(f"[info] não consegui espiar {label}: {e}")

        all_records: list[dict] = []
        for label, dataset_id in (self.config.get("datasets") or {}).items():
            url = f"https://{domain}/resource/{dataset_id}.json"
            try:
                sample_rows = _http_get(url, {"$limit": 2}).json()
                self._log_schema(label, dataset_id, sample_rows)
                if not sample_rows:
                    continue
                columns = list(sample_rows[0].keys())
                date_field = self._pick_date_field(columns, sample_rows[0])
                self._log_freshness(url, label, date_field)

                params = {"$limit": 1000}
                if date_field:
                    params["$where"] = f"{date_field} >= '{since}T00:00:00'"
                    params["$order"] = f"{date_field} DESC"
                else:
                    params["$order"] = ":updated_at DESC"
                    params["$limit"] = 200
                    print(f"[info] {self.city} / {label}: sem coluna de data utilizável; "
                          f"usando os 200 registros mais recentemente atualizados")

                try:
                    rows = _http_get(url, params).json()
                except RuntimeError as e:
                    print(f"[aviso] {self.city} / {label}: filtro falhou ({e}); tentando sem filtro")
                    rows = _http_get(url, {"$order": ":updated_at DESC", "$limit": 200}).json()

                print(f"[info] {self.city} / {label}: {len(rows)} registros recentes encontrados")
                for rec in rows:
                    rec["_dataset_label"] = label
                    all_records.append(rec)
            except Exception as e:  # noqa: BLE001
                print(f"[erro] {self.city} / {label} ({dataset_id}): {e}")
        return all_records


class ArcGISAdapter(BaseAdapter):
    """ArcGIS Hub (GeoJSON) — usado por Worcester e outras cidades."""

    def fetch_raw(self, days_back: int) -> list[dict]:
        geojson_url = self.config["geojson_url"]
        data = _http_get(geojson_url).json()
        features = data.get("features", [])
        rows = [f.get("properties", {}) for f in features]
        if rows:
            print(f"[info] {self.city} COLUNAS: {sorted(rows[0].keys())}")
            print(f"[info] {self.city} EXEMPLO: { {k: str(v)[:60] for k, v in rows[0].items()} }")
        return rows

    def fetch(self, days_back: int = 2) -> list[dict]:
        records = self.normalize(self.fetch_raw(days_back))
        since = (date.today() - timedelta(days=days_back)).isoformat()
        return [r for r in records if r.get("issue_date") and r["issue_date"] >= since]


ADAPTERS = {
    "ckan": CKANAdapter,
    "socrata": SocrataAdapter,
    "arcgis": ArcGISAdapter,
}
