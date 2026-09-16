#!/usr/bin/env bash
# Vigía del "YesStyle Glow Up Giveaway" (pedido por Connie 16-sep-2026, msg 1231).
# Solo lectura, sin login: la página pública muestra el MISMO estado que la app.
#
# La página tiene una <section ...cardView> que hoy dice "Coming Soon". Cuando el
# giveaway se abre, ahí aparecen los productos con su botón "Claim Now".
#
# Imprime una sola línea:
#   OK-SILENCIO   -> sigue en "Coming Soon", no hay nada que avisar
#   HAY-QUE-AVISAR-> el "Coming Soon" desaparecio: giveaway probablemente ABIERTO
#   SIN-DATO      -> no se pudo leer la pagina (red, WAF, rediseño). NO es noticia.
#
# El SIN-DATO es a proposito: si YesStyle bloquea o cambia el HTML, el vigía se
# calla en vez de inventar que el giveaway abrio. Un falso positivo aca la hace
# correr a una pagina vacia.
URL="https://www.yesstyle.com/en/glow-up-giveaway.html"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
ESTADO="$HOME/.claude/tgstate/vigia_yesstyle.estado"
mkdir -p "$(dirname "$ESTADO")"

tmp=$(mktemp); trap 'rm -f "$tmp"' EXIT
codigo=$(curl -s -m 40 -A "$UA" -w "%{http_code}" -o "$tmp" "$URL" 2>/dev/null)
bytes=$(wc -c < "$tmp")

# Tres guardas antes de opinar: respondio 200, vino la pagina entera, y es LA pagina.
if [ "$codigo" != "200" ] || [ "${bytes:-0}" -lt 100000 ] || ! grep -q "Glow Up Giveaway" "$tmp"; then
  echo "SIN-DATO (HTTP ${codigo:-000}, ${bytes:-0} bytes) — no se pudo leer la pagina, sin conclusiones"
  exit 0
fi

# El bloque que manda es el cardView, no cualquier "Coming Soon" suelto del HTML.
card=$(grep -o -E '__cardView">.{0,400}' "$tmp" | head -1)

if printf '%s' "$card" | grep -q "Coming Soon"; then
  echo "OK-SILENCIO (sigue en Coming Soon)"
  echo "cerrado" > "$ESTADO"
  exit 0
fi

previo=$(cat "$ESTADO" 2>/dev/null || echo "cerrado")
if [ "$previo" = "abierto" ]; then
  echo "OK-SILENCIO (ya abierto y ya avisado)"
  exit 0
fi
echo "abierto" > "$ESTADO"
echo "HAY-QUE-AVISAR"
echo "El 'Coming Soon' del Glow Up Giveaway desaparecio: probablemente ya se puede reclamar."
echo "Pagina: $URL"
echo "Extracto: $(printf '%s' "$card" | sed 's/<[^>]*>/ /g' | tr -s ' ' | cut -c1-220)"
