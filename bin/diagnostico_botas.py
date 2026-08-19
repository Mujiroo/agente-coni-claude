#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Por que el grupo 'Botas de Bomberos' no tiene ni una impresion.

Quedo pendiente el 19-ago-2026: 15 keywords ENABLED y 0 impresiones en 30 dias,
mientras 'botas bombero' en amplia (grupo General) se lleva 393 impresiones y 8
conversiones. Falta saber si el grupo esta pausado o si no tiene anuncios aptos;
ese dia se agoto la cuota de la API antes de poder mirarlo.
"""
import json, subprocess, sys, os, collections

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "9907217991"


def gaql(q):
    cmd = ["bash", os.path.join(WS, "bin", "maton.sh"),
           "google-ads/v23/customers/%s/googleAds:search" % CID,
           "-X", "POST", "-H", "Content-Type: application/json",
           "-d", json.dumps({"query": q})]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout
    try:
        return json.loads(out)
    except Exception:
        return {"error": {"raw": out[:200]}}


def main():
    d = gaql("SELECT campaign.name, ad_group.name, ad_group.status, ad_group.id "
             "FROM ad_group WHERE campaign.status = 'ENABLED'")
    if "error" in d:
        print("SIN-QUOTA | %s" % json.dumps(d)[:120])
        return 2

    print("=== GRUPOS DE ANUNCIOS ===")
    botas = []
    for r in d.get("results", []):
        ag = r["adGroup"]
        marca = "  <<<" if "bota" in ag["name"].lower() else ""
        print("  %-18s | %-24s | %s%s" % (r["campaign"]["name"][:18], ag["name"][:24],
                                          ag["status"], marca))
        if "bota" in ag["name"].lower():
            botas.append((ag["id"], ag["name"], ag["status"]))

    d2 = gaql("SELECT ad_group.name, ad_group_ad.status, ad_group_ad.ad.id, "
              "ad_group_ad.policy_summary.approval_status "
              "FROM ad_group_ad WHERE campaign.status = 'ENABLED'")
    if "error" in d2:
        print("\nSIN-QUOTA al leer anuncios")
        return 2

    porgrupo = collections.defaultdict(list)
    for r in d2.get("results", []):
        a = r["adGroupAd"]
        porgrupo[r["adGroup"]["name"]].append(
            (a["status"], a.get("policySummary", {}).get("approvalStatus")))

    print("\n=== ANUNCIOS POR GRUPO ===")
    for ag, v in sorted(porgrupo.items()):
        print("  %-24s %d anuncios  %s" % (ag[:24], len(v), sorted(set(v))))

    print("\n=== VEREDICTO ===")
    for _, nombre, st in botas:
        ads = porgrupo.get(nombre, [])
        activos = [a for a in ads if a[0] == "ENABLED" and a[1] != "DISAPPROVED"]
        if st != "ENABLED":
            print("  '%s': el GRUPO esta %s. Esa es la causa." % (nombre, st))
        elif not ads:
            print("  '%s': grupo activo pero SIN NINGUN ANUNCIO. Esa es la causa." % nombre)
        elif not activos:
            print("  '%s': grupo activo, %d anuncios, ninguno apto (pausados o "
                  "rechazados). Esa es la causa." % (nombre, len(ads)))
        else:
            print("  '%s': grupo activo con %d anuncios aptos. NO es de estado: la "
                  "keyword amplia del grupo General le esta ganando la subasta."
                  % (nombre, len(activos)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
