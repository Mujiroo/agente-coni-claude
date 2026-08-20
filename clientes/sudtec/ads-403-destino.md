# Sudtec Ads — el 403 que desaprobó el grupo Botas (20-ago-2026)

## Qué pasó

El único anuncio del grupo **Botas** (`821602063409`, Campaña Sudtec
`22490713380`) quedó **DISAPPROVED** y el grupo nunca arrancó: **0 impresiones y
$0 en 7 días**. Google mandó el correo de rechazo a Connie el 20-ago 09:05.

Dos políticas en el rechazo, y **solo una bloquea**:

- `DESTINATION_NOT_WORKING` — tipo **PROHIBITED**. Esta es la que apaga el anuncio.
- `UNAPPROVED_SUBSTANCES` («el texto contiene: product») — tipo **LIMITED**.
  Falso positivo con la palabra `product`. No frena nada; no perseguirla.

## La causa real (esto es lo que no se ve mirando el sitio)

La URL del anuncio era:

    https://www.sudtec.cl/lista-productos/?yith_wcan=1&product_cat=botas

**En navegador da 200; al robot le da 403.** Por eso el sitio "se ve bien" y el
anuncio igual está rechazado.

Lo que dispara el 403 es el parámetro **`yith_wcan=1`**, no `product_cat`:

| URL | navegador | AdsBot |
|---|---|---|
| `/lista-productos/` | 200 | 200 |
| `/lista-productos/?foo=1` | 200 | 200 |
| `/lista-productos/?product_cat=botas` | 200 | **200** |
| `/lista-productos/?yith_wcan=1` | 200 | **403** |
| `/lista-productos/?yith_wcan=1&product_cat=botas` | 200 | **403** |

Tampoco es cosa del user-agent solamente: con `curl/8.0` y sin user-agent
también da 403. La regla parece ser *`yith_wcan=1` + cliente que no es un
navegador reconocido* → 403 (protección anti-scraping sobre el filtro YITH).

## La trampa: quitar el parámetro NO sirve

`?product_cat=botas` **se ignora**: devuelve los **28** productos de la lista sin
filtrar (alzaprimas, VETTER Magnaseal…), no las botas. El filtro real lo activa
`yith_wcan=1`. Si alguien "arregla" el 403 borrando ese parámetro, el anuncio
queda apuntando a una lista mezclada.

`/categoria-producto/botas/` tampoco sirve: **redirige a un producto suelto**
(Bota Blauer CLASH), no es una categoría.

## CORRECCIÓN (20-ago 09:35) — la causa NO era el parámetro

Todo lo de arriba **quedó desmentido**: el anuncio se volvió a rechazar con la
URL nueva. La tabla de 403/200 estaba **confundida por la caché de LiteSpeed**.

Lo que pasa de verdad:

- Petición que llega a **PHP** (cache **MISS**) → **403 a cualquier robot**
- Petición servida desde **caché** (`x-litespeed-cache: hit`) → **200 a todos**

Las páginas que parecían "buenas" (`/lista-productos/`, home, la categoría)
estaban simplemente **cacheadas**. La del filtro no lo estaba. De ahí la falsa
conclusión de que el culpable era `yith_wcan=1`.

**Prueba decisiva** (URL con parámetro aleatorio, siempre MISS):

| User-agent | Resultado |
|---|---|
| Chrome escritorio / Safari iPhone | **200** |
| `Mozilla/...` inventado sin «bot» | **200** |
| Googlebot · AdsBot-Google · Bingbot | **403** |
| `curl/8.0` · sin user-agent · `bot` | **403** |
| `Mozilla/5.0 (compatible; MiCosaBot/1.0)` | **403** |

O sea: **la regla bloquea por user-agent de robot**, y solo se nota cuando la
caché no tapa el golpe.

### Consecuencias

1. **El anuncio va a seguir cayéndose.** Si Google revisa con la caché vencida,
   ve un 403. Cambiar la URL no lo arregla: es cuestión de suerte de caché.
2. **También afecta al SEO.** Googlebot recibe el mismo 403 — y Connie vive del
   SEO, así que esto le importa por partida doble.

### Dónde está el bloqueo

**No es de WordPress.** Los 18 plugins activos no incluyen ninguno de seguridad
(no hay Wordfence, Sucuri ni similar). El 403 es una página genérica de
**LiteSpeed**, sin ID de incidente: es del **servidor / hosting**.

**Lo que hay que pedir:** que el hosting deje pasar a **Googlebot** y
**AdsBot-Google** (y de paso Bingbot). Ni Connie ni yo lo podemos tocar.

## La señal que se dejó pasar el 19-ago

En la propuesta del grupo Botas quedó escrito, textual:

> *URL verificada; da 403 a `curl` por el firewall del sitio, 200 desde navegador.*

**Estaba visto y se descartó como inofensivo.** Ese 403 era exactamente lo que
después desaprobó el anuncio. La lección: **un 403 a `curl` con 200 en navegador
NO es un detalle cosmético cuando esa URL va a ser el destino de un anuncio** —
el robot de Google es, para el servidor, un cliente tan "no navegador" como curl.

## La URL buena

    https://www.sudtec.cl/product-category/epp/botas/

- **200 al robot** y 200 en navegador, sin redirección
- Es la **canónica** (`/product-category/botas/` apunta ahí)
- Muestra las **8 botas**: Blauer CLASH, Jolly 9016/A y Lytos FR-1401…1406

Alternativa más angosta: `/product-category/botas-material-forestal/` (6, solo
Lytos). También 200 al robot.

Hay **dos categorías "Botas"** en Woo: id **280** slug `botas` (8 productos) e id
**302** slug `botas-material-forestal` (6).

## Estado — NO resuelto (la URL se cambió igual, pero no era la causa)

Connie dio el OK (msg 199) y se aplicó el cambio con `ads:mutate`
(`updateMask=finalUrls`) sobre el ad `821602063409`.

Después del cambio, verificado contra la API:

- destino: `https://www.sudtec.cl/product-category/epp/botas/`
- `status`: ENABLED · `reviewStatus`: **REVIEW_IN_PROGRESS**
- `policyTopicEntries`: **vacío** — se cayeron las dos políticas

Editar el `finalUrls` **reenvía el anuncio a revisión solo**, no hay que pedirla
aparte. Queda un cron de seguimiento para el 21-ago 10:00 que le confirma a
Connie cómo quedó y se borra a sí mismo.

## Regla que quedó en el código

`bin/vigilancia_cambios.py` revertía el ruteo (quitar la negativa `botas` de
General) si el grupo Botas pasaba `DIAS_BOTAS=5` sin impresiones. Ese
razonamiento era incompleto: **"0 impresiones" también puede ser un anuncio
desaprobado**, y en ese caso quitar la negativa revierte un cambio bueno por un
diagnóstico equivocado.

Ahora el script consulta el `approval_status` del anuncio antes de culpar al
ruteo: si está DESAPROBADO, **no revierte, no acumula el contador** y avisa que
lo que hay que arreglar es el destino.


## Keywords del grupo Botas — volumen sin verificar (pregunta de Connie, msg 201)

Ella preguntó si se verificó que las keywords tuvieran búsquedas. Respuesta
honesta: **se verificó el catálogo, no el volumen**.

- ✅ Verificado: que cada keyword calce con producto real (por eso se descartó
  `botas de bomberos rosadas`).
- ✅ Con datos propios: `botas bombero` → 393 impresiones, 8 conversiones, CPA 1.970.
- ❌ **Sin verificar en el Planificador:** `botas lytos` y `botas blauer`, las dos
  **nuevas**. Son marcas de nicho en Chile y bien pueden tener volumen ~0.

Matiz que importa: volumen cero **no gasta**, pero **en concordancia amplia sí**,
porque pesca tráfico suelto. Para nombres de marca va **exacta o de frase**.

Queda cron el **21-ago 04:00** que trae el volumen real y el estado del anuncio
en **una sola pasada batcheada** (la cuota se agotó el 20-ago).
