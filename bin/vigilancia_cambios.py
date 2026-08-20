#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vigila que los cambios del 19-ago-2026 en SUDTEC no empeoren la cuenta.

Connie viaja a China el 21-ago y no va a estar mirando. El 19-ago (msg 187) dio
autorizacion explicita: "si ves que las campanas empeoraron o no sirve, pausa los
cambios".

Los cambios vigilados:
  A. 'accesorios bomberos' en FRASE -> pausada
  B. negativas 'reloj' / 'relojes'
  C. grupo 'Botas' nuevo + negativa 'botas' en el grupo General

La linea base son SUS PROPIOS NUMEROS de los 30 dias previos al cambio, no
benchmarks de internet.

ECONOMIA DE CUOTA: una sola consulta por corrida. Ver [[cuota-google-ads]].

Salidas: OK-SILENCIO | HAY-QUE-AVISAR | REVERTIR-RUTEO | SIN-QUOTA
"""
import json, subprocess, sys, os, datetime

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "9907217991"
ESTADO = os.path.join(WS, "memory", "estado", "vigilancia_cambios.json")

# --- linea base: 30 dias previos al cambio (auditoria 17-ago + datos 19-ago) ---
BASE_CONV_DIA = 140 / 30.0        # 4,67 conversiones al dia
BASE_CPA = 1675                   # CLP por conversion
BASE_BOTAS_CONV_DIA = 8 / 30.0    # 0,27 al dia

# --- umbrales acordados (explicados a Connie el 19-ago) ---
CAIDA_CONV = 0.30      # baja de mas del 30% en conversiones/dia
SUBIDA_CPA = 1.50      # CPA por sobre 1,5x la base (= ~2.500 CLP)
DIAS_SEGUIDOS = 3      # tiene que sostenerse; un dia malo no significa nada
DIAS_BOTAS = 5         # margen para que el grupo nuevo arranque


def gaql(q):
    cmd = ["bash", os.path.join(WS, "bin", "maton.sh"),
           "google-ads/v23/customers/%s/googleAds:search" % CID,
           "-X", "POST", "-H", "Content-Type: application/json",
           "-d", json.dumps({"query": q})]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=150).stdout
    try:
        return json.loads(out)
    except Exception:
        return {"error": {"raw": out[:200]}}


def prev():
    if os.path.exists(ESTADO):
        try:
            return json.load(open(ESTADO))
        except Exception:
            pass
    return {"malos_seguidos": 0, "dias_botas_sin_nada": 0}


def main():
    # UNA sola consulta: metricas por grupo de anuncios de los ultimos 7 dias
    d = gaql("SELECT ad_group.name, campaign.name, metrics.impressions, metrics.clicks, "
             "metrics.conversions, metrics.cost_micros FROM ad_group "
             "WHERE segments.date DURING LAST_7_DAYS AND campaign.status = 'ENABLED'")
    if "error" in d:
        if "RESOURCE_EXHAUSTED" in json.dumps(d):
            print("SIN-QUOTA | no pude leer; reintento la proxima corrida")
            return 2
        print("HAY-QUE-AVISAR\n🔴 No pude leer la cuenta: %s" % json.dumps(d)[:180])
        return 1

    conv = cost = imp = 0.0
    botas_imp = botas_conv = 0.0
    for r in d.get("results", []):
        m = r.get("metrics", {})
        c = float(m.get("conversions", 0)); co = int(m.get("costMicros", 0)) / 1e6
        i = int(m.get("impressions", 0))
        conv += c; cost += co; imp += i
        if r["adGroup"]["name"].strip().lower() == "botas":
            botas_imp += i; botas_conv += c

    st = prev()
    alertas = []
    conv_dia = conv / 7.0
    cpa = (cost / conv) if conv else None

    # --- C: el grupo Botas no arranca y la negativa ya corto el trafico viejo ---
    if botas_imp == 0:
        st["dias_botas_sin_nada"] = st.get("dias_botas_sin_nada", 0) + 1
    else:
        st["dias_botas_sin_nada"] = 0

    # Antes de culpar al ruteo hay que descartar la otra causa de "0 impresiones":
    # que el anuncio del grupo este DESAPROBADO. Si lo esta, la negativa en General
    # no tiene nada que ver y quitarla seria revertir un cambio bueno por un
    # diagnostico equivocado (paso el 20-ago-2026: DESTINATION_NOT_WORKING por un
    # 403 que el sitio le devuelve al robot en la URL con 'yith_wcan=1').
    botas_desaprobado = None
    if st["dias_botas_sin_nada"] >= 1:
        da = gaql("SELECT ad_group_ad.ad.id, ad_group_ad.policy_summary.approval_status "
                  "FROM ad_group_ad WHERE ad_group.name = 'Botas' "
                  "AND ad_group_ad.status = 'ENABLED'")
        if "error" not in da:
            malos = [r["adGroupAd"] for r in da.get("results", [])
                     if r["adGroupAd"].get("policySummary", {})
                          .get("approvalStatus") == "DISAPPROVED"]
            vivos = [r for r in da.get("results", [])
                     if r["adGroupAd"].get("policySummary", {})
                          .get("approvalStatus") != "DISAPPROVED"]
            if malos and not vivos:
                botas_desaprobado = ", ".join(a["ad"]["id"] for a in malos)

    if botas_desaprobado:
        # No es el ruteo: no se revierte y no se acumula el contador.
        st["dias_botas_sin_nada"] = 0
        alertas.append(("🔴", "El grupo <b>Botas</b> sigue sin impresiones porque su "
                              "anuncio (<code>%s</code>) esta <b>DESAPROBADO</b>, no por el "
                              "ruteo. <b>No toco la negativa de General.</b> Hay que arreglar "
                              "el destino del anuncio y mandarlo a revision."
                              % botas_desaprobado))

    revertir = (not botas_desaprobado) and st["dias_botas_sin_nada"] >= DIAS_BOTAS
    if revertir:
        alertas.append(("🔴", "El grupo <b>Botas</b> lleva <b>%d días sin una sola "
                              "impresión</b>. La negativa en General ya está cortando esas "
                              "búsquedas, así que se están perdiendo. <b>Hay que quitar la "
                              "negativa.</b>" % st["dias_botas_sin_nada"]))

    # --- cuenta completa: conversiones y CPA contra su propia base ---
    malo = False
    if conv_dia < BASE_CONV_DIA * (1 - CAIDA_CONV):
        malo = True
    if cpa and cpa > BASE_CPA * SUBIDA_CPA:
        malo = True
    st["malos_seguidos"] = st.get("malos_seguidos", 0) + 1 if malo else 0

    if st["malos_seguidos"] >= DIAS_SEGUIDOS:
        alertas.append(("🔴", "La cuenta lleva <b>%d días seguidos</b> peor que antes de los "
                              "cambios: <b>%.1f</b> conversiones/día contra <b>%.1f</b> de "
                              "base, y CPA <b>%s</b> contra <b>%d</b>."
                        % (st["malos_seguidos"], conv_dia, BASE_CONV_DIA,
                           ("%.0f" % cpa) if cpa else "s/d", BASE_CPA)))

    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    st["revisado"] = datetime.date.today().isoformat()
    st["conv_dia"] = round(conv_dia, 2); st["cpa"] = round(cpa) if cpa else None
    st["botas_imp_7d"] = botas_imp
    json.dump(st, open(ESTADO, "w"), indent=1, ensure_ascii=False)

    if not alertas:
        print("OK-SILENCIO | conv/dia %.1f (base %.1f) | CPA %s (base %d) | botas imp 7d %d"
              % (conv_dia, BASE_CONV_DIA, ("%.0f" % cpa) if cpa else "s/d", BASE_CPA, botas_imp))
        return 0

    print("REVERTIR-RUTEO" if revertir else "HAY-QUE-AVISAR")
    for ic, t in alertas:
        print("%s %s" % (ic, t))
    print()
    print("contexto: 7 dias | conversiones %.1f | costo %.0f CLP | impresiones %d | "
          "grupo Botas: %d impresiones, %.1f conversiones"
          % (conv, cost, imp, botas_imp, botas_conv))
    return 1


if __name__ == "__main__":
    sys.exit(main())
