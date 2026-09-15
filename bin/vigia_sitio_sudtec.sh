#!/usr/bin/env bash
# Vigía de salud de www.sudtec.cl (15-sep-2026). Solo lectura.
# Mide una página SIN caché (pasa por PHP), que es lo que se cae cuando los bots saturan.
# Imprime OK-SILENCIO, o HAY-QUE-AVISAR tras 2 mediciones lentas seguidas (evita falsas alarmas).
ESTADO="$HOME/.claude/tgstate/vigia_sitio_sudtec.fallos"
UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Safari/604.1"
UMBRAL=15
r=$(curl -s -o /dev/null -m 40 -A "$UA" -w "%{http_code} %{time_total}" "https://www.sudtec.cl/?nc=$RANDOM$RANDOM" 2>/dev/null)
codigo=${r%% *}; tiempo=${r##* }
lento=$(awk -v t="${tiempo:-99}" -v u="$UMBRAL" 'BEGIN{print (t>u)?1:0}')
if [ "$codigo" != "200" ] || [ "$lento" = "1" ]; then
  n=$(( $(cat "$ESTADO" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$ESTADO"
  if [ "$n" -ge 2 ]; then
    echo "HAY-QUE-AVISAR"
    echo "sitio sin cache: HTTP ${codigo:-000} en ${tiempo:-?} s (umbral ${UMBRAL} s) | mediciones malas seguidas: $n"
  else
    echo "OK-SILENCIO (1 medicion mala: HTTP ${codigo:-000} ${tiempo:-?} s, espero la siguiente)"
  fi
else
  [ -s "$ESTADO" ] && [ "$(cat "$ESTADO")" -ge 2 ] && echo "RECUPERADO tras $(cat "$ESTADO") mediciones malas: HTTP $codigo en $tiempo s" || echo "OK-SILENCIO (HTTP $codigo en $tiempo s)"
  echo 0 > "$ESTADO"
fi
