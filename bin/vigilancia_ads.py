#!/usr/bin/env python3
"""
Vigilancia diaria de la cuenta Google Ads de SUDTEC mientras Connie viaja.

Regla de oro: CALLA cuando todo va bien, GRITA cuando algo se rompe. Un aviso
diario de "todo ok" se vuelve ruido y se deja de leer; lo que ella pidio es
enterarse ANTES que el cliente si algo se cae.

Vigila cinco cosas:
  1. La campana dejo de estar activa
  2. Gasto de ayer en cero (o casi) -> algo la freno
  3. Proyeccion del mes por sobre los 300.000 del cliente
  4. Las solicitudes REALES (correos de cg@) se desplomaron
  5. Alguien cambio el presupuesto por fuera

Uso:
  python3 bin/vigilancia_ads.py           # revisa y decide si hay que avisar
  python3 bin/vigilancia_ads.py --forzar  # imprime el estado aunque este todo bien
"""
import json, os, subprocess, sys, datetime, collections

WS      = os.environ.get("AGENT_WORKSPACE", "/home/agent/workspace")
MATON   = os.path.join(WS, "bin", "maton.sh")
ESTADO  = os.path.join(WS, "memory", "estado", "vigilancia_ads.json")
CID     = "9907217991"
LIMITE  = 300000          # CLP/mes, tope duro del cliente
ORIGEN  = "cg@sudtec.cl"


def maton(ruta, *extra):
    r = subprocess.run(["bash", MATON, ruta, *extra], capture_output=True, text=True, timeout=120)
    return json.loads(r.stdout or "{}")


def gaql(q):
    return maton("google-ads/v23/customers/%s/googleAds:search" % CID,
                 "-X", "POST", "-H", "Content-Type: application/json",
                 "-d", json.dumps({"query": q}))


def estado_previo():
    if os.path.exists(ESTADO):
        return json.load(open(ESTADO))
    return {}


def main():
    forzar = "--forzar" in sys.argv
    prev = estado_previo()
    alertas, notas = [], []

    hoy = datetime.date.today()
    ayer = hoy - datetime.timedelta(days=1)

    # ---- campanas activas y su presupuesto ----
    d = gaql("SELECT campaign.name, campaign.status, campaign_budget.amount_micros "
             "FROM campaign WHERE campaign.status != 'REMOVED'")
    if "error" in d:
        # Un fallo de lectura NO se puede tragar en silencio: sin datos no se
        # puede afirmar que todo va bien.
        alertas.append(("🔴", "No pude leer la cuenta de Google Ads: %s"
                        % json.dumps(d)[:200]))
        d = {}

    presu = {}
    activas = []
    for r in d.get("results", []):
        n = r["campaign"]["name"]
        presu[n] = int(r.get("campaignBudget", {}).get("amountMicros", 0)) // 1000000
        if r["campaign"]["status"] == "ENABLED":
            activas.append(n)

    if presu and "Campaña Sudtec" not in activas:
        alertas.append(("🔴", "<b>La campaña principal NO está activa.</b> "
                              "Dejó de mostrarse; no van a entrar cotizaciones."))

    # ---- alguien movio el presupuesto por fuera ----
    if prev.get("presupuestos"):
        for n, v in presu.items():
            ant = prev["presupuestos"].get(n)
            if ant is not None and ant != v:
                alertas.append(("⚠️", "El presupuesto de <b>%s</b> cambió de "
                                      "<b>%s</b> a <b>%s</b> CLP/día, y no fui yo. "
                                      "Alguien lo tocó por fuera." % (n, ant, v)))
    total_dia = sum(presu.get(n, 0) for n in activas)
    if total_dia * 30.4 > LIMITE:
        alertas.append(("🔴", "Los topes suman <b>%.0f</b> CLP/mes y el límite del "
                              "cliente son <b>%s</b>." % (total_dia * 30.4, LIMITE)))

    # ---- gasto de ayer ----
    d2 = gaql("SELECT metrics.cost_micros, metrics.conversions FROM customer "
              "WHERE segments.date = '%s'" % ayer.isoformat())
    gasto_ayer = sum(int(r["metrics"].get("costMicros", 0)) for r in d2.get("results", [])) // 1000000
    conv_ayer = sum(float(r["metrics"].get("conversions", 0)) for r in d2.get("results", []))
    if presu and gasto_ayer < total_dia * 0.25:
        alertas.append(("🔴", "Ayer (%s) se gastaron solo <b>%s CLP</b> de %s "
                              "presupuestados. Algo frenó la campaña."
                        % (ayer.strftime("%d-%b"), gasto_ayer, total_dia)))

    # ---- proyeccion del mes ----
    ini = hoy.replace(day=1)
    d3 = gaql("SELECT segments.date, metrics.cost_micros FROM customer "
              "WHERE segments.date BETWEEN '%s' AND '%s'" % (ini.isoformat(), hoy.isoformat()))
    mtd = sum(int(r["metrics"].get("costMicros", 0)) for r in d3.get("results", [])) // 1000000
    prox = (datetime.date(hoy.year + (hoy.month == 12), hoy.month % 12 + 1, 1))
    dias_mes = (prox - ini).days
    restantes = dias_mes - hoy.day
    proyeccion = mtd + restantes * total_dia
    if proyeccion > LIMITE:
        alertas.append(("🔴", "<b>Se va a pasar del presupuesto.</b> Llevas <b>%s</b> "
                              "en el mes y al ritmo actual cierra en <b>%s</b> "
                              "(límite %s)." % (mtd, proyeccion, LIMITE)))

    # ---- solicitudes REALES: los correos de cg@ ----
    def correos(dias):
        r = maton("google-mail/gmail/v1/users/me/messages?q=from%%3Acg%%40sudtec.cl"
                  "+newer_than%%3A%dd&maxResults=200" % dias)
        return len(r.get("messages", []) or [])
    c3, c14 = correos(3), correos(14)
    base3 = (c14 / 14.0) * 3 if c14 else 0
    if base3 >= 3 and c3 <= base3 * 0.4:
        alertas.append(("⚠️", "<b>Cayeron las solicitudes.</b> En 3 días llegaron "
                              "<b>%d</b> cotizaciones; lo normal para ese lapso son "
                              "<b>%.1f</b>." % (c3, base3)))

    # ---- se guarda el estado para comparar manzana con manzana la proxima vez ----
    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    json.dump({"presupuestos": presu, "revisado": hoy.isoformat(),
               "gasto_ayer": gasto_ayer, "mtd": mtd, "correos_3d": c3},
              open(ESTADO, "w"), indent=1, ensure_ascii=False)

    if not alertas and not forzar:
        print("OK-SILENCIO | gasto ayer %s | mes %s | proyeccion %s | conv ayer %.0f | "
              "cotizaciones 3d %d" % (gasto_ayer, mtd, proyeccion, conv_ayer, c3))
        return

    print("HAY-QUE-AVISAR" if alertas else "OK (forzado)")
    for icono, t in alertas:
        print("%s %s" % (icono, t))
    print()
    print("contexto: gasto ayer %s CLP | mes %s CLP | proyeccion cierre %s CLP | "
          "limite %s | cotizaciones ultimos 3 dias %d (14 dias: %d)"
          % (gasto_ayer, mtd, proyeccion, LIMITE, c3, c14))


if __name__ == "__main__":
    main()
