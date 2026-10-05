"""
Roda a coleta (via run_all), descobre o que é NOVO desde a última vez
(SQLite), grava latest_permits.json para o dashboard, e envia o e-mail diário.

Variáveis de ambiente:
    RESEND_API_KEY   -> chave da Resend (https://resend.com)
    DIGEST_TO_EMAIL  -> e-mail que recebe o resumo diário
"""

import json
import os
import sqlite3
from pathlib import Path

import requests

from run_all import run

DB_PATH = Path(__file__).parent / "permit_history.db"
OUTPUT_JSON = Path(__file__).parent / "latest_permits.json"

RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
DIGEST_TO_EMAIL = os.environ.get("DIGEST_TO_EMAIL")


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


def build_email_html(new_permits: list[dict]) -> str:
    if not new_permits:
        return "<p>Nenhum permit novo hoje.</p>"

    rows = ""
    for p in sorted(new_permits, key=lambda x: x.get("estimated_value") or 0, reverse=True):
        value = f"${p['estimated_value']:,.0f}" if p.get("estimated_value") else "—"
        rows += f"""
        <tr>
            <td style="padding:8px;border-bottom:1px solid #333;">{p['address']}, {p['city']}</td>
            <td style="padding:8px;border-bottom:1px solid #333;">{p.get('permit_type') or '—'}</td>
            <td style="padding:8px;border-bottom:1px solid #333;">{p.get('contractor') or '—'}</td>
            <td style="padding:8px;border-bottom:1px solid #333;">{value}</td>
        </tr>"""

    return f"""
    <h2 style="font-family:sans-serif;">Permit Radar — {len(new_permits)} novo(s) permit(s) hoje</h2>
    <table style="border-collapse:collapse;width:100%;font-family:sans-serif;font-size:13px;">
        <thead>
            <tr>
                <th style="text-align:left;padding:8px;">Endereço</th>
                <th style="text-align:left;padding:8px;">Tipo</th>
                <th style="text-align:left;padding:8px;">Contractor</th>
                <th style="text-align:left;padding:8px;">Valor estimado</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    """


def send_email(html: str):
    if not RESEND_API_KEY or not DIGEST_TO_EMAIL:
        print("RESEND_API_KEY ou DIGEST_TO_EMAIL não configurados — pulando envio de e-mail.")
        return

    resp = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
        json={
            "from": "Permit Radar <alerts@yourdomain.com>",
            "to": [DIGEST_TO_EMAIL],
            "subject": "Permit Radar — novos permits hoje",
            "html": html,
        },
        timeout=20,
    )
    resp.raise_for_status()
    print("E-mail enviado:", resp.json())


def main():
    conn = init_db()
    all_permits, skipped = run(days_back=2)

    OUTPUT_JSON.write_text(json.dumps(all_permits, indent=2, ensure_ascii=False))

    new_permits = filter_new(conn, all_permits)
    print(f"Total coletado: {len(all_permits)} | Novos: {len(new_permits)} | Cidades puladas: {len(skipped)}")

    html = build_email_html(new_permits)
    send_email(html)


if __name__ == "__main__":
    main()