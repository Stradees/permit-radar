"""
Roda a coleta, descobre o que é NOVO desde a última vez (SQLite), acumula o
histórico em latest_permits.json (usado pelo dashboard) e envia o e-mail diário.

Variáveis de ambiente:
    RESEND_API_KEY     -> chave da Resend (https://resend.com)
    DIGEST_TO_EMAIL    -> e-mail que recebe o resumo diário
    DIGEST_FROM_EMAIL  -> (opcional) remetente. Padrão: o remetente de teste da Resend
    DAYS_BACK          -> (opcional) quantos dias para trás buscar. Padrão: 14
"""

import html
import json
import os
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import requests

from run_all import run

DB_PATH = Path(__file__).parent / "permit_history.db"
OUTPUT_JSON = Path(__file__).parent / "latest_permits.json"

RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
DIGEST_TO_EMAIL = os.environ.get("DIGEST_TO_EMAIL")
DIGEST_FROM_EMAIL = os.environ.get("DIGEST_FROM_EMAIL", "Permit Radar <onboarding@resend.dev>")
DAYS_BACK = int(os.environ.get("DAYS_BACK", "14"))

KEEP_DAYS = 90          # quantos dias de histórico o dashboard guarda
MAX_EMAIL_ROWS = 100    # máximo de linhas no e-mail (as de maior valor primeiro)


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS seen_permits (
            permit_number TEXT,
            source_city TEXT,
            source_state TEXT,
            PRIMARY KEY (permit_number, source_city, source_state)
        )
    """)
    conn.commit()
    return conn


def permit_key(p: dict) -> str:
    return f"{p.get('source_state')}|{p.get('source_city')}|{p.get('permit_number')}"


def filter_new(conn, permits: list[dict]) -> list[dict]:
    new_ones = []
    for p in permits:
        cur = conn.execute(
            "SELECT 1 FROM seen_permits WHERE permit_number=? AND source_city=? AND source_state=?",
            (p["permit_number"], p["source_city"], p["source_state"]),
        )
        if cur.fetchone() is None:
            new_ones.append(p)
            conn.execute(
                "INSERT OR IGNORE INTO seen_permits (permit_number, source_city, source_state) VALUES (?, ?, ?)",
                (p["permit_number"], p["source_city"], p["source_state"]),
            )
    conn.commit()
    return new_ones


def load_existing() -> list[dict]:
    if OUTPUT_JSON.exists():
        try:
            return json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            return []
    return []


def merge_history(existing: list[dict], fresh: list[dict]) -> list[dict]:
    """Junta o histórico antigo com os permits de hoje (sem duplicar) e descarta o que passou de KEEP_DAYS."""
    merged = {permit_key(p): p for p in existing if p.get("permit_number")}
    for p in fresh:
        merged[permit_key(p)] = p
    cutoff = (date.today() - timedelta(days=KEEP_DAYS)).isoformat()
    kept = [p for p in merged.values() if not p.get("issue_date") or p["issue_date"] >= cutoff]
    kept.sort(key=lambda p: p.get("issue_date") or "", reverse=True)
    return kept


def esc(v) -> str:
    return html.escape(str(v)) if v not in (None, "") else "—"


def build_email_html(new_permits: list[dict]) -> str:
    ordered = sorted(new_permits, key=lambda x: x.get("estimated_value") or 0, reverse=True)
    shown = ordered[:MAX_EMAIL_ROWS]

    rows = ""
    for p in shown:
        value = f"${p['estimated_value']:,.0f}" if p.get("estimated_value") else "—"
        rows += f"""
        <tr>
            <td style="padding:8px;border-bottom:1px solid #ddd;">{esc(p.get('address'))}<br><small style="color:#666;">{esc(p.get('city'))} · {esc(p.get('issue_date'))}</small></td>
            <td style="padding:8px;border-bottom:1px solid #ddd;">{esc(p.get('permit_type'))}</td>
            <td style="padding:8px;border-bottom:1px solid #ddd;">{esc(p.get('contractor'))}</td>
            <td style="padding:8px;border-bottom:1px solid #ddd;text-align:right;"><b>{value}</b></td>
        </tr>"""

    extra = ""
    if len(ordered) > len(shown):
        extra = f"<p style='font-family:sans-serif;font-size:12px;color:#666;'>Mostrando os {len(shown)} de maior valor. Há {len(ordered) - len(shown)} outros no dashboard.</p>"

    return f"""
    <h2 style="font-family:sans-serif;color:#2d7a0a;">Permit Radar — {len(new_permits)} novo(s) permit(s)</h2>
    <table style="border-collapse:collapse;width:100%;font-family:sans-serif;font-size:13px;">
        <thead>
            <tr style="background:#f2f7ee;">
                <th style="text-align:left;padding:8px;">Endereço</th>
                <th style="text-align:left;padding:8px;">Tipo</th>
                <th style="text-align:left;padding:8px;">Contractor</th>
                <th style="text-align:right;padding:8px;">Valor estimado</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    {extra}
    """


def send_email(html_body: str, count: int):
    if not RESEND_API_KEY or not DIGEST_TO_EMAIL:
        print("RESEND_API_KEY ou DIGEST_TO_EMAIL não configurados — pulando envio de e-mail.")
        return
    try:
        resp = requests.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
            json={
                "from": DIGEST_FROM_EMAIL,
                "to": [DIGEST_TO_EMAIL],
                "subject": f"Permit Radar — {count} novo(s) permit(s)",
                "html": html_body,
            },
            timeout=30,
        )
        if resp.status_code >= 400:
            print(f"[erro] envio de e-mail falhou: HTTP {resp.status_code} — {resp.text[:300]}")
            return
        print("E-mail enviado:", resp.json())
    except Exception as e:  # noqa: BLE001
        print(f"[erro] envio de e-mail falhou: {e}")


def main():
    conn = init_db()
    fresh, skipped = run(days_back=DAYS_BACK)

    history = merge_history(load_existing(), fresh)
    OUTPUT_JSON.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")

    new_permits = filter_new(conn, fresh)
    print(f"Coletados agora: {len(fresh)} | Novos: {len(new_permits)} | "
          f"Histórico no dashboard: {len(history)} | Cidades puladas: {len(skipped)}")

    if new_permits:
        send_email(build_email_html(new_permits), len(new_permits))
    else:
        print("Nenhum permit novo — e-mail não enviado.")


if __name__ == "__main__":
    main()
