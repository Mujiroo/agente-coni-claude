#!/usr/bin/env python3
"""Barrida de remitentes bloqueados.

Connie pidio (25-ago-2026) que los correos de AliExpress no le lleguen. El filtro
NATIVO de Gmail no se puede crear desde aca: ni Maton ni Composio tienen el scope
`gmail.settings.basic` (los dos dan 403 ACCESS_TOKEN_SCOPE_INSUFFICIENT en
settings/filters). Lo que si tenemos es permiso de MODIFICAR mensajes, asi que
esta barrida hace lo mismo por fuera: cada pasada manda a la PAPELERA lo que haya
llegado de los dominios de memory/estado/remitentes_bloqueados.json.

Papelera, no borrado definitivo: Gmail la guarda 30 dias, o sea es reversible.

Salida: 'SIN-NOVEDAD' si no habia nada, o 'LIMPIADOS: n' con el detalle.
"""
import json, os, sys, urllib.request, urllib.parse, urllib.error

WS = os.environ.get("AGENT_WORKSPACE", "/home/agent/workspace")
LISTA = os.path.join(WS, "memory/estado/remitentes_bloqueados.json")
BASE = "https://api.maton.ai/"


def clave():
    k = os.environ.get("MATON_API_KEY")
    if k:
        return k
    for l in open(os.path.join(WS, ".env")):
        if l.startswith("MATON_API_KEY="):
            return l.split("=", 1)[1].strip().strip("\"'")
    sys.exit("ERROR: no encuentro MATON_API_KEY")


KEY = clave()


def api(ruta, body=None):
    datos = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos,
        headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"},
        method="POST" if body is not None else "GET")
    with urllib.request.urlopen(req, timeout=90) as r:
        crudo = r.read()
    return json.loads(crudo) if crudo else {}


def main():
    dominios = [r["dominio"] for r in json.load(open(LISTA))["remitentes"]]
    if not dominios:
        print("SIN-NOVEDAD (no hay remitentes bloqueados)")
        return

    # solo lo que sigue vivo en el buzon: lo ya mandado a papelera no vuelve a salir
    q = "(" + " OR ".join("from:" + d for d in dominios) + ") -in:trash -in:spam"
    ids, tok = [], None
    while True:
        ruta = "google-mail/gmail/v1/users/me/messages?maxResults=500&q=" + urllib.parse.quote(q)
        if tok:
            ruta += "&pageToken=" + tok
        d = api(ruta)
        ids += [m["id"] for m in d.get("messages", [])]
        tok = d.get("nextPageToken")
        if not tok:
            break

    if not ids:
        print("SIN-NOVEDAD")
        return

    for i in range(0, len(ids), 900):   # el batch de Gmail admite hasta 1000
        api("google-mail/gmail/v1/users/me/messages/batchModify",
            {"ids": ids[i:i + 900], "addLabelIds": ["TRASH"],
             "removeLabelIds": ["INBOX", "UNREAD"]})

    print("LIMPIADOS: %d (%s)" % (len(ids), ", ".join(dominios)))


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as e:
        print("ERROR HTTP %s: %s" % (e.code, e.read().decode()[:300]))
        sys.exit(1)
