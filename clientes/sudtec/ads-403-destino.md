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

## LA VERSIÓN DEFINITIVA (20-ago 09:50, con el `.htaccess` a la vista)

Connie mandó el `.htaccess` (msg 208). El bloque que importa:

    # === BLOQUEO DE BOTS AGRESIVOS ===
    RewriteCond %{HTTP_USER_AGENT} (Barkrowler|babbar|GPTBot|CCBot|ClaudeBot|anthropic-ai|
      Bytespider|PetalBot|SemrushBot|AhrefsBot|MJ12bot|DotBot|DataForSeoBot|ZoominfoBot|
      serpstatbot|BLEXBot) [NC]
    RewriteRule .* - [F,L]
    ...
    RewriteCond %{QUERY_STRING} (yith_wcan=|filter_|min_price=|max_price=) [NC]
    RewriteCond %{HTTP_USER_AGENT} !(Chrome|Firefox|Safari|Edg|OPR)/ [NC]
    RewriteRule .* - [F,L]

**Googlebot y AdsBot NO están en la lista de bots bloqueados.** Lo único que los
golpea es la última regla: **URL con parámetro de filtro + user-agent que no sea
navegador → 403**.

Puesto en fecha: el bloqueo se agregó la semana del 11-ago-2026 por un **ataque de
bots** que navegaban el sitio y saturaban procesos (Connie, msg 204). La regla de
los filtros ataca exactamente eso: la navegación facetada genera combinaciones
infinitas de URL y es lo que tumba el PHP.

**Conclusión: la causa era la del primer diagnóstico.** El anuncio apuntaba a
`?yith_wcan=1&product_cat=botas` → regla 4 → 403 → `DESTINATION_NOT_WORKING`.
Cambiar el destino a `/product-category/epp/botas/` **es el arreglo correcto**, y
ya está aplicado.

**El `.htaccess` no hay que tocarlo.** Está bien hecho. Que Google no crawlee URLs
de filtro es lo correcto también para SEO (presupuesto de rastreo, contenido
duplicado). Mejora opcional, no urgente: agregar `AdsBot-Google` a la excepción de
la regla 4, como red de seguridad por si un anuncio vuelve a apuntar a un filtro.

## Dos errores míos en este diagnóstico (para no repetirlos)

**1. Confundí caché con permiso.** Comparé URLs sin mirar `x-litespeed-cache`. Las
que daban 200 estaban **cacheadas** (LiteSpeed responde sin pasar por
`.htaccess`); la del filtro no. De ahí salió la primera tabla, que era correcta en
los números y equivocada en la causa.

**2. Contaminé mi propia prueba, y con eso alarmé de más.** Para forzar cache MISS
le agregué `?yith_wcan=1` a cada URL… que es **justo el parámetro que dispara la
regla**. Concluí que *todo el sitio* devolvía 403 a Googlebot y le avisé a Connie
que el SEO estaba en riesgo de desindexación. **Era falso.** Repetido con `?cb=`
(un parámetro que no está en la regla) y con `miss` confirmado en la cabecera,
home, lista, categorías y fichas dan **200** a Googlebot y AdsBot.

**La regla que queda:** el rompe-caché nunca debe contener el parámetro que se está
investigando. Y antes de avisar de una alarma grande —desindexación, pérdida de
tráfico— **verificarla con una prueba que no comparta variable con la hipótesis**.

## La señal que se dejó pasar el 19-ago

En la propuesta del grupo Botas quedó escrito, textual:

> *URL verificada; da 403 a `curl` por el firewall del sitio, 200 desde navegador.*

**Estaba visto y se descartó como inofensivo.** Ese 403 era exactamente lo que
después desaprobó el anuncio. La lección: **un 403 a `curl` con 200 en navegador
NO es cosmético cuando esa URL va a ser el destino de un anuncio** — para el
servidor, el robot de Google es un cliente tan "no navegador" como curl.

## La URL buena

    https://www.sudtec.cl/product-category/epp/botas/

- **200 al robot** y 200 en navegador, sin redirección
- Es la **canónica** (`/product-category/botas/` apunta ahí)
- Muestra las **8 botas**: Blauer CLASH, Jolly 9016/A y Lytos FR-1401…1406

Alternativa más angosta: `/product-category/botas-material-forestal/` (6, solo
Lytos). También 200 al robot.

Hay **dos categorías "Botas"** en Woo: id **280** slug `botas` (8 productos) e id
**302** slug `botas-material-forestal` (6).

## Estado — ✅ RESUELTO (aprobado el 20-ago 14:00)

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


## Los sitelinks: 9 más apuntando a URLs bloqueadas (hallazgo 20-ago 10:05)

Revisando la cuenta completa aparecieron **9 sitelinks** cuyo destino lleva
`yith_wcan=1` — el mismo patrón que la regla 4 del `.htaccess` bloquea:

| Categoría | Reemplazo verificado | Productos |
|---|---|---|
| uniformes | `/product-category/uniformes/` | 16 |
| rescate | `/product-category/rescate/` | 16 |
| epp | `/product-category/epp/` | 16 |
| camaras-termales-rescate | `/product-category/camaras-termales-rescate/` | 5 |
| linternas | `/product-category/linternas/` | 3 |
| material-mayor | `/product-category/material-mayor/` | 2 |

**Hoy figuran APPROVED** porque Google los revisó antes del bloqueo (semana del
11-ago). Pero los 6 destinos **dan 403 hoy** a AdsBot. Cuando Google los
re-revise, se caen igual que el anuncio de botas.

Los reemplazos están **verificados**: 200 a AdsBot sin caché y con productos.

**Estado: APLICADO el 20-ago-2026 11:08**, con OK de Connie (msg 232).

**Nota sobre el anuncio de botas:** al 20-ago 10:05 sigue `DISAPPROVED`, pero su
configuración está limpia — `finalUrls` es la nueva, y no hay URL móvil, plantilla
de seguimiento ni sufijo. Se asume veredicto viejo pendiente de re-revisión.
Verificado vía **Composio**, porque Maton estaba sin cuota
([[composio-respaldo-google-ads]]).


## Confirmación desde el panel de Google (20-ago 10:39, captura de Connie)

La ficha «Ver problemas con la política» del anuncio zanja el asunto:

- **URL final:** `https://www.sudtec.cl/product-category/epp/botas/` (la nueva, correcta)
- **Destino no operativo** · Plataforma: ordenador · Error de HTTP: **403**
- **URL ampliada:** `https://www.sudtec.cl/lista-productos/?yith_wcan=1&product_cat=botas`
  ← **la VIEJA**, o sea lo que Google probó
- **Última comprobación: 20 ago 2026, 7** ← **7:00**, y el cambio se aplicó a las **9:12**

**Conclusión: el veredicto es anterior al arreglo.** No hay nada más que tocar; se
cae solo cuando Google reejecute la comprobación de destino. Si sigue rechazado con
una comprobación **posterior a las 9:12**, ahí sí toca pedir revisión manual.

Dato operativo: **editar `finalUrls` dispara la revisión del anuncio, pero la
comprobación del destino corre por su cuenta** — `reviewStatus` volvió a `REVIEWED`
sin que el rastreador hubiera vuelto a la URL nueva. No confundir las dos cosas.

### «Sustancias no aprobadas» es un falso positivo, y no es del texto

Los **15 titulares y 4 descripciones** están **APPROVED uno por uno**
(`policySummaryInfo.approvalStatus`), y **ninguno contiene la palabra «product»**.

La evidencia que Google marca (`textList: ["product"]`) sale de la **URL**, que
contiene `product-category`. Google la cruza con su política de fármacos y
suplementos.

Es de tipo **LIMITED**, no PROHIBITED: **por sí sola no apaga el anuncio**. La que
lo apaga es `DESTINATION_NOT_WORKING`. No perseguirla ni reescribir el anuncio por
ella.


## Sitelinks — aplicado (20-ago-2026 11:08)

Los 9 se cambiaron con `GOOGLEADS_MUTATE_ASSETS` **por Composio** (Maton seguía sin
cuota), `update_mask: final_urls`, primero con `validate_only: true` y luego en
firme con `partial_failure: true`.

| id | Texto del enlace | Destino nuevo |
|---|---|---|
| 335606059860 | Cámara Termal | `/product-category/camaras-termales-rescate/` |
| 337464913368 | Cámaras Termales | `/product-category/camaras-termales-rescate/` |
| 337322119721 | Uniformes Bomberos | `/product-category/uniformes/` |
| 371724058864 | Herramientas de Rescate | `/product-category/rescate/` |
| 372779306605 | Herramientas Rescate | `/product-category/rescate/` |
| 371793951090 | EPP | `/product-category/epp/` |
| 372779306602 | EPP Bomberos | `/product-category/epp/` |
| 337464701931 | Linternas Bomberos | `/product-category/linternas/` |
| 337463806029 | Carros de Bomberos | `/product-category/material-mayor/` |

**Verificado releyendo los 22 sitelinks:** **cero** con `yith_wcan`. Y los **12
destinos de toda la cuenta** (incluidos los que no se tocaron) responden **200 a
AdsBot y a navegador**.

Al editarlos, los 9 vuelven a **revisión** de Google — esperado, y esta vez contra
la URL buena.

### Susto durante la verificación (vale recordarlo)

Justo después de la purga total de caché, `uniformes` y `camaras-termales-rescate`
devolvieron **500 a AdsBot**. Repetidas 8 veces cada una: **200 constante**. Era la
regeneración masiva posterior al purge. **No se aplicó nada hasta confirmarlo** y
hasta barrer las 15 rutas del sitio.

**Lección:** una purga total sobre este sitio provoca un pico de 500 transitorios.
Si hay que purgar y después verificar, dar un margen y repetir la medición antes de
concluir nada — y mejor purgar acotado que todo.

### Pendiente de criterio (no técnico)

**Carros de Bomberos** apunta a *Material Mayor*, que tiene **3 productos**. El
enlace funciona, pero promete más de lo que muestra. Planteado a Connie (msg 233)
para revisarlo a su vuelta; **no se tocó** porque es decisión suya.


## ✅ Cierre — 20-ago-2026 14:00

Google reejecutó la comprobación de destino, esta vez contra la URL nueva, y el
anuncio **quedó APPROVED**:

- `approvalStatus`: **APPROVED** · `reviewStatus`: REVIEWED
- `policyTopicEntries`: **vacío** — cayeron **las dos**, incluida
  `UNAPPROVED_SUBSTANCES`

**Confirma toda la cadena de diagnóstico:** el destino con `yith_wcan=1` daba 403
al robot por la regla del `.htaccess`, y el rechazo que Connie recibió a las 10:39
era el **veredicto viejo** (comprobación de las 07:00, anterior al cambio de las
09:12). Lo de «sustancias» era ruido asociado, no una infracción propia del texto.

**Tiempo real del ciclo:** cambio a las **09:12** → aprobado visto a las **14:00**.
Unas **5 horas**, no el día hábil que Google indica como referencia.

### Sitelinks, 3 horas después del cambio

De los 9 modificados: **6 APPROVED, 3 REVIEW_IN_PROGRESS, 0 rechazados.**

| Estado | Sitelinks |
|---|---|
| APPROVED | Uniformes Bomberos · Carros de Bomberos · Linternas Bomberos · Cámaras Termales · EPP Bomberos · Herramientas Rescate |
| En revisión | Cámara Termal · Herramientas de Rescate · EPP |

### Lo que queda

El grupo Botas sigue con **0 impresiones** — esperable, se aprobó recién. Si a la
pasada de las 19:00 sigue en cero, **ahí sí hay algo más que mirar** (puja,
keywords o presupuesto), no el destino.


## Por qué el grupo Botas marcó 0 impresiones el 20-ago (pregunta de Connie, msg 268)

Ella planteó que podía ser porque los **sitelinks** entraron en revisión al
cambiarles la URL. **Hay que separarlo:**

**Los sitelinks NO frenan el anuncio.** Son *assets*: si uno no está aprobado,
simplemente **no se muestra**; el anuncio sale igual, sin ese enlace. No apagan la
campaña.

**El anuncio sí, y explica casi todo.** Estuvo **DISAPPROVED desde antes de
medianoche hasta las 14:00**, y era el **único** del grupo. Un anuncio desaprobado
no sirve. **De las ~19 horas del día, en ~14 el grupo no podía mostrarse.**

Queda sin explicar solo la ventana **14:00–19:00**, y ahí caben dos hipótesis:

1. Un anuncio recién aprobado **tarda un rato** en entrar a subastas (normal)
2. Las keywords del grupo tienen la **puja demasiado baja** frente al grupo
   *General* y no ganan ninguna subasta

**La hipótesis 2 es la que se mide el 21-ago 07:00** con la consulta ya guardada.

⚠️ **Conclusión que importa para no leer mal los números:** el **20-ago no sirve
para juzgar el rendimiento del grupo Botas** — el anuncio estuvo caído casi todo el
día. **El primer día válido es el 21-ago.**


## 🕳️ El hueco de tráfico del 20-ago (pregunta de Connie, msg 270)

Preguntó si los grupos de *General* estaban andando. **Sí**, según la lectura de
las 19:00:

| Grupo | Impresiones | Clics |
|---|---|---|
| General | 91 | 13 |
| Improfor | 21 | 1 |
| **Botas** | **0** | 0 |
| **Total cuenta** | **112** | — |

*(días normales: 158–328 impresiones)*

**Pero la pregunta destapa el problema real del día:**

- El **19-ago** se puso **`botas` como negativa en el grupo General**, para rutear
  ese tráfico al grupo nuevo.
- El **20-ago**, General tenía las botas **bloqueadas** y el grupo Botas estaba
  **desaprobado hasta las 14:00**.

→ **El tráfico de botas se cayó por el hueco entre los dos. Nadie lo capturó.**

Y no es marginal: `botas bombero` traía históricamente **393 impresiones y 8
conversiones**. Es plausible que buena parte del bajón del día sea eso, y **no** un
problema general de la campaña.

### La red de seguridad ya está puesta

`bin/vigilancia_cambios.py` corre a diario: si el grupo Botas pasa **5 días**
(`DIAS_BOTAS`) sin una sola impresión, **quita la negativa de General
automáticamente** y devuelve el tráfico. Connie no tiene que hacer nada desde China.

Y por el parche del 20-ago en la mañana, **no cuenta los días en que el anuncio
estaba desaprobado** — sería castigar por una causa ya resuelta. Por eso el contador
sigue en **0** (`memory/estado/vigilancia_cambios.json`).

**Ese parche resultó ser justo lo que hacía falta:** sin él, el sistema habría
revertido el ruteo por un motivo equivocado; con él, la reversión solo se dispara si
el grupo no arranca **estando en condiciones de hacerlo**.
