#!/usr/bin/env bash
# Vigía del "YesStyle Glow Up Giveaway" (pedido por Connie 16-sep-2026, msg 1231).
# Solo lectura, sin login: la página pública muestra el MISMO estado que la app.
#
# Imprime:
#   OK-SILENCIO   -> cerrado ("Coming Soon"), o ya abierto y ya avisado
#   HAY-QUE-AVISAR-> giveaway ABIERTO, con producto, fechas y stock
#   SIN-DATO      -> no se pudo leer la pagina, o el HTML ya no calza. NO es noticia.
#
# COMO SE RECONOCE EL ESTADO (corregido el 16-sep tras el primer disparo real):
#   cerrado -> <section ...__cardView><h3>Coming Soon</h3>
#   abierto -> ese cardView DESAPARECE y salen __freeClaimsContent / __productInfo
#              con el producto, el rango de fechas, el % reclamado y el tope de unidades.
#
# La version anterior daba "abierto" por la simple AUSENCIA del "Coming Soon". Acerto,
# pero por el motivo equivocado: si la pagina hubiera cargado a medias habria gritado
# igual. Ahora se exige EVIDENCIA POSITIVA de apertura, asi que un render parcial cae
# en SIN-DATO y se calla.
URL="https://www.yesstyle.com/en/glow-up-giveaway.html"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
ESTADO="$HOME/.claude/tgstate/vigia_yesstyle.estado"
mkdir -p "$(dirname "$ESTADO")"

tmp=$(mktemp); trap 'rm -f "$tmp"' EXIT
if [ -n "$FAKE" ]; then cp "$FAKE" "$tmp"; codigo=200; else
  codigo=$(curl -s -m 40 -A "$UA" -w "%{http_code}" -o "$tmp" "$URL" 2>/dev/null); fi
bytes=$(wc -c < "$tmp")

if [ "$codigo" != "200" ] || [ "${bytes:-0}" -lt 100000 ] || ! grep -q "Glow Up Giveaway" "$tmp"; then
  echo "SIN-DATO (HTTP ${codigo:-000}, ${bytes:-0} bytes) — no se pudo leer la pagina, sin conclusiones"
  exit 0
fi

# 1) Cerrado: el cardView con su "Coming Soon".
if grep -o -E '__cardView">.{0,400}' "$tmp" | head -1 | grep -q "Coming Soon"; then
  echo "OK-SILENCIO (sigue en Coming Soon)"
  echo "cerrado" > "$ESTADO"; exit 0
fi

# 2) Abierto: tiene que haber bloque de producto. Sin el, NO se opina.
bloque=$(grep -o -E '__freeClaimsContent.{0,1500}' "$tmp" | head -1)
if [ -z "$bloque" ]; then
  echo "SIN-DATO (no esta el 'Coming Soon' pero tampoco el bloque de producto: el HTML cambio)"
  exit 0
fi

texto=$(printf '%s' "$bloque" | sed 's/<[^>]*>/ | /g' | sed "s/&#x27;/'/g; s/&amp;/\&/g" | tr -s ' |' ' |')
fechas=$(printf '%s' "$texto"  | grep -o -E '[A-Z]{3,5}\. ?[0-9]{1,2} ?- ?[A-Z]{3,5}\. ?[0-9]{1,2}' | head -1)
claimed=$(printf '%s' "$texto" | grep -o -E '[0-9]+% claimed' | head -1)
limite=$(printf '%s' "$texto"  | grep -o -E 'Limited to [0-9,]+ items' | head -1)
# El nombre viene partido en trozos ("I'm from" y "Propolis Glazed Serum"). Se pegan
# los trozos de texto util y se descartan los de markup, fechas y contadores.
producto=$(printf '%s' "$texto" | awk -F'\\|' '{
  for(i=1;i<=NF;i++){
    t=$i; gsub(/^ +| +$/,"",t)
    if (t=="" || t=="-" || length(t)<3) continue
    if (t ~ /claimed|Limited to|__|class=|<|>|MuiButton/) continue
    if (t ~ /^[A-Z][A-Z][A-Z]+\. *[0-9]/) continue   # rango de fechas, ya va aparte
    printf "%s ", t
  }}' | sed 's/ *$//' | cut -c1-90)

previo=$(cat "$ESTADO" 2>/dev/null || echo "cerrado")
if [ "$previo" = "abierto" ]; then
  echo "OK-SILENCIO (ya abierto y ya avisado) | ${producto:-?} | ${claimed:-?}"
  exit 0
fi
echo "abierto" > "$ESTADO"
echo "HAY-QUE-AVISAR"
echo "El Glow Up Giveaway esta ABIERTO."
echo "Producto : ${producto:-(no se pudo leer)}"
echo "Fechas   : ${fechas:-?}"
echo "Avance   : ${claimed:-?} · ${limite:-?}"
echo "Pagina   : $URL"
