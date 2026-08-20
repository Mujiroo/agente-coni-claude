# Una página puede dar 200 en navegador y 403 al robot de Google

Pasó en Sudtec el 20-ago-2026 y costó entender: un anuncio rechazado por
`DESTINATION_NOT_WORKING` mientras la página **se veía perfecta** en el navegador.

**Al diagnosticar un destino rechazado, probar SIEMPRE con user-agent de robot**,
no solo abriendo la página:

    curl -s -o /dev/null -w '%{http_code}' -L \
      -A 'AdsBot-Google (+http://www.google.com/adsbot.html)' "$URL"

Y comparar contra un user-agent de navegador. Si difieren, el problema es una
regla de seguridad del hosting/WAF, no el contenido.

Dos cosas más que se aprendieron ahí:

1. **Aislar qué parte de la URL lo dispara**, parámetro por parámetro. En Sudtec
   era `yith_wcan=1` (filtro YITH), no la categoría.
2. **Verificar que la URL de reemplazo muestre lo mismo.** El reemplazo obvio
   (quitar el parámetro) devolvía la lista sin filtrar y nadie lo habría notado
   hasta ver el gasto. Contar productos, no suponer.

Detalle completo en `clientes/sudtec/ads-403-destino.md`.
