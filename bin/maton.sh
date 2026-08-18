#!/bin/bash
# Helper de Maton (maton.ai) — proxy REST a las APIs nativas de Google con la
# cuenta de Constanza (pfeifer.constanza@gmail.com).
#
#   bash bin/maton.sh conexiones
#   bash bin/maton.sh google-mail/gmail/v1/users/me/profile
#   bash bin/maton.sh 'google-calendar/calendar/v3/calendars/primary/events?maxResults=5'
#   bash bin/maton.sh google-sheets/v4/spreadsheets/<id> -X POST -d '{...}'
#
# Cualquier opcion extra se pasa tal cual a curl (para POST/PATCH/DELETE).
set -u
BASE="https://api.maton.ai"

KEY="${MATON_API_KEY:-}"
if [ -z "$KEY" ]; then
  ENVF="${TG_ENV_FILE:-${AGENT_WORKSPACE:-/home/agent/workspace}/.env}"
  KEY=$(grep -m1 '^MATON_API_KEY=' "$ENVF" 2>/dev/null | cut -d= -f2- | tr -d '"'"'"' \r')
fi
[ -n "$KEY" ] || { echo "ERROR: no encuentro MATON_API_KEY ni en el entorno ni en el .env" >&2; exit 1; }

if [ "${1:-}" = "conexiones" ]; then
  # OJO: el listado de conexiones vive en ctrl.maton.ai, NO en api.maton.ai
  curl -sS --max-time 60 -H "Authorization: Bearer $KEY" https://ctrl.maton.ai/connections
  echo
  exit 0
fi

RUTA="${1:?uso: maton.sh <ruta> [opciones de curl]  |  maton.sh conexiones}"
shift
curl -sS --max-time 90 -H "Authorization: Bearer $KEY" "$BASE/${RUTA#/}" "$@"
echo
