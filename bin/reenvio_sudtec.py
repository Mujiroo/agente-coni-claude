#!/usr/bin/env python3
"""
Reenvia a bd@sudtec.cl los correos NUEVOS que llegan de cg@sudtec.cl.

Por que existe: bd@sudtec.cl figura como destinatario directo en todos los
correos de cg@ desde marzo-2026, pero no le estan llegando. Este reenvio es un
PARCHE desde la casilla de Connie, no el arreglo de fondo (ese esta en el
servidor de correo de sudtec.cl).

Anti-duplicado: cada id de Gmail ya reenviado queda en el archivo de estado.
Sin eso, cada corrida reenviaria lo mismo otra vez.

Uso:
  python3 bin/reenvio_sudtec.py            # SIMULACION: muestra que haria, no envia
  python3 bin/reenvio_sudtec.py --enviar   # envia de verdad
"""
import base64, json, os, subprocess, sys, time
from email import message_from_bytes
from email.utils import formatdate

ORIGEN  = "cg@sudtec.cl"
DESTINO = "bd@sudtec.cl"
WS      = os.environ.get("AGENT_WORKSPACE", "/home/agent/workspace")
ESTADO  = os.path.join(WS, "memory", "estado", "reenvio_sudtec.json")
MATON   = os.path.join(WS, "bin", "maton.sh")
VENTANA = "newer_than:2d"   # margen: si estuve caido un dia, igual los alcanzo

# El original pasa por el relay de sudtec (MailChannels + ImunifyEmail) y llega
# cargado de cabeceras de ese trayecto, incluida una "X-MC-Relay: Junk". Arrastrarlas
# a un correo nuevo no sirve de nada y puede empeorar la entrega, asi que el reenvio
# se construye LIMPIO: solo el cuerpo y lo minimo para que se vea igual.
CONSERVAR = {"content-type", "content-transfer-encoding", "mime-version"}


def maton(ruta, *extra):
    r = subprocess.run(["bash", MATON, ruta, *extra], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError("maton fallo (%s): %s" % (r.returncode, r.stderr[:300]))
    try:
        return json.loads(r.stdout or "{}")
    except json.JSONDecodeError:
        raise RuntimeError("respuesta no-JSON de Maton: %s" % r.stdout[:300])


def cargar_estado():
    if os.path.exists(ESTADO):
        with open(ESTADO) as f:
            return json.load(f)
    return {"reenviados": [], "ultima_corrida": None, "arranque": None}


def guardar_estado(e):
    e["reenviados"] = e["reenviados"][-500:]   # no crece para siempre
    os.makedirs(os.path.dirname(ESTADO), exist_ok=True)
    with open(ESTADO, "w") as f:
        json.dump(e, f, indent=1, ensure_ascii=False)


def armar_reenvio(crudo, remitente):
    """Reconstruye el correo limpio hacia bd@, con el cuerpo original intacto."""
    orig = message_from_bytes(crudo)
    asunto = orig.get("Subject", "(sin asunto)")
    fecha  = orig.get("Date", "")
    de     = orig.get("From", ORIGEN)
    para   = orig.get("To", "")

    nuevo = message_from_bytes(crudo)
    for h in list(nuevo.keys()):
        if h.lower() not in CONSERVAR:
            del nuevo[h]
    nuevo["From"] = remitente
    nuevo["To"] = DESTINO
    nuevo["Subject"] = "RV: " + asunto
    nuevo["Reply-To"] = ORIGEN
    nuevo["Date"] = formatdate(localtime=True)
    # Rastro de que esto es un reenvio automatico y no un correo escrito a mano.
    nuevo["X-Reenviado-Por"] = "Kai (asistente de Constanza Pfeifer) - reenvio automatico"
    nuevo["X-Original-From"] = de
    nuevo["X-Original-To"] = para
    nuevo["X-Original-Date"] = fecha
    return nuevo, asunto, fecha


def main():
    enviar = "--enviar" in sys.argv
    est = cargar_estado()
    ya = set(est["reenviados"])

    perfil = maton("google-mail/gmail/v1/users/me/profile")
    remitente = perfil["emailAddress"]

    q = "from:%s %s" % (ORIGEN, VENTANA)
    lista = maton("google-mail/gmail/v1/users/me/messages?q=%s&maxResults=50"
                  % q.replace(":", "%3A").replace("@", "%40").replace(" ", "+"))
    msgs = lista.get("messages", []) or []

    # Primera corrida: NO se reenvia el historial, solo se marca lo que ya existe.
    # Si no, bd@ recibiria de golpe todo lo de la ventana.
    if est.get("arranque") is None:
        est["arranque"] = int(time.time())
        est["reenviados"] = [m["id"] for m in msgs]
        est["ultima_corrida"] = int(time.time())
        guardar_estado(est)
        print("Primera corrida: marco %d correos existentes como ya vistos. "
              "Desde ahora reenvio solo los nuevos." % len(msgs))
        return

    nuevos = [m for m in msgs if m["id"] not in ya]
    if not nuevos:
        est["ultima_corrida"] = int(time.time())
        guardar_estado(est)
        print("Sin correos nuevos de %s." % ORIGEN)
        return

    nuevos.reverse()   # del mas viejo al mas nuevo, para que lleguen en orden
    hechos = []
    for m in nuevos:
        det = maton("google-mail/gmail/v1/users/me/messages/%s?format=raw" % m["id"])
        crudo = base64.urlsafe_b64decode(det["raw"])
        nuevo, asunto, fecha = armar_reenvio(crudo, remitente)

        if not enviar:
            print("[SIMULACION] reenviaria  id=%s  %s  |  %s  ->  %s"
                  % (m["id"], fecha, asunto, DESTINO))
            continue

        payload = json.dumps({"raw": base64.urlsafe_b64encode(nuevo.as_bytes()).decode()})
        res = maton("google-mail/gmail/v1/users/me/messages/send",
                    "-X", "POST", "-H", "Content-Type: application/json", "-d", payload)
        if "id" not in res:
            print("ERROR al reenviar id=%s: %s" % (m["id"], json.dumps(res)[:300]), file=sys.stderr)
            continue
        hechos.append((m["id"], asunto, fecha))
        est["reenviados"].append(m["id"])
        guardar_estado(est)     # se guarda de a uno: si me corto, no duplico
        print("Reenviado  id=%s  ->  %s  |  %s" % (m["id"], DESTINO, asunto))

    est["ultima_corrida"] = int(time.time())
    guardar_estado(est)
    if enviar:
        print("TOTAL reenviados: %d" % len(hechos))


if __name__ == "__main__":
    main()
