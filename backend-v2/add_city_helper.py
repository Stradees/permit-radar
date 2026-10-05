"""
Ajuda a triar rapidamente qual tipo de sistema uma cidade usa, a partir da URL
do portal de permits dela. Não substitui a confirmação manual, mas acelera
MUITO o processo de mapear as ~340 cidades restantes de Massachusetts (e
depois outros estados).

Uso:
    python add_city_helper.py "https://cambridgema.portal.opengov.com/"
    python add_city_helper.py "https://data.somacity.gov/Building/Permits/abcd-1234"
"""

import sys

PATTERNS = [
    ("socrata", ["data.", ".gov/resource/", ".gov/dataset/"]),
    ("ckan", ["/dataset/", "ckan"]),
    ("arcgis", ["arcgis.com", "opendata.", "hub.arcgis"]),
    ("opengov_portal", ["portal.opengov.com"]),
    ("accela", ["accela.com", "citizenaccess"]),
    ("munis_css", ["munis", "tylertech"]),
    ("bsa_online", ["bsaonline.com"]),
]


def guess_source_type(url: str) -> str:
    url_lower = url.lower()
    for source_type, needles in PATTERNS:
        if any(n in url_lower for n in needles):
            return source_type
    return "unknown — inspecionar manualmente"


def registry_snippet(city: str, url: str) -> str:
    guess = guess_source_type(url)
    return f"""
      - name: {city}
        source_type: {guess}
        status: needs_field_mapping   # ou no_public_api, dependendo do que for confirmado
        portal_url: "{url}"
        notes: "Tipo sugerido automaticamente ({guess}) a partir da URL — confirmar manualmente antes de ativar."
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python add_city_helper.py <url_do_portal_de_permits> [nome_da_cidade]")
        sys.exit(1)

    url = sys.argv[1]
    city = sys.argv[2] if len(sys.argv) > 2 else "NOME_DA_CIDADE"

    print(f"Tipo sugerido: {guess_source_type(url)}\n")
    print("Cole isso em registry.yaml e ajuste:")
    print(registry_snippet(city, url))