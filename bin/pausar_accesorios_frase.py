#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pausa la keyword 'accesorios bomberos' en concordancia FRASE (Sudtec).

Autorizado por Connie el 19-ago-2026 (msg 164). Se creo porque la API de Google
Ads empezo a devolver 429 y el cambio quedo sin aplicar ni verificar.

Es idempotente: si ya esta pausada, no hace nada y lo dice.
Salidas: YA-PAUSADA | PAUSADA-AHORA | SIGUE-ACTIVA | SIN-QUOTA | ERROR
"""
import json, subprocess, sys, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "9907217991"
RES = "customers/9907217991/adGroupCriteria/181820804074~452736550247"
KW, MT = "accesorios bomberos", "PHRASE"


def maton(ruta, extra=None):
    cmd = ["bash", os.path.join(WS, "bin", "maton.sh"), ruta] + (extra or [])
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    try:
        return json.loads(out)
    except Exception:
        return {"error": {"raw": out[:200]}}


def es_quota(d):
    return "error" in d and "RESOURCE_EXHAUSTED" in json.dumps(d)


def estado():
    q = ("SELECT ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type, "
         "ad_group_criterion.status FROM ad_group_criterion WHERE "
         "ad_group_criterion.keyword.text = '%s' AND ad_group_criterion.type = 'KEYWORD'" % KW)
    d = maton("google-ads/v23/customers/%s/googleAds:search" % CID,
              ["-X", "POST", "-H", "Content-Type: application/json",
               "-d", json.dumps({"query": q})])
    if es_quota(d):
        return None, d
    for r in d.get("results", []):
        c = r["adGroupCriterion"]
        if c["keyword"]["matchType"] == MT:
            return c["status"], d
    return "NO-ENCONTRADA", d


def main():
    st, d = estado()
    if st is None:
        print("SIN-QUOTA | no pude leer el estado")
        return 2
    if st == "PAUSED":
        print("YA-PAUSADA | la keyword en frase esta pausada, nada que hacer")
        return 0
    if st == "NO-ENCONTRADA":
        print("ERROR | no encontre la keyword en frase")
        return 3

    body = {"operations": [{"update": {"resourceName": RES, "status": "PAUSED"},
                            "updateMask": "status"}]}
    r = maton("google-ads/v23/customers/%s/adGroupCriteria:mutate" % CID,
              ["-X", "POST", "-H", "Content-Type: application/json",
               "-d", json.dumps(body)])
    if es_quota(r):
        print("SIN-QUOTA | la escritura sigue bloqueada por cuota")
        return 2

    st2, _ = estado()
    if st2 == "PAUSED":
        print("PAUSADA-AHORA | verificado: quedo en PAUSED")
        return 0
    print("SIGUE-ACTIVA | la escritura respondio pero el estado es %s" % st2)
    return 4


if __name__ == "__main__":
    sys.exit(main())
