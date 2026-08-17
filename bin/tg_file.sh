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
FP=$(curl -s --max-time 30 "https://api.telegram.org/bot${TOK}/getFile?file_id=${FID}" \
  | python3 -c 'import sys,json;print(json.load(sys.stdin).get("result",{}).get("file_path",""))')
[ -n "$FP" ] || { echo "ERROR: file_id invalido o expirado" >&2; exit 1; }
OUT="$DEST/$(basename "$FP")"
curl -s --max-time 180 -o "$OUT" "https://api.telegram.org/file/bot${TOK}/${FP}"
echo "$OUT"
