"""
Adapters — um por TIPO de sistema de permits, não por cidade.

Cada cidade vira só uma entrada em registry.yaml. Os adapters sabem conversar
com a plataforma (CKAN, Socrata, ArcGIS) e traduzem os campos de cada cidade
para o formato padrão do Permit Radar.

Versão 2.5: Worcester (ArcGIS) e relatórios em arquivo; filtra permits de especialidade, classifica o tipo de obra
(New Construction / Addition / Renovation / Demolition) e descobre colunas sozinho.
Para ver colunas e tipos de permit no log, defina PERMIT_DEBUG=1.
"""

from __future__ import annotations

import csv
import io
import os
import re
import time
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urljoin

import requests

DEBUG = bool(os.environ.get("PERMIT_DEBUG"))

HEADERS = {"User-Agent": "PermitRadar/1.0 (public permit data aggregator)"}

# Nomes comuns de colunas, em ordem de preferência. O primeiro que existir vence.
DEFAULT_CANDIDATES = {
    "permit_number": ["permit_number", "permitnumber", "permit_no", "permit_num", "permit_nbr",
                      "permit", "record_number", "record__", "record_no", "permit_id",
                      "plannumber", "id"],
    "address": ["address", "full_address", "site_address", "street_address",
                "property_address", "project_address", "location_address", "location"],
    "permit_type": ["permit_type", "permittypedescr", "permit_type_description",
                    "permit_for", "record_type", "worktype", "work_type", "type"],
    "status": ["status", "permit_status", "record_status", "current_status"],
    "estimated_value": ["estimated_cost", "declared_valuation", "total_project_cost",
                        "total_cost_of_construction", "total_cost", "project_value",
                        "estimated_value", "est_cost", "job_cost", "project_cost",
                        "construction_cost", "cost_of_construction", "valuation",
                        "building_cost", "value", "cost"],
    "issue_date": ["issue_date", "issued_date", "date_issued", "permit_issue_date",
                   "permit_license_issued_date", "issuance_date", "issued"],
    "description": ["description", "comments", "project_description",
                    "work_description", "scope_of_work", "description_of_work",
                    "detailed_description_of_work", "isd_approved_description"],
    "owner": ["owner", "owner_name", "property_owner", "owner_legal_name"],
    "applicant": ["applicant", "applicant_name"],
    "contractor": ["contractor", "contractor_name", "general_contractor", "builder",
                   "firm_name", "licensed_name", "gc_name", "licensed_contractor"],
}

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}")
EMPTY_VALUES = {"n/a", "na", "none", "null", "-", "--", "unknown", ""}


# ---------------------------------------------------------------------------
# Relevância e classificação
# O radar é para construção e reforma. Permits de especialidade (elétrico,
# hidráulico, gás, alarme...) e administrativos (certificados, emendas) ficam de fora.
# ---------------------------------------------------------------------------
INCLUDE_TYPE_RE = re.compile(
    r"(building|bldg|short form|long form|erect|new construction|foundation|alteration|"
    r"addition|demolition|remodel|renovation|construction|roof|siding|residential|commercial|"
    r"deck|accessory|adu|garage|carport|restore after fire)", re.I)
EXCLUDE_TYPE_RE = re.compile(
    r"\b(amendment|certificate|electrical|plumbing|gas|mechanical|sheet metal|fire alarms?|"
    r"low voltage|sprinkler|signs?|occupancy|excavation|asbestos|tents?|dumpster|food|tobacco|"
    r"insulation|stove|antenna|zoning|crowd|carnival|billboard|turbine|pool|fence|retaining|"
    r"shed|change of use|temporary|moving)\b", re.I)
EVENT_DESC_RE = re.compile(r"\b(tents?|beer garden|festival|one day event|1 day event)\b", re.I)

NEW_CONSTRUCTION_DESC_RE = re.compile(
    r"\bnew (building|structure|construction|single[- ]family|two[- ]family|three[- ]family|"
    r"multi[- ]?family|dwelling|home|house)\b", re.I)
WORK_ON_EXISTING_RE = re.compile(r"\b(renovat\w*|remodel\w*|alteration\w*|repair\w*|replac\w*|install\w*)\b", re.I)
DEMOLITION_RE = re.compile(r"\b(demolish\w*|demolition|demo)\b", re.I)
BUILD_WORDS_RE = re.compile(r"\b(renovat\w*|remodel\w*|replac\w*|install\w*|build|construct\w*|new|rebuild\w*)\b", re.I)
ADDITION_RE = re.compile(r"\b(addition|dormer|sunroom|bump[- ]?out)\b", re.I)


def is_relevant(permit_type, description=None) -> bool:
    """True se o permit é de construção/reforma geral (e não de especialidade ou administrativo)."""
    t = permit_type or ""
    if t:
        if EXCLUDE_TYPE_RE.search(t):
            return False
        if not INCLUDE_TYPE_RE.search(t):
            return False
    if description and EVENT_DESC_RE.search(description):
        return False
    return True


def classify_permit(permit_type, description=None) -> str:
    """Padroniza o tipo de obra: New Construction / Addition / Renovation / Demolition
    (ou Unspecified, quando a cidade não informa o tipo)."""
    t = (permit_type or "")
    d = (description or "")
    if re.search(r"type not listed", t, re.I):
        return "Unspecified"
    if re.search(r"new construction|erect", t, re.I):
        return "New Construction"
    if NEW_CONSTRUCTION_DESC_RE.search(d) and not WORK_ON_EXISTING_RE.search(d):
        return "New Construction"
    if re.search(r"demolition", t, re.I) or (DEMOLITION_RE.search(d) and not BUILD_WORDS_RE.search(d)):
        return "Demolition"
    if re.search(r"accessory dwelling|\badu\b", t, re.I):
        return "Addition"
    if re.search(r"\baddition\b", t, re.I) and not re.search(r"alteration", t, re.I):
        return "Addition"
    if ADDITION_RE.search(d):
        return "Addition"
    return "Renovation"


def _http_get(url: str, params: dict | None = None):
    """GET com 3 tentativas para oscilações de rede; em erro HTTP, devolve a explicação do servidor."""
    last_exc = None
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, headers=HEADERS, timeout=60)
        except (requests.Timeout, requests.ConnectionError) as e:
            last_exc = e
            time.sleep(3 * (attempt + 1))
            continue
        if resp.status_code in (502, 503, 504) and attempt < 2:
            time.sleep(3 * (attempt + 1))
            continue
        if resp.status_code >= 400:
            raise RuntimeError(f"HTTP {resp.status_code} — resposta do servidor: {resp.text[:400]}")
        return resp
    raise RuntimeError(f"falha de rede após 3 tentativas: {last_exc}")


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
            if key is None:
                continue
            val = raw.get(key)
            if val in (None, ""):
                continue
            # "N/A" e similares viram vazio (exceto no tipo, onde ele ajuda a descartar o registro)
            if std_field != "permit_type" and isinstance(val, str) and val.strip().lower() in EMPTY_VALUES:
                continue
            return val
        return None

    def normalize(self, raw_records: list[dict]) -> list[dict]:
        out = []
        ignored = 0
        for raw in raw_records:
            rec = {"source_city": self.city, "source_state": self.state,
                   "source_link": self.source_link, "city": self.city}
            clean = {k: v for k, v in raw.items() if k != "_dataset_label"}
            for std_field in self.STANDARD_FIELDS:
                rec[std_field] = self._pick(clean, std_field)
            rec["estimated_value"] = self._to_float(rec["estimated_value"])
            # Valores como $0,01 ou $1 são marcadores administrativos, não o custo real da obra.
            if rec["estimated_value"] is not None and rec["estimated_value"] < 10:
                rec["estimated_value"] = None
            rec["issue_date"] = self._to_date(rec["issue_date"])
            if not rec.get("permit_type"):
                rec["permit_type"] = raw.get("_dataset_label")
            unknown_label = self.config.get("unknown_type_label")
            if unknown_label and (rec.get("permit_type") is None or
                                  str(rec["permit_type"]).strip().lower() in EMPTY_VALUES):
                rec["permit_type"] = unknown_label
            if rec.get("permit_number") is not None:
                rec["permit_number"] = str(rec["permit_number"])
            if not is_relevant(rec.get("permit_type"), rec.get("description")):
                ignored += 1
                continue
            rec["category"] = classify_permit(rec.get("permit_type"), rec.get("description"))
            out.append(rec)
        if ignored:
            print(f"[info] {self.city}: {ignored} permits de especialidade/administrativos ignorados "
                  f"(elétrico, hidráulico, gás, alarme, certificados...)")
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
        if isinstance(v, datetime):
            return v.date().isoformat()
        if isinstance(v, date):
            return v.isoformat()
        if isinstance(v, (int, float)):
            seconds = v / 1000 if v > 1e11 else v
            try:
                return datetime.fromtimestamp(seconds, tz=timezone.utc).date().isoformat()
            except (OverflowError, OSError, ValueError):
                return None
        if isinstance(v, datetime):
            return v.date().isoformat()
        if isinstance(v, date):
            return v.isoformat()
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


class ArcGISQueryAdapter(BaseAdapter):
    """ArcGIS FeatureServer consultado pela API REST (/query), com paginação e espera
    automática quando o servidor limita as consultas (erro 429).

    Usado por Worcester. Config: service_url, order_by, page_size, max_pages, where.
    Ex.: em Worcester as datas são TEXTO (m/d/aaaa) e o registro mais novo vem primeiro
    (ObjectId crescente), então buscamos as primeiras páginas e filtramos a data aqui."""

    def _query(self, url: str, params: dict) -> dict:
        for attempt in range(6):
            resp = requests.get(url, params=params, headers=HEADERS, timeout=60)
            if resp.status_code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            data = resp.json()
            err = data.get("error")
            if err and err.get("code") == 429:
                wait = 30 * (attempt + 1)
                print(f"[info] {self.city}: servidor pediu para esperar; aguardando {wait}s")
                time.sleep(wait)
                continue
            if err:
                raise RuntimeError(f"ArcGIS erro {err.get('code')}: {err.get('message')} {err.get('details')}")
            return data
        raise RuntimeError("ArcGIS: limite de consultas excedido após várias tentativas")

    def fetch_raw(self, days_back: int) -> list[dict]:
        base = self.config["service_url"].rstrip("/")
        page = int(self.config.get("page_size", 1000))
        pages = int(self.config.get("max_pages", 2))
        rows: list[dict] = []
        for i in range(pages):
            params = {"where": self.config.get("where", "1=1"), "outFields": "*",
                      "orderByFields": self.config.get("order_by", "ObjectId ASC"),
                      "resultOffset": i * page, "resultRecordCount": page, "f": "json"}
            feats = self._query(base + "/query", params).get("features", [])
            rows += [f.get("attributes", {}) for f in feats]
            if len(feats) < page:
                break
        return rows

    def fetch(self, days_back: int = 2) -> list[dict]:
        records = self.normalize(self.fetch_raw(days_back))
        since = (date.today() - timedelta(days=days_back)).isoformat()
        dated = [r["issue_date"] for r in records if r.get("issue_date")]
        if dated:
            print(f"[info] {self.city}: permit mais recente emitido em: {max(dated)}")
        return [r for r in records if r.get("issue_date") and r["issue_date"] >= since]


def _norm_header(h) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(h or "").lower()).strip("_")


class FileReportAdapter(BaseAdapter):
    """Cidades que publicam os permits emitidos em arquivos mensais (Excel ou CSV),
    como Reading. O adaptador abre a página de índice, acha os links dos arquivos mais
    recentes, baixa, localiza a linha de cabeçalho e traduz as colunas.

    Config: index_url, link_regex, link_text_regex, max_files, min_days_back.
    EXPERIMENTAL até o primeiro log confirmar os nomes reais das colunas."""

    HEADER_TOKENS = ("address", "permit", "date", "type", "contractor", "applicant", "cost")

    def _find_links(self, html: str) -> list[str]:
        link_re = re.compile(self.config.get("link_regex", r"DocumentCenter/View/\d+"), re.I)
        text_re = re.compile(self.config.get("link_text_regex", ""), re.I)
        picked: list[str] = []
        for href, inner in re.findall(r"<a[^>]+href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", html, re.I | re.S):
            text = re.sub(r"<[^>]+>", " ", inner)
            if link_re.search(href) and text_re.search(text):
                url = urljoin(self.config["index_url"], href.replace("&amp;", "&"))
                if url not in picked:
                    picked.append(url)
        return picked[: int(self.config.get("max_files", 2))]

    def _parse_xlsx(self, content: bytes) -> list[dict]:
        from openpyxl import load_workbook
        wb = load_workbook(io.BytesIO(content), read_only=True, data_only=True)
        out: list[dict] = []
        for ws in wb.worksheets:
            rows = list(ws.iter_rows(values_only=True))
            hdr = None
            for i, r in enumerate(rows[:15]):
                cells = [str(c).strip() for c in r if c not in (None, "")]
                joined = " ".join(cells).lower()
                if len(cells) >= 3 and any(t in joined for t in self.HEADER_TOKENS):
                    hdr = i
                    break
            if hdr is None:
                continue
            headers = [_norm_header(c) for c in rows[hdr]]
            print(f"[info] {self.city}: colunas do arquivo ({ws.title}): {[h for h in headers if h]}")
            for r in rows[hdr + 1:]:
                if not any(c not in (None, "") for c in r):
                    continue
                out.append({h: v for h, v in zip(headers, r) if h})
        return out

    def _parse_csv(self, content: bytes) -> list[dict]:
        text = content.decode("utf-8-sig", errors="replace")
        reader = csv.DictReader(io.StringIO(text))
        rows = [{_norm_header(k): v for k, v in row.items() if k} for row in reader]
        if rows:
            print(f"[info] {self.city}: colunas do arquivo: {list(rows[0].keys())}")
        return rows

    def fetch_raw(self, days_back: int) -> list[dict]:
        html = _http_get(self.config["index_url"]).text
        urls = self._find_links(html)
        print(f"[info] {self.city}: {len(urls)} arquivo(s) de relatório encontrado(s)")
        rows: list[dict] = []
        for url in urls:
            try:
                resp = _http_get(url)
                data = resp.content
                parsed = self._parse_xlsx(data) if data[:2] == b"PK" else self._parse_csv(data)
                print(f"[info] {self.city}: {len(parsed)} linhas em {url}")
                rows += parsed
            except Exception as e:  # noqa: BLE001
                print(f"[erro] {self.city}: falha ao ler {url}: {e}")
        return rows

    def fetch(self, days_back: int = 2) -> list[dict]:
        days = max(days_back, int(self.config.get("min_days_back", 45)))  # relatórios mensais têm atraso
        records = self.normalize(self.fetch_raw(days))
        since = (date.today() - timedelta(days=days)).isoformat()
        return [r for r in records if r.get("issue_date") and r["issue_date"] >= since]


ADAPTERS = {
    "ckan": CKANAdapter,
    "socrata": SocrataAdapter,
    "arcgis": ArcGISAdapter,
    "arcgis_query": ArcGISQueryAdapter,
    "file_report": FileReportAdapter,
}
