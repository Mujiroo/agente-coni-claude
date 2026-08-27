#!/bin/bash
# Descarga un adjunto de Telegram por file_id.
# Uso: tg_file.sh <file_id> [dir_destino]
# Vars: TG_ENV_FILE (o AGENT_WORKSPACE/.env), TG_TOKEN_VAR (default TELEGRAM_BOT_TOKEN).
# No depende de ninguna API externa: solo el token del propio agente.
set -euo pipefail
FID="${1:?falta el file_id}"
SELFDIR="$(cd "$(dirname "$0")" && pwd)"
WS="${AGENT_WORKSPACE:-$(cd "$SELFDIR/.." && pwd)}"
ENV_FILE="${TG_ENV_FILE:-$WS/.env}"
DEST="${2:-${TG_DOWNLOAD_DIR:-$WS/incoming}}"
mkdir -p "$DEST"
TOKVAR="${TG_TOKEN_VAR:-TELEGRAM_BOT_TOKEN}"
TOK=$(grep -m1 "^${TOKVAR}=" "$ENV_FILE" | cut -d= -f2- | sed 's/[[:space:]]*#.*$//' | tr -d '"'"'"' \r')
[ -n "$TOK" ] || { echo "ERROR: sin token ($TOKVAR) en $ENV_FILE" >&2; exit 1; }
# getFile a veces se cuelga aunque el resto de la API responda (paso el 25-ago-2026:
# getMe al instante y getFile timeout una y otra vez, con file_id validos). Antes eso
# reventaba con un traceback de Python sobre respuesta vacia y parecia "file_id expirado",
# que es un diagnostico equivocado y manda a buscar por el lado que no es.
# 27-ago-2026: con 30s se rendia y una llamada identica a 45s SI respondia, en plena
# emergencia (Connie en la estacion de tren). getFile puede tardar >30s y responder bien:
# se sube el techo a 60s y se reintenta 3 veces antes de declarar caida la API.
RESP=""
for INTENTO in 1 2 3; do
  RESP=$(curl -s --max-time 60 "https://api.telegram.org/bot${TOK}/getFile?file_id=${FID}" || true)
  [ -n "$RESP" ] && break
  [ "$INTENTO" -lt 3 ] && sleep 3
done
if [ -z "$RESP" ]; then
  echo "ERROR-RED: getFile no respondio tras 3 intentos de 60s. La API puede estar caida solo para archivos; reintenta en unos minutos." >&2
  exit 2
fi
FP=$(printf '%s' "$RESP" | python3 -c 'import sys,json
try:
    print(json.load(sys.stdin).get("result",{}).get("file_path",""))
except Exception:
    print("")')
[ -n "$FP" ] || { echo "ERROR: file_id invalido o expirado -- respuesta: $(printf '%s' "$RESP" | head -c 200)" >&2; exit 1; }
OUT="$DEST/$(basename "$FP")"
curl -s --max-time 180 -o "$OUT" "https://api.telegram.org/file/bot${TOK}/${FP}"
echo "$OUT"
