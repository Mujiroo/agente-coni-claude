#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica negativas pendientes en Google Ads (Sudtec). Idempotente y verificado.

Nacio el 19-ago-2026: Connie autorizo negativizar "relojes" (msg 171) y la API
devolvio 429 con "Retry in 35691 seconds" — la cuota de ESCRITURA es diaria y se
agoto. El script revisa que la negativa no exista, la crea y despues verifica.

Salidas: YA-EXISTEN | CREADAS | SIN-QUOTA | ERROR
"""
import json, subprocess, sys, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "9907217991"
CAMPS = ["customers/9907217991/campaigns/22490713380",
         "customers/9907217991/campaigns/23598502728"]
TERMINOS = ["reloj", "relojes"]


def maton(ruta, extra=None):
    cmd = ["bash", os.path.join(WS, "bin", "maton.sh"), ruta] + (extra or [])
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    try:
        return json.loads(out)
    except Exception:
        return {"error": {"raw": out[:200]}}


def es_quota(d):
    return "error" in d and "RESOURCE_EXHAUSTED" in json.dumps(d)


def existentes():
    q = ("SELECT campaign.resource_name, campaign_criterion.keyword.text "
         "FROM campaign_criterion WHERE campaign_criterion.negative = TRUE "
         "AND campaign_criterion.type = 'KEYWORD'")
    d = maton("google-ads/v23/customers/%s/googleAds:search" % CID,
              ["-X", "POST", "-H", "Content-Type: application/json",
               "-d", json.dumps({"query": q})])
    if es_quota(d):
        return None
    return {(r["campaign"]["resourceName"],
             r["campaignCriterion"]["keyword"]["text"].lower())
            for r in d.get("results", [])}


def main():
    hay = existentes()
    if hay is None:
        print("SIN-QUOTA | no pude leer las negativas actuales")
        return 2

    faltan = [(c, t) for c in CAMPS for t in TERMINOS if (c, t) not in hay]
    if not faltan:
        print("YA-EXISTEN | las %d negativas ya estaban puestas" % (len(CAMPS) * len(TERMINOS)))
        return 0

    ops = [{"create": {"campaign": c, "negative": True,
                       "keyword": {"text": t, "matchType": "BROAD"}}} for c, t in faltan]
    r = maton("google-ads/v23/customers/%s/campaignCriteria:mutate" % CID,
              ["-X", "POST", "-H", "Content-Type: application/json",
               "-d", json.dumps({"operations": ops})])
    if es_quota(r):
        print("SIN-QUOTA | la escritura sigue bloqueada (%d pendientes)" % len(faltan))
        return 2
    if "error" in r:
        print("ERROR | %s" % json.dumps(r)[:200])
        return 3

    hay2 = existentes()
    if hay2 is None:
        print("ERROR | escribi pero no pude verificar")
        return 3
    quedan = [(c, t) for c, t in faltan if (c, t) not in hay2]
    if quedan:
        print("ERROR | quedaron %d sin crear" % len(quedan))
        return 3
    print("CREADAS | %d negativas creadas y verificadas: %s" %
          (len(faltan), ", ".join(sorted({t for _, t in faltan}))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
