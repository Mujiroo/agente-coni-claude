---
name: bloqueo-bots-htaccess-sudtec
description: Sudtec bloqueó robots por .htaccess tras un ataque de bots; eso desaprobó un anuncio y deja a Googlebot en 403 en todo el sitio.
metadata:
  type: project
---

**La semana del 11-ago-2026 Sudtec puso un bloqueo de robots en el `.htaccess`**
porque el sitio estaba bajo un ataque de bots que saturaba procesos y lo tumbaba.
Connie lo contó el 20-ago (msg 204).

**Efecto colateral:** todo el sitio devuelve **403 a Googlebot y AdsBot** cuando
la petición llega a PHP. Desaprobó un anuncio de Ads por
`DESTINATION_NOT_WORKING`, y deja el **SEO en riesgo de desindexación**.

**La caché de LiteSpeed lo disimula:** si la página está cacheada, el robot recibe
200. Por eso parece intermitente y por eso me equivoqué de diagnóstico al
principio. Ver [[ads-403-robot-vs-navegador]].

**El defecto de la regla, y el argumento para cambiarla:** filtra por
**user-agent**, que es lo que el visitante *dice* ser. Probado: `curl` con un UA
de Chrome inventado **pasa con 200**. Así que la regla no detiene a los atacantes
(les basta mentir) y sí detiene a Google y Bing, que se identifican honestamente.

**Lo pedido:** excepción para `Googlebot|AdsBot-Google|Google-InspectionTool|Storebot-Google|bingbot`
antes de la regla de bloqueo; y de fondo, rate limiting por IP o Cloudflare, que
verifica robots de verdad.

**Estado al 20-ago-2026:** esperando que Connie consiga el bloque actual del
`.htaccess` para devolver el parche exacto. **No tengo acceso a archivos del
servidor** — esto se cambia con quien administra el hosting.

Relacionado: [[ads-403-robot-vs-navegador]], [[cuota-google-ads]]
