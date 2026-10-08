"""
Descoberta automática de cidades monitoráveis (MA, NH, RI e CT).

O que faz:
  1. Monta a lista de TODAS as cidades/vilas dos 4 estados (Censo dos EUA; se falhar, usa uma lista básica).
  2. Para cada uma, testa endereços de sistemas conhecidos:
       - PermitEyes (Public View)  -> pode ser coletado (robots.txt permite)
       - OpenGov / ViewpointCloud  -> existe, mas o robots.txt NÃO permite coleta automática
       - Tyler EnerGov             -> existe (precisa de análise)
  3. Cada PermitEyes encontrado é VALIDADO de ponta a ponta com o mesmo leitor do Radar
     (lê as colunas, acha os registros novos, conta permits dos últimos 14 dias).
  4. Escreve:
       discovery_report.md                   -> relatório para leitura
       sources/registry_discovered.yaml      -> cidades novas, prontas como "experimental"
     (cidades que já estão no cadastro, ou já no arquivo de descobertas, NUNCA são alteradas)

Uso:
    python discover_towns.py                       # os 4 estados
    python discover_towns.py --states MA NH        # só alguns
    python discover_towns.py --no-validate         # só testa se os endereços existem
"""

import argparse
import contextlib
import io
import re
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

import requests
import yaml

from run_all import load_registry
from sources.adapters import HEADERS, PermitEyesAdapter

HERE = Path(__file__).parent
REPORT = HERE / "discovery_report.md"
DISCOVERED = HERE / "sources" / "registry_discovered.yaml"
TIMEOUT = 15

STATES = {  # sigla: (chave no cadastro, FIPS, nome por extenso)
    "MA": ("massachusetts", "25", "Massachusetts"),
    "NH": ("new_hampshire", "33", "New Hampshire"),
    "RI": ("rhode_island", "44", "Rhode Island"),
    "CT": ("connecticut", "09", "Connecticut"),
}

# Lista básica, usada só se o Censo não puder ser baixado
SEEDS = {
    "MA": ["Boston", "Worcester", "Springfield", "Cambridge", "Lowell", "Brockton", "Quincy", "Lynn", "New Bedford",
           "Fall River", "Newton", "Somerville", "Lawrence", "Framingham", "Haverhill", "Waltham", "Malden", "Medford",
           "Taunton", "Chicopee", "Weymouth", "Revere", "Peabody", "Methuen", "Barnstable", "Pittsfield", "Arlington",
           "Attleboro", "Salem", "Westfield", "Leominster", "Fitchburg", "Beverly", "Marlborough", "Woburn", "Amherst",
           "Braintree", "Shrewsbury", "Chelmsford", "Dartmouth", "Chelsea", "Everett", "Natick", "Randolph", "Watertown",
           "Franklin", "Billerica", "Needham", "Dedham", "Hingham", "Concord", "Mashpee", "Falmouth", "Becket", "Dalton",
           "Lee", "Lenox", "Monterey", "Richmond", "Sheffield", "Great Barrington", "Stockbridge", "Reading",
           "North Reading", "Danvers", "Brookline", "Lexington", "Sudbury", "Northampton"],
    "NH": ["Manchester", "Nashua", "Concord", "Derry", "Dover", "Rochester", "Salem", "Merrimack", "Hudson", "Londonderry",
           "Keene", "Portsmouth", "Laconia", "Claremont", "Lebanon", "Hampton", "Exeter", "Milford", "Durham", "Bedford",
           "Goffstown", "Hooksett", "Windham", "Pelham", "Hanover", "Conway", "Pembroke", "Somersworth", "Newmarket"],
    "RI": ["Providence", "Cranston", "Warwick", "Pawtucket", "East Providence", "Woonsocket", "Coventry", "Cumberland",
           "North Providence", "South Kingstown", "West Warwick", "Johnston", "North Kingstown", "Newport", "Bristol",
           "Westerly", "Smithfield", "Lincoln", "Central Falls", "Portsmouth", "Barrington", "Middletown"],
    "CT": ["Hartford", "New Haven", "Stamford", "Bridgeport", "Waterbury", "Norwalk", "Danbury", "New Britain",
           "West Hartford", "Greenwich", "Hamden", "Meriden", "Bristol", "Manchester", "West Haven", "Milford",
           "Stratford", "East Hartford", "Middletown", "Wallingford", "Southington", "Shelton", "Norwich", "Torrington",
           "Trumbull", "Glastonbury", "Naugatuck", "Newington", "Cheshire", "Vernon", "Windsor", "New London", "Fairfield",
           "Westport", "Darien", "New Canaan", "Ridgefield", "Berlin", "Durham", "Enfield", "Tolland", "North Haven"],
}

# Cidades de Berkshire (MA) usam um padrão de endereço próprio no PermitEyes
BERKSHIRE = {"becket", "dalton", "lee", "lenox", "monterey", "richmond", "sheffield", "stockbridge", "greatbarrington",
             "pittsfield", "adams", "lanesborough", "williamstown", "northadams", "westernstockbridge", "egremont",
             "newmarlborough", "otis", "sandisfield", "tyringham", "washington", "windsor", "hinsdale", "peru", "cheshire",
             "clarksburg", "florida", "hancock", "mountwashington", "alford", "newashford", "savoy", "wendell"}

EXTRA_CHECKS = [  # endereços específicos que valem uma olhada
    ("Nashua NH - serviço da cidade (permits, MapServer)",
     "https://newgis.nashuanh.gov/arcgisapp3/rest/services/CommunityDevelopment/Building_Permits_for_AGOL/MapServer?f=json"),
    ("Dover NH - portal de permits", "https://permits.dover.nh.gov"),
    ("Concord NH - portal (Tyler CSS)", "https://www.concordnh.gov/1888/Citizen-Self-Service-Permits"),
    ("Enfield CT - arquivo de permits mensais", "https://www.enfield-ct.gov/Archive.aspx?AMID=37"),
    ("Milford CT - permits emitidos por mês", "https://www.ci.milford.ct.us/building-inspection/pages/list-of-permits-issued-by-month"),
    ("Tolland CT - viewmypermitct", "https://www.viewmypermitct.org/"),
    ("New Haven CT - portal", "https://www.newhavenct.gov/"),
]


def slugify(name: str) -> str:
    return re.sub(r"[^a-z]", "", name.lower())


def load_towns(st: str, fips: str) -> tuple[list[str], str]:
    """Todas as cidades/vilas do estado (Censo). Devolve (lista, origem)."""
    sources = []
    for year in (2023, 2022, 2021, 2020):
        sources.append((f"https://www2.census.gov/geo/docs/maps-data/data/gazetteer/{year}_Gazetteer/{year}_gaz_cousubs_{fips}.txt", "txt"))
    for year in (2023, 2022, 2021, 2020):
        sources.append((f"https://www2.census.gov/geo/docs/maps-data/data/gazetteer/{year}_Gazetteer/{year}_Gaz_cousubs_national.zip", "zip"))
    for url, kind in sources:
        try:
            r = requests.get(url, headers=HEADERS, timeout=60)
            if r.status_code != 200:
                continue
            if kind == "zip":
                z = zipfile.ZipFile(io.BytesIO(r.content))
                text = z.read(z.namelist()[0]).decode("latin-1")
            else:
                text = r.content.decode("latin-1")
            names = parse_gazetteer(text, st)
            if len(names) >= 20:
                return names, url
        except Exception:  # noqa: BLE001
            continue
    return sorted(SEEDS[st]), "lista básica interna (o Censo não respondeu)"


def parse_gazetteer(text: str, st: str) -> list[str]:
    rows = text.splitlines()
    header = [h.strip() for h in rows[0].split("\t")]
    idx = {h: i for i, h in enumerate(header)}
    names = set()
    for line in rows[1:]:
        parts = line.split("\t")
        if len(parts) < len(header) - 1 or parts[idx["USPS"]].strip() != st:
            continue
        name = parts[idx["NAME"]].strip()
        if "not defined" in name.lower():
            continue
        m = re.match(r"^(.*?)\s+(?:Town\s+city|town|city)$", name, re.I)
        if m:
            names.add(m.group(1).strip())
    return sorted(names)


def get(url: str):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        return r.status_code, r.url, r.text[:40000]
    except Exception as e:  # noqa: BLE001
        return None, url, str(e)[:80]


def probe_town(args):
    name, st = args
    slug = slugify(name)
    out = {"name": name, "st": st, "slug": slug, "permiteyes": None, "opengov": None, "tyler": None}

    candidates = [f"https://permiteyes.us/{slug}/publicview.php"]
    if st == "MA" and slug in BERKSHIRE:
        candidates.append(f"https://permiteyes.us/berkshire/{slug}publicview.php")
    for url in candidates:
        code, final, text = get(url)
        low = text.lower() if isinstance(text, str) else ""
        if code == 200 and "permiteyes" in low and ("publicview" in low or "public view" in low) and "login.php" not in final:
            out["permiteyes"] = url
            break

    for host in (f"{slug}{st.lower()}.portal.opengov.com", f"{slug}{st.lower()}.viewpointcloud.com",
                 f"{slug}.portal.opengov.com", f"{slug}{st.lower()}.viewpointcloud.io"):
        code, final, text = get(f"https://{host}/")
        # só vale se a própria página citar a cidade (evita falso positivo de endereços "coringa")
        if code and code < 400 and isinstance(text, str) and name.lower() in text.lower():
            out["opengov"] = host
            break

    code, final, text = get(f"https://{slug}{st.lower()}-energovpub.tylerhost.net/apps/selfservice")
    if code and code < 400 and isinstance(text, str) and name.lower() in text.lower():
        out["tyler"] = f"{slug}{st.lower()}-energovpub.tylerhost.net"
    return out


def validate_permiteyes(name: str, state_key: str, url: str) -> dict:
    cfg = {"portal_url": url, "page_size": 100, "max_pages": 5}
    if "/berkshire/" in url:
        cfg.update({"drop_headers": ["owner"], "town_name": name})
    buf = io.StringIO()
    res = {"ok": False, "count": 0, "error": None, "config": cfg, "fields": [], "sample": None, "log": []}
    try:
        ad = PermitEyesAdapter(city=name, state=state_key, config=cfg, field_map={}, source_link=url)
        with contextlib.redirect_stdout(buf):
            rows = ad.fetch(days_back=14)
        res["ok"], res["count"] = True, len(rows)
        if rows:
            r0 = rows[0]
            res["sample"] = {k: r0.get(k) for k in ("permit_number", "address", "permit_type", "category", "issue_date")}
            res["fields"] = sorted(k for k in ("estimated_value", "contractor", "description") if any(r.get(k) for r in rows))
    except Exception as e:  # noqa: BLE001
        res["error"] = str(e)[:200]
    res["log"] = [ln for ln in buf.getvalue().splitlines() if ln.strip()][:6]
    return res


def known_names() -> set[str]:
    names = set()
    for state, data in load_registry().get("states", {}).items():
        for c in data.get("cities", []):
            names.add((state, c["name"].lower()))
    return names


def entry_for(name: str, state_key: str, v: dict, url: str) -> dict:
    return {
        "name": name, "source_type": "permiteyes", "status": "experimental",
        "access": "search_by_address_or_record", "portal_url": url, "config": v["config"], "field_map": {},
        "source_link": url,
        "notes": f"Descoberta automática em {date.today().isoformat()} (PermitEyes Public View). "
                 f"Validação: {v['count']} permits em 14 dias; campos extras: {', '.join(v['fields']) or 'nenhum'}.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--states", nargs="*", default=list(STATES), help="Siglas: MA NH RI CT")
    ap.add_argument("--no-validate", action="store_true")
    args = ap.parse_args()

    known = known_names()
    existing_discovered = {}
    if DISCOVERED.exists():
        existing_discovered = yaml.safe_load(DISCOVERED.read_text(encoding="utf-8")) or {}
    disc_states = existing_discovered.get("states", {})
    disc_names = {(s, c["name"].lower()) for s, d in disc_states.items() for c in d.get("cities", [])}

    L = [f"# Permit Radar — varredura de descoberta ({date.today().isoformat()})", ""]
    summary = []
    sections = []

    for st in args.states:
        key, fips, label = STATES[st]
        towns, origin = load_towns(st, fips)
        print(f"[{st}] {len(towns)} cidades ({origin})", flush=True)
        with ThreadPoolExecutor(max_workers=12) as pool:
            probes = list(pool.map(probe_town, [(t, st) for t in towns]))

        pe = [p for p in probes if p["permiteyes"]]
        og = [p for p in probes if p["opengov"]]
        ty = [p for p in probes if p["tyler"]]
        validated, failed, new_entries = [], [], []

        for p in pe:
            if args.no_validate:
                continue
            v = validate_permiteyes(p["name"], key, p["permiteyes"])
            p["validation"] = v
            (validated if v["ok"] and v["count"] > 0 else failed).append(p)
            already = (key, p["name"].lower()) in known or (key, p["name"].lower()) in disc_names
            if v["ok"] and v["count"] > 0 and not already:
                new_entries.append(entry_for(p["name"], key, v, p["permiteyes"]))
            time.sleep(0.5)

        if new_entries:
            block = disc_states.setdefault(key, {"cities": []})
            block.setdefault("cities", []).extend(new_entries)

        summary.append((label, len(towns), len(pe), len(validated), len(og), len(ty), len(new_entries)))
        sec = [f"## {label}", "", f"Cidades verificadas: {len(towns)} (fonte da lista: {origin})", ""]
        if pe:
            sec += ["### PermitEyes (a coleta é permitida)", "", "| Cidade | Endereço | Validação | Campos extras |", "| --- | --- | --- | --- |"]
            for p in pe:
                v = p.get("validation")
                if v is None:
                    sec.append(f"| {p['name']} | {p['permiteyes']} | não validada | |")
                elif v["ok"]:
                    sec.append(f"| {p['name']} | {p['permiteyes']} | {v['count']} permits em 14 dias | {', '.join(v['fields']) or '—'} |")
                else:
                    sec.append(f"| {p['name']} | {p['permiteyes']} | FALHOU: {v['error']} | |")
            sec.append("")
        if og:
            sec += ["### OpenGov / ViewpointCloud (existe, mas o robots.txt não permite coleta automática)", "",
                    ", ".join(f"{p['name']} ({p['opengov']})" for p in og), ""]
        if ty:
            sec += ["### Tyler EnerGov (a analisar)", "", ", ".join(f"{p['name']} ({p['tyler']})" for p in ty), ""]
        if not (pe or og or ty):
            sec += ["Nenhum sistema conhecido foi encontrado pelos endereços testados.", ""]
        sections.append("\n".join(sec))

    L += ["## Resumo", "", "| Estado | Cidades | PermitEyes | Validadas | OpenGov | Tyler | Novas no cadastro |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in summary:
        L.append("| " + " | ".join(str(x) for x in row) + " |")
    L.append("")
    L += sections

    L += ["## Endereços avaliados individualmente", "", "| Item | HTTP | Observação |", "| --- | --- | --- |"]
    for label, url in EXTRA_CHECKS:
        code, final, text = get(url)
        note = " ".join(re.sub(r"<[^>]+>", " ", str(text)).split())[:110] if code else str(text)
        L.append(f"| {label} | {code} | {note} |")

    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    if disc_states:
        DISCOVERED.write_text("# Gerado por discover_towns.py. Cidades já existentes aqui nunca são alteradas pela varredura.\n"
                              + yaml.safe_dump({"states": disc_states}, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
