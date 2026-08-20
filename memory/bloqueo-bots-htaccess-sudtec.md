---
name: bloqueo-bots-htaccess-sudtec
description: Sudtec bloqueó robots por .htaccess tras un ataque de bots; eso desaprobó un anuncio y deja a Googlebot en 403 en todo el sitio.
metadata:
  type: project
---

**La semana del 11-ago-2026 Sudtec puso un bloqueo de robots en el `.htaccess`**
porque el sitio estaba bajo un ataque de bots que saturaba procesos y lo tumbaba.
Connie lo contó el 20-ago (msg 204).

**Alcance real (verificado con el `.htaccess` a la vista):** el bloqueo golpea
**solo las URLs con parámetro de filtro** — `yith_wcan=`, `filter_`, `min_price=`,
`max_price=` — cuando el user-agent no es de navegador. **Googlebot y AdsBot NO
están** en la lista de bots bloqueados. El resto del sitio les responde 200.

Eso desaprobó un anuncio de Ads (`DESTINATION_NOT_WORKING`) porque su destino era
una URL de filtro. **No hay riesgo de desindexación**: llegué a decírselo a Connie
y era una alarma falsa, generada por mi propia prueba. Ver
[[ads-403-robot-vs-navegador]].

**La caché de LiteSpeed lo disimula:** si la página está cacheada, el robot recibe
200. Por eso parece intermitente y por eso me equivoqué de diagnóstico al
principio. Ver [[ads-403-robot-vs-navegador]].

**La regla está bien hecha y NO hay que tocarla.** Bloquea scrapers por nombre
(Semrush, Ahrefs, GPTBot, CCBot…) y protege las URLs de filtro, que es justo por
donde entraba el ataque: la navegación facetada genera combinaciones infinitas de
URL y satura el PHP. Que Google no crawlee URLs de filtro es además **correcto
para SEO**.

**Lo que sí se arregla es el anuncio**, no el sitio: su destino no debe ser una URL
de filtro. Ya se cambió a `/product-category/epp/botas/`.

**Mejora opcional, no urgente:** agregar `AdsBot-Google` a la excepción de la regla
de filtros, como red de seguridad por si algún anuncio vuelve a apuntar a un
filtro.

**Límite conocido:** esa regla filtra por user-agent, así que un bot que mienta y
declare `Chrome/` pasa igual. Si el ataque vuelve, lo que sirve es **rate limiting
por IP** o Cloudflare. No es urgente hoy.

Relacionado: [[ads-403-robot-vs-navegador]], [[cuota-google-ads]]
