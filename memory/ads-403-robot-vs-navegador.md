# Una página puede dar 200 en navegador y 403 al robot de Google

Pasó en Sudtec el 20-ago-2026 y costó entender: un anuncio rechazado por
`DESTINATION_NOT_WORKING` mientras la página **se veía perfecta** en el navegador.

**Ojo con la caché: es la que hace mentir a la prueba.** El 20-ago llegué a una
conclusión equivocada (culpé a un parámetro de la URL) porque las páginas que
comparaba estaban **cacheadas** y respondían 200 a todos. Solo forzando un
**cache MISS** (parámetro aleatorio) aparece la verdad: el servidor devuelve
**403 a cualquier user-agent de robot** cuando la petición llega a PHP.

Así que la prueba correcta son **dos** cosas, no una: user-agent de robot **y**
URL que no esté en caché. Mirar siempre `x-litespeed-cache` en la respuesta.

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

3. **Un 403 a `curl` con 200 en navegador no es cosmético** si esa URL va a ser
   el destino de un anuncio. El 19-ago quedó anotado como detalle menor y al día
   siguiente fue lo que desaprobó el anuncio. Para el servidor, el robot de
   Google es un cliente tan "no navegador" como curl.

Y esto **no es solo de Ads**: si el servidor bloquea robots, **Googlebot recibe
lo mismo** y el daño es también de SEO.

Detalle completo en `clientes/sudtec/ads-403-destino.md`.
