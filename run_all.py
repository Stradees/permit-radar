"""
Runner central. Não sabe nada sobre cidades específicas — só lê o registry.yaml
e delega pro adapter certo. Adicionar cobertura (mais cidades, mais estados) é
uma mudança de configuração, não de código.

status no registry.yaml:
    confirmed     -> roda e entra no dashboard e no e-mail
    experimental  -> roda e mostra no log, mas NÃO entra no dashboard
                     (até o log confirmar que os dados estão corretos).
                     Para incluir mesmo assim: INCLUDE_EXPERIMENTAL=1
    qualquer outro -> não roda (sem fonte automática viável ainda)

Uso:
    python run_all.py                       # todos os estados, cidades confirmed
    python run_all.py --state massachusetts
    python run_all.py --city Reading        # testa uma cidade (inclusive experimental)
"""

import argparse
import json
import os
from pathlib import Path

import yaml

from sources.adapters import ADAPTERS

REGISTRY_PATH = Path(__file__).parent / "sources" / "registry.yaml"
RUNNABLE = ("confirmed", "experimental")


def load_registry() -> dict:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run(states_filter: list[str] | None = None, days_back: int = 2,
        cities_filter: list[str] | None = None,
        include_experimental: bool | None = None) -> tuple[list[dict], list[dict]]:
    """Retorna (permits, skipped) — skipped lista cidades não processadas e por quê."""
    if include_experimental is None:
        include_experimental = bool(os.environ.get("INCLUDE_EXPERIMENTAL"))
    wanted = {c.lower() for c in cities_filter} if cities_filter else None

    registry = load_registry()
    all_permits: list[dict] = []
    skipped: list[dict] = []

    for state_name, state_data in registry.get("states", {}).items():
        if states_filter and state_name not in states_filter:
            continue

        for city_cfg in state_data.get("cities", []):
            city = city_cfg["name"]
            status = city_cfg.get("status")
            source_type = city_cfg.get("source_type")

            if wanted and city.lower() not in wanted:
                continue
            if status not in RUNNABLE:
                skipped.append({"city": city, "state": state_name, "reason": status})
                continue

            adapter_cls = ADAPTERS.get(source_type)
            if adapter_cls is None:
                skipped.append({"city": city, "state": state_name, "reason": f"sem adapter para '{source_type}'"})
                continue

            try:
                adapter = adapter_cls(
                    city=city,
                    state=state_name,
                    config=city_cfg.get("config", {}),
                    field_map=city_cfg.get("field_map", {}),
                    source_link=city_cfg.get("source_link", ""),
                )
                permits = adapter.fetch(days_back=days_back)
            except Exception as e:  # noqa: BLE001
                skipped.append({"city": city, "state": state_name, "reason": f"erro: {e}"})
                print(f"[erro] {city}, {state_name}: {e}")
                continue

            if status == "experimental" and not include_experimental and not wanted:
                print(f"[experimental] {city}, {state_name}: {len(permits)} permits (NÃO incluídos no dashboard)")
                for p in permits[:3]:
                    print(f"    exemplo: {p.get('permit_number')} | {p.get('address')} | {p.get('permit_type')} | "
                          f"{p.get('issue_date')} | valor={p.get('estimated_value')} | contratante={p.get('contractor')}")
                skipped.append({"city": city, "state": state_name, "reason": "experimental (em teste)"})
                continue

            tag = "ok" if status == "confirmed" else "experimental"
            print(f"[{tag}] {city}, {state_name}: {len(permits)} permits")
            all_permits.extend(permits)

    return all_permits, skipped


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", action="append", help="Filtrar por estado (pode repetir)")
    parser.add_argument("--city", action="append", help="Rodar só esta cidade (pode repetir)")
    parser.add_argument("--days-back", type=int, default=2)
    parser.add_argument("--out", default="latest_permits.json")
    args = parser.parse_args()

    permits, skipped = run(states_filter=args.state, days_back=args.days_back, cities_filter=args.city)

    Path(args.out).write_text(json.dumps(permits, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nTotal coletado: {len(permits)} permits")
    if skipped:
        print(f"\nCidades não processadas ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s['city']}, {s['state']}: {s['reason']}")
