#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crea el grupo de anuncios 'Botas' en Campana Sudtec (Google Ads).

Aprobado por Connie el 19-ago-2026 (msg 179), con el texto del anuncio a la vista
(msg 178). Quedo pendiente porque la cuota de ESCRITURA de la API se agoto.

NO TOCA NINGUN PRESUPUESTO. El grupo vive dentro de una campana que ya existe y
comparte su presupuesto diario. El techo de 300.000 CLP/mes no se mueve.

Es idempotente: si el grupo ya existe, no lo duplica. Verifica al final.
Salidas: YA-EXISTE | CREADO | SIN-QUOTA | ERROR
"""
import json, subprocess, sys, os

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "9907217991"
CAMP = "customers/9907217991/campaigns/22490713380"      # Campana Sudtec
AG_GENERAL = "customers/9907217991/adGroups/181820804074"
NOMBRE = "Botas"
URL = "https://www.sudtec.cl/lista-productos/?yith_wcan=1&product_cat=botas"

KEYWORDS = [("botas bombero", "PHRASE"), ("botas de bomberos", "PHRASE"),
            ("botas para bomberos", "PHRASE"), ("botas incendio", "PHRASE"),
            ("botas seguridad incendio", "PHRASE"),
            ("botas para incendios forestales", "PHRASE"),
            ("botas jolly", "PHRASE"), ("botas lytos", "PHRASE"),
            ("botas blauer", "PHRASE")]

TITULARES = ["Botas para Bomberos", "Botas Lytos FR-1401 a 1406", "Botas Jolly y Blauer",
             "Botas Estructurales", "Botas Forestales", "Botas de Bomberos Sudtec",
             "Pide tu Cotización", "Cotiza sin Compromiso", "6 Modelos Lytos Disponibles",
             "Equipos de Emergencia", "Para Cuerpos de Bomberos", "Brigadas y Empresas",
             "Ver Catálogo de Botas", "Botas de Seguridad", "Sudtec South Pacific"]
DESCRIPCIONES = [
    "Botas para bomberos de las marcas Lytos, Jolly y Blauer. Pide tu cotización en línea.",
    "Seis modelos Lytos FR, más Jolly y Blauer. Elige el tuyo y solicita cotización.",
    "Equipamiento de emergencia para cuerpos de bomberos, brigadas y empresas en Chile.",
    "Revisa el catálogo de botas de Sudtec y pide una cotización sin compromiso."]


def maton(ruta, cuerpo=None):
    cmd = ["bash", os.path.join(WS, "bin", "maton.sh"), ruta]
    if cuerpo is not None:
        cmd += ["-X", "POST", "-H", "Content-Type: application/json",
                "-d", json.dumps(cuerpo, ensure_ascii=False)]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=180).stdout
    try:
        return json.loads(out)
    except Exception:
        return {"error": {"raw": out[:200]}}


def gaql(q):
    return maton("google-ads/v23/customers/%s/googleAds:search" % CID, {"query": q})


def es_quota(d):
    return "error" in d and "RESOURCE_EXHAUSTED" in json.dumps(d)


def limites_ok():
    malos = [h for h in TITULARES if len(h) > 30] + [d for d in DESCRIPCIONES if len(d) > 90]
    return not malos and len(TITULARES) == 15 and len(DESCRIPCIONES) == 4


def buscar_grupo():
    d = gaql("SELECT ad_group.resource_name, ad_group.name, ad_group.status FROM ad_group "
             "WHERE ad_group.name = '%s' AND ad_group.status != 'REMOVED'" % NOMBRE)
    if es_quota(d):
        return None, True
    for r in d.get("results", []):
        return r["adGroup"]["resourceName"], False
    return None, False


def main():
    if not limites_ok():
        print("ERROR | el texto del anuncio no cumple los limites de Google")
        return 3

    ag, sinq = buscar_grupo()
    if sinq:
        print("SIN-QUOTA | no pude consultar los grupos")
        return 2
    if ag:
        print("YA-EXISTE | el grupo '%s' ya esta creado (%s)" % (NOMBRE, ag))
        return 0

    # 1) grupo
    r = maton("google-ads/v23/customers/%s/adGroups:mutate" % CID,
              {"operations": [{"create": {"campaign": CAMP, "name": NOMBRE,
                                          "status": "ENABLED", "type": "SEARCH_STANDARD"}}]})
    if es_quota(r):
        print("SIN-QUOTA | no pude crear el grupo")
        return 2
    if "error" in r:
        print("ERROR | creando el grupo: %s" % json.dumps(r, ensure_ascii=False)[:250])
        return 3
    ag = r["results"][0]["resourceName"]

    # 2) keywords
    ops = [{"create": {"adGroup": ag, "status": "ENABLED",
                       "keyword": {"text": t, "matchType": m}}} for t, m in KEYWORDS]
    r2 = maton("google-ads/v23/customers/%s/adGroupCriteria:mutate" % CID, {"operations": ops})
    if "error" in r2:
        print("ERROR | grupo creado (%s) pero fallaron las keywords: %s"
              % (ag, json.dumps(r2, ensure_ascii=False)[:200]))
        return 3

    # 3) anuncio
    ad = {"finalUrls": [URL], "responsiveSearchAd": {
            "headlines": [{"text": h} for h in TITULARES],
            "descriptions": [{"text": d} for d in DESCRIPCIONES],
            "path1": "botas", "path2": "cotizacion"}}
    r3 = maton("google-ads/v23/customers/%s/adGroupAds:mutate" % CID,
               {"operations": [{"create": {"adGroup": ag, "status": "ENABLED", "ad": ad}}]})
    if "error" in r3:
        print("ERROR | grupo y keywords ok, fallo el anuncio: %s"
              % json.dumps(r3, ensure_ascii=False)[:250])
        return 3

    # 4) negativa 'botas' en General, para rutear el trafico al grupo nuevo
    r4 = maton("google-ads/v23/customers/%s/adGroupCriteria:mutate" % CID,
               {"operations": [{"create": {"adGroup": AG_GENERAL, "negative": True,
                                           "keyword": {"text": "botas", "matchType": "BROAD"}}}]})
    if "error" in r4:
        print("ERROR | todo creado, fallo la negativa en General: %s"
              % json.dumps(r4, ensure_ascii=False)[:200])
        return 3

    # 5) verificar
    d = gaql("SELECT ad_group.name, ad_group.status FROM ad_group "
             "WHERE ad_group.name = '%s' AND ad_group.status = 'ENABLED'" % NOMBRE)
    if not d.get("results"):
        print("ERROR | escribi todo pero no veo el grupo activo")
        return 3
    print("CREADO | grupo '%s' activo, %d keywords, 1 anuncio, negativa 'botas' en General. "
          "NINGUN presupuesto modificado." % (NOMBRE, len(KEYWORDS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
