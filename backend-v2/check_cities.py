"""
Teste de saúde de todas as cidades do registry.yaml.

Para cada cidade ele:
  1. abre as páginas oficiais (portal_url / info_url) e diz se estão no ar;
  2. descobre a plataforma (OpenGov, Accela, PermitEyes, CivicPlus, Tyler...);
  3. acha, na página da prefeitura, os links para o portal real;
  4. procura endereços de dados escondidos (para destravar cidades ainda sem adaptador);
  5. verifica o robots.txt do site (boa prática de coleta);
  6. nas cidades com adaptador (confirmed/experimental), faz uma coleta de teste.

Gera `health_report.md` (e imprime o resumo no log).

Uso:
    python check_cities.py                 # todas
    python check_cities.py --city Newton   # uma cidade
"""

import argparse
import contextlib
import io
import re
import urllib.robotparser as robotparser
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

from run_all import load_registry
from sources.adapters import ADAPTERS, HEADERS

REPORT_PATH = Path(__file__).parent / "health_report.md"
TIMEOUT = 25

SIGNATURES = [
    ("OpenGov/ViewpointCloud", r"viewpointcloud|opengov"),
    ("Accela", r"accela|citizenaccess"),
    ("PermitEyes", r"permiteyes|fullcircletech"),
    ("CivicPlus", r"civicplus|civicengage"),
    ("Tyler (EnerGov/MUNIS)", r"tylerhost|energov|tylertech|munis"),
    ("ArcGIS", r"arcgis"),
    ("Socrata", r"socrata"),
    ("MyGov", r"mygov"),
    ("Municity", r"municity"),
]
PORTAL_HOST_RE = re.compile(
    r"https?://[\w.-]*(?:permiteyes|viewpointcloud|opengov|accela|tylerhost|mygov|municity|"
    r"civicpluswebopen|energov)[\w.-]*[^\s\"'<>)]*", re.I)


def fetch(url: str):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        deny = r.headers.get("x-deny-reason")
        return r.status_code, r.url, r.text[:400000], (f"bloqueado pelo ambiente ({deny})" if deny else None)
    except Exception as e:  # noqa: BLE001
        return None, url, "", str(e)[:140]


def detect_platforms(url: str, html: str) -> list[str]:
    hay = (url + " " + html[:200000]).lower()
    return [name for name, rx in SIGNATURES if re.search(rx, hay)]


def page_title(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip()[:90] if m else ""


def robots_status(url: str):
    try:
        p = urlparse(url)
        rp = robotparser.RobotFileParser()
        rp.set_url(f"{p.scheme}://{p.netloc}/robots.txt")
        rp.read()
        return rp.can_fetch("PermitRadar", url)
    except Exception:  # noqa: BLE001
        return None


def portal_links(base_url: str, html: str) -> list[str]:
    found = []
    for m in PORTAL_HOST_RE.findall(html):
        u = m.rstrip(".,;")
        if u not in found:
            found.append(u)
    for href in re.findall(r"href=[\"']([^\"']+)[\"']", html, re.I):
        if re.search(r"permiteyes|viewpointcloud|opengov|accela|tylerhost|mygov|civicpluswebopen", href, re.I):
            u = urljoin(base_url, href)
            if u not in found:
                found.append(u)
    return found[:8]


def data_endpoints(url: str, html: str) -> list[str]:
    """Procura, na página e nos scripts do mesmo site, endereços que parecem entregar dados."""
    pats = [r"(?:url|ajax|post|get|fetch|load)\s*[:(]\s*[\"']([^\"']+(?:\.php|\.json|/api/|/v\d/)[^\"']*)[\"']",
            r"[\"'](https?://[^\"']*(?:api|viewpointcloud)[^\"']*)[\"']"]
    found = []

    def grab(text: str, base: str):
        for rx in pats:
            for m in re.findall(rx, text, re.I):
                u = urljoin(base, m)
                if u not in found and not u.lower().endswith((".png", ".jpg", ".css")):
                    found.append(u)

    grab(html, url)
    host = urlparse(url).netloc
    for src in re.findall(r"<script[^>]+src=[\"']([^\"']+)[\"']", html, re.I)[:12]:
        full = urljoin(url, src)
        if urlparse(full).netloc != host or "jquery" in full.lower() or "bootstrap" in full.lower():
            continue
        try:
            js = requests.get(full, headers=HEADERS, timeout=TIMEOUT).text[:300000]
            grab(js, full)
        except Exception:  # noqa: BLE001
            pass
    return found[:12]


KEY_LINE_RE = re.compile(r"ajax|\$\.(?:post|get|ajax)|datatable|serverside|getpublic|getbuilding|getvalues|"
                         r"publicview|issue.?date|date.?from|date.?to|\burl\s*:", re.I)
LIB_RE = re.compile(r"jquery|bootstrap|moment|fullcalendar|select2|datepicker|metronic|font-?awesome|"
                    r"\.min\.js|google|maps|recaptcha|datatable|app\.js|layout|quick-sidebar|demo", re.I)


def grep_js(code: str, label: str, limit: int = 60) -> list[str]:
    """Mostra o essencial do código da página: os blocos \"ajax\" (com as linhas seguintes) e os
    parâmetros enviados (d.xxx = ...)."""
    lines = code.splitlines()
    out: list[str] = []
    shown = set()
    blocks = 0
    for i, line in enumerate(lines):
        if re.search(r"[\"']?ajax[\"']?\s*:\s*[{\"']", line, re.I) and blocks < 5:
            blocks += 1
            for k in range(i, min(i + 10, len(lines))):
                if k not in shown:
                    shown.add(k)
                    out.append(f"{label}:{k + 1}: {lines[k].strip()[:170]}")
        elif re.search(r"\bd\.\w+\s*=|getvalues|ajax/\w+\.php|\burl\s*=|\bvar url\b|SelectedTownId|town_?id|"
                       r"DeptName\s*=|tableId\s*=|\.php[\"']", line, re.I) and i not in shown:
            shown.add(i)
            out.append(f"{label}:{i + 1}: {line.strip()[:170]}")
        if len(out) >= limit:
            break
    return out


def probe_permiteyes(url: str, endpoints: list[str]) -> list[str]:
    """Mostra como a tela pública do PermitEyes pede os dados (para construirmos o leitor)."""
    L: list[str] = []
    code, final, html, err = fetch(url)
    if not html:
        return [f"não consegui abrir {url}: HTTP {code} {err or ''}"]
    inline = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.I | re.S)
    for n, block in enumerate(inline):
        L += grep_js(block, f"script-inline-{n + 1}")
    host = urlparse(final).netloc
    for src in re.findall(r"<script[^>]+src=[\"']([^\"']+)[\"']", html, re.I)[:30]:
        full = urljoin(final, src)
        if urlparse(full).netloc != host or LIB_RE.search(full):
            continue
        try:
            js = requests.get(full, headers=HEADERS, timeout=TIMEOUT).text[:400000]
            L += grep_js(js, full.split("/")[-1][:40])
        except Exception:  # noqa: BLE001
            pass
    # Tentativas diretas nos endereços de dados (POST no estilo DataTables)
    tries = []
    for e in endpoints + [urljoin(final, "ajax/getpublicview.php"), urljoin(final, "ajax/getbuildingpublichome.php")]:
        if ("/ajax/" in e or "getvalues" in e) and e not in tries:
            tries.append(e)
    body = {"draw": 1, "start": 0, "length": 3, "search[value]": ""}
    for ep in tries[:5]:
        try:
            r = requests.post(ep, headers=HEADERS, timeout=TIMEOUT, data=body)
            try:
                js = r.json()
                rows = js.get("data", [])[:2]
                clean = [[" ".join(re.sub(r"<[^>]+>", " ", str(c)).split()) for c in row] for row in rows]
                L.append(f"POST {ep} -> HTTP {r.status_code}; recordsTotal={js.get('recordsTotal')}; linhas de exemplo: {clean}")
            except Exception:  # noqa: BLE001
                vis = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", r.text, flags=re.S | re.I)
                vis = " ".join(re.sub(r"<[^>]+>", " ", vis).split())[:250]
                L.append(f"POST {ep} -> HTTP {r.status_code} (sem JSON) texto da página: {vis}")
        except Exception as e:  # noqa: BLE001
            L.append(f"POST {ep} -> erro {str(e)[:100]}")
    return L[:60]


def check_city(cfg: dict) -> dict:
    name, status = cfg["name"], cfg.get("status")
    urls = []
    for key in ("portal_url", "info_url"):
        if cfg.get(key) and cfg[key] not in urls:
            urls.append(cfg[key])
    res = {"name": name, "status": status, "access": cfg.get("access", ""), "type": cfg.get("source_type", ""),
           "pages": [], "portals": [], "endpoints": [], "dry": None, "probe": None, "dry_log": []}

    for u in urls:
        code, final, html, err = fetch(u)
        res["pages"].append({
            "url": u, "http": code, "final": final, "error": err,
            "platforms": detect_platforms(final, html) if html else [],
            "title": page_title(html) if html else "",
            "robots": robots_status(final) if (code and code < 400) else None,
        })
        if html:
            for link in portal_links(final, html):
                if link not in res["portals"]:
                    res["portals"].append(link)
            if "permiteyes" in (final + html[:200000]).lower() or "viewpointcloud" in (final + html[:200000]).lower():
                for ep in data_endpoints(final, html):
                    if ep not in res["endpoints"]:
                        res["endpoints"].append(ep)

    # Segunda passada: abre os portais encontrados na página da prefeitura (até 2)
    for link in res["portals"][:2]:
        code, final, html, err = fetch(link)
        if html:
            for ep in data_endpoints(final, html):
                if ep not in res["endpoints"]:
                    res["endpoints"].append(ep)
            res["pages"].append({"url": link, "http": code, "final": final, "error": err,
                                 "platforms": detect_platforms(final, html), "title": page_title(html),
                                 "robots": robots_status(final) if (code and code < 400) else None})

    # Sondagem do PermitEyes (só nas cidades marcadas com probe: true)
    if cfg.get("probe"):
        target = next((u for u in ([cfg.get("portal_url")] + res["portals"]) if u and "permiteyes" in u and "publicview" in u), None)
        if target:
            res["probe"] = {"url": target, "lines": probe_permiteyes(target, res["endpoints"])}

    return res


def dry_run(cfg: dict) -> dict:
    """Coleta de teste de uma cidade com adaptador; captura as mensagens do adaptador."""
    out = {"dry": None, "dry_log": []}
    buf = io.StringIO()
    try:
        ad = ADAPTERS[cfg["source_type"]](city=cfg["name"], state="massachusetts", config=cfg.get("config", {}),
                                          field_map=cfg.get("field_map", {}), source_link=cfg.get("source_link", ""))
        with contextlib.redirect_stdout(buf):
            rows = ad.fetch(days_back=14)
        sample = rows[0] if rows else None
        out["dry"] = {"ok": True, "count": len(rows),
                      "sample": ({k: sample.get(k) for k in ("permit_number", "address", "permit_type", "category",
                                                             "estimated_value", "contractor", "issue_date")}
                                 if sample else None)}
    except Exception as e:  # noqa: BLE001
        out["dry"] = {"ok": False, "error": str(e)[:300]}
    out["dry_log"] = [ln for ln in buf.getvalue().splitlines() if ln.strip()][:25]
    return out


def render(results: list[dict]) -> str:
    L = [f"# Permit Radar — teste de saúde das cidades ({date.today().isoformat()})", ""]
    counts: dict[str, int] = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    L.append("Resumo por situação: " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    L.append("")
    L.append("| Cidade | Situação | Acesso | Páginas no ar | Plataforma detectada | Coleta de teste |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for r in results:
        ok = sum(1 for p in r["pages"] if p["http"] and p["http"] < 400)
        pages = f"{ok}/{len(r['pages'])}" if r["pages"] else "—"
        plats = sorted({pl for p in r["pages"] for pl in p["platforms"]})
        dry = "—"
        if r["dry"]:
            dry = f"{r['dry']['count']} permits" if r["dry"]["ok"] else "ERRO"
        L.append(f"| {r['name']} | {r['status']} | {r['access']} | {pages} | {', '.join(plats) or '—'} | {dry} |")
    L.append("")
    L.append("## Detalhes por cidade")
    for r in results:
        L.append(f"\n### {r['name']} — {r['status']}")
        for p in r["pages"]:
            rb = {True: "permitido", False: "NÃO permitido", None: "n/d"}[p["robots"]]
            L.append(f"- {p['url']} → HTTP {p['http']}"
                     + (f" ({p['error']})" if p["error"] else "")
                     + (f" · título: {p['title']}" if p["title"] else "")
                     + (f" · plataforma: {', '.join(p['platforms'])}" if p["platforms"] else "")
                     + f" · robots.txt: {rb}")
        if r["portals"]:
            L.append("- Portais encontrados na página da prefeitura: " + " | ".join(r["portals"]))
        if r["endpoints"]:
            L.append("- Endereços de dados candidatos: " + " | ".join(r["endpoints"]))
        if r["dry"]:
            if r["dry"]["ok"]:
                L.append(f"- Coleta de teste (14 dias): {r['dry']['count']} permits. Exemplo: {r['dry']['sample']}")
            else:
                L.append(f"- Coleta de teste FALHOU: {r['dry']['error']}")
            if r.get("dry_log"):
                L.append("- Mensagens da coleta de teste:")
                L += [f"    {ln}" for ln in r["dry_log"]]
        if r.get("probe"):
            L.append(f"- Sondagem do PermitEyes em {r['probe']['url']}:")
            L.append("```")
            L += r["probe"]["lines"]
            L.append("```")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", action="append", help="Verificar só esta cidade (pode repetir)")
    args = ap.parse_args()
    wanted = {c.lower() for c in args.city} if args.city else None

    cities = []
    for state, data in load_registry().get("states", {}).items():
        for c in data.get("cities", []):
            if not wanted or c["name"].lower() in wanted:
                cities.append(c)

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(check_city, cities))

    # Coletas de teste, uma de cada vez (para as mensagens não se misturarem)
    by_name = {c["name"]: c for c in cities}
    for r in results:
        cfg = by_name[r["name"]]
        if cfg.get("status") in ("confirmed", "experimental") or (
                cfg.get("source_type") == "permiteyes" and cfg.get("config")):
            if cfg.get("source_type") in ADAPTERS:
                r.update(dry_run(cfg))

    report = render(results)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
