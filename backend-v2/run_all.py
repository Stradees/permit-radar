"""
Runner central. Não sabe nada sobre cidades específicas — só lê o registry.yaml
e delega pro adapter certo. Adicionar cobertura (mais cidades, mais estados) é
uma mudança de configuração, não de código.

Uso:
    python run_all.py                  # roda todos os estados/cidades "confirmed"
    python run_all.py --state massachusetts
"""

import argparse
import json
from pathlib import Path

import yaml

from sources.adapters import ADAPTERS

REGISTRY_PATH = Path(__file__).parent / "sources" / "registry.yaml"


def load_registry() -> dict:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run(states_filter: list[str] | None = None, days_back: int = 2) -> tuple[list[dict], list[dict]]:
    """Retorna (permits, skipped) — skipped lista cidades não processadas e por quê."""
    registry = load_registry()
    all_permits = []
    skipped = []

    for state_name, state_data in registry.get("states", {}).items():
        if states_filter and state_name not in states_filter:
            continue

        for city_cfg in state_data.get("cities", []):
            city = city_cfg["name"]
            status = city_cfg.get("status")
            source_type = city_cfg.get("source_type")

            if status != "confirmed":
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
                    config=city_cfg["config"],
                    field_map=city_cfg["field_map"],
                    source_link=city_cfg.get("source_link", ""),
                )
                permits = adapter.fetch(days_back=days_back)
                print(f"[ok] {city}, {state_name}: {len(permits)} permits")
                all_permits.extend(permits)
            except Exception as e:
                skipped.append({"city": city, "state": state_name, "reason": f"erro: {e}"})
                print(f"[erro] {city}, {state_name}: {e}")

    return all_permits, skipped


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", action="append", help="Filtrar por estado (pode repetir)")
    parser.add_argument("--days-back", type=int, default=2)
    parser.add_argument("--out", default="latest_permits.json")
    args = parser.parse_args()

    permits, skipped = run(states_filter=args.state, days_back=args.days_back)

    Path(args.out).write_text(json.dumps(permits, indent=2, ensure_ascii=False))

    print(f"\nTotal coletado: {len(permits)} permits")
    if skipped:
        print(f"\nCidades não processadas ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s['city']}, {s['state']}: {s['reason']}")
