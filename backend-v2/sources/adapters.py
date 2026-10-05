"""
Adapters — um por TIPO de sistema de permits, não por cidade.

A ideia central: dezenas de cidades (em MA e em outros estados) usam a mesma
plataforma por baixo dos panos (Socrata, CKAN, ArcGIS Hub, Accela, OpenGov...).
Em vez de escrever um scraper por cidade, escrevemos um adapter por PLATAFORMA,
e cada cidade vira só uma entrada de configuração em registry.yaml.

Isso é o que permite escalar para o estado inteiro e depois para outros estados
sem reescrever código.
"""

from __future__ import annotations
import requests
from datetime import date, timedelta
from typing import Any


class BaseAdapter:
    """Interface comum. Todo adapter recebe um `config` (dict do registry.yaml)
    e um `field_map` (dict) que traduz os nomes de campo da fonte para o
    formato padrão do Permit Radar."""

    STANDARD_FIELDS = [
        "permit_number", "address", "permit_type", "status",
        "estimated_value", "issue_date", "description",
        "owner", "applicant", "contractor",
    ]

    def __init__(self, city: str, state: str, config: dict, field_map: dict, source_link: str = ""):
        self.city = city
        self.state = state
        self.config = config
        self.field_map = field_map
        self.source_link = source_link

    def fetch_raw(self, days_back: int) -> list[dict]:
        raise NotImplementedError

    def normalize(self, raw_records: list[dict]) -> list[dict]:
        out = []
        for raw in raw_records:
            record = {"source_city": self.city, "source_state": self.state, "source_link": self.source_link}
            for std_field in self.STANDARD_FIELDS:
                src_field = self.field_map.get(std_field)
                record[std_field] = raw.get(src_field) if src_field else None
            record["estimated_value"] = self._to_float(record.get("estimated_value"))
            record["city"] = self.city
            out.append(record)
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


class CKANAdapter(BaseAdapter):
    """CKAN datastore_search_sql API — usado por Boston (data.boston.gov) e
    outras cidades/estados que publicam dados via portal CKAN."""

    def fetch_raw(self, days_back: int) -> list[dict]:
        base_url = self.config["base_url"]
        resource_id = self.config["resource_id"]
        date_field = self.config.get("date_field", "issued_date")
        since = (date.today() - timedelta(days=days_back)).isoformat()

        sql = f'SELECT * FROM "{resource_id}" WHERE {date_field} >= \'{since}\' ORDER BY {date_field} DESC LIMIT 1000'
        resp = requests.get(base_url, params={"sql": sql}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if not data.get("success"):
            raise RuntimeError(f"CKAN API error ({self.city}): {data}")
        return data["result"]["records"]


class SocrataAdapter(BaseAdapter):
    """Socrata SODA API — usado por Cambridge e muitas outras cidades/estados
    (Socrata é a plataforma de dados abertos mais comum nos EUA)."""

    def fetch_raw(self, days_back: int) -> list[dict]:
        domain = self.config["domain"]
        datasets: dict[str, str] = self.config["datasets"]  # {label: dataset_id}
        date_field = self.config.get("date_field", "issued_date")
        since = (date.today() - timedelta(days=days_back)).isoformat()

        all_records = []
        for label, dataset_id in datasets.items():
            url = f"https://{domain}/resource/{dataset_id}.json"
            params = {
                "$where": f"{date_field} >= '{since}T00:00:00'",
                "$order": f"{date_field} DESC",
                "$limit": 1000,
            }
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            for rec in resp.json():
                rec["_dataset_label"] = label
                all_records.append(rec)
        return all_records


class ArcGISAdapter(BaseAdapter):
    """ArcGIS Hub / FeatureServer — usado por Worcester, West Springfield e
    muitas cidades menores que publicam via ArcGIS Open Data.

    IMPORTANTE: a filtragem por data é feita no cliente (não via query da API)
    porque campos de data no ArcGIS costumam vir em epoch milissegundos e
    variam de dataset para dataset — confirme o nome e formato do campo de
    data antes de usar em produção (ver `status: needs_field_mapping` no
    registry.yaml)."""

    def fetch_raw(self, days_back: int) -> list[dict]:
        geojson_url = self.config["geojson_url"]
        resp = requests.get(geojson_url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        features = data.get("features", [])
        return [f["properties"] for f in features]


ADAPTERS = {
    "ckan": CKANAdapter,
    "socrata": SocrataAdapter,
    "arcgis": ArcGISAdapter,
}