---
name: ads-403-robot-vs-navegador
description: Cómo diagnosticar un destino de anuncio rechazado por 403 sin confundirse con la caché ni contaminar la prueba.
metadata:
  type: feedback
---

El 20-ago-2026, un anuncio de Sudtec cayó por `DESTINATION_NOT_WORKING` mientras
la página **se veía perfecta en el navegador**. Llegué a la causa, pero me
equivoqué dos veces en el camino. Las dos son evitables.

## 1. La caché tapa el problema

LiteSpeed responde **sin pasar por `.htaccess`**. Si la página está cacheada, el
robot recibe 200 aunque haya una regla que lo bloquea. Comparar URLs sin mirar la
caché lleva a culpar a la URL equivocada.

**Mirar siempre `x-litespeed-cache` en la respuesta** y forzar un MISS real antes
de concluir nada.

## 2. El rompe-caché no puede ser la variable investigada

Para forzar MISS usé `?yith_wcan=1`… que era **justo el parámetro que disparaba
el bloqueo**. Resultado: vi 403 en todas las páginas y le avisé a Connie que
Googlebot estaba bloqueado en **todo el sitio** y el SEO en riesgo de
desindexación. **Era falso** — lo generaba mi propia prueba.

**Regla:** el parámetro rompe-caché debe ser inocuo (`?cb=123`) y **no compartir
variable con la hipótesis**.

## 3. Antes de dar una alarma grande, verificarla aparte

«Desindexación», «pérdida de tráfico», «se cae la campaña» son alarmas que hacen
actuar a Connie. Antes de mandarlas, confirmarlas con una prueba que **no dependa
de la misma hipótesis**. Una alarma falsa cuesta credibilidad y la hace mover
cosas que están bien.

## 4. Un 403 a curl con 200 en navegador NO es cosmético

El 19-ago quedó anotado como detalle menor; al día siguiente fue lo que desaprobó
el anuncio. Para el servidor, **el robot de Google es un cliente tan "no
navegador" como curl**. Si esa URL va a ser destino de un anuncio, es bloqueante.

## Cómo probar bien

    # con user-agent de robot, cache-buster inocuo, y mirando la caché
    curl -sS -o /dev/null -D - -A 'AdsBot-Google (+http://www.google.com/adsbot.html)' \
      "https://sitio/pagina/?cb=$RANDOM" | grep -iE '^HTTP/|x-litespeed-cache'

Comparar contra un user-agent de navegador. Si difieren, es regla de servidor.

Relacionado: [[bloqueo-bots-htaccess-sudtec]], [[cuota-google-ads]]
