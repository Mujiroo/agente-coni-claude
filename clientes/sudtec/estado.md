# SUDTEC — reenvío de cotizaciones cg@ → bd@

*Abierto: 17-ago-2026, a pedido de Connie.*

## Lo que ella pidió

Reenviar a `bd@sudtec.cl` los correos que llegan de `cg@sudtec.cl`, porque bd@
«no está recibiendo las cotizaciones». Solo los nuevos, nunca dos veces.

## Lo que encontré al revisar (importante)

**`bd@sudtec.cl` ya viene como destinatario directo en TODOS los correos de
`cg@`**, sin excepción, desde por lo menos el **3 de marzo de 2026**. El `To:` es
siempre el mismo:

```
c.montilla@south-pacific.cl, bd@sudtec.cl, pfeifer.constanza@gmail.com
```

O sea: **cg@ sí le está escribiendo a bd@**. Lo que falla es la entrega o el
filtrado del lado de la casilla `bd@sudtec.cl`. El reenvío es un **parche**, no
el arreglo.

Pista sobre la causa: el original sale por el relay de sudtec (MailChannels +
ImunifyEmail) y trae la cabecera **`X-MC-Relay: Junk`** — algo en el propio
trayecto de sudtec lo está clasificando como basura. A la casilla de Connie
igual le llega a Recibidos; a bd@ puede que lo esté comiendo esa clasificación.
Quien administre el correo de sudtec.cl debería mirar ahí.

## Volumen

- **201** correos de cg@ en total en la casilla de Connie
- **55** en los últimos 30 días · **15** en los últimos 7 → **~2 por día**
- Todos con el asunto `[Solicitud de presupuesto]`, cuerpo HTML, sin adjuntos

## La solución que armé

`bin/reenvio_sudtec.py` — corre por cron, y en cada pasada:

1. Busca en Gmail `from:cg@sudtec.cl newer_than:2d` (la ventana de 2 días da
   margen si estuve caído; no provoca duplicados porque el filtro real es el
   estado).
2. Descarta los id que ya están en `memory/estado/reenvio_sudtec.json`.
3. Reconstruye cada correo **limpio** (descarta las cabeceras del relay de
   sudtec, incluida la `Junk`) conservando el cuerpo HTML intacto, y lo manda a
   `bd@sudtec.cl` con asunto `RV: [Solicitud de presupuesto]` y `Reply-To:
   cg@sudtec.cl`, para que bd@ conteste al cotizador y no a Connie.
4. Guarda el id **apenas envía cada uno**, no al final: si me corto a la mitad,
   no reenvío dos veces.

En la primera corrida real **no manda el historial**: marca lo que ya existe
como visto y desde ahí en adelante solo reenvía lo nuevo.

Modo simulación (`sin --enviar`) para ver qué haría sin mandar nada.

## Estado

- ✅ **ACTIVO desde el 17-ago-2026, 20:50.** Connie dio el OK y pidió partir el
  **18-ago-2026 a las 06:00**.
- Crons puestos en `crons/jobs.txt`: **06:00, 15:00 y 23:00** todos los días.
- Marca inicial puesta el 17-ago a las 20:50: los 5 correos que ya estaban en la
  ventana quedaron como vistos. **No se reenvió historial.**
- Arranque diferido (`no_antes_de` en el estado): la pasada de las 23:00 de hoy
  **no hace nada** y no toca el estado, así el primer envío real es mañana 06:00
  con todo lo que llegue de aquí a esa hora.

## Decisiones ya tomadas (no volver a preguntar)

- **Horarios: 06:00 / 15:00 / 23:00.** Ella los eligió sabiendo que eso implica
  hasta **9 h** de espera entre pasadas; se lo advertí y lo aceptó.
- **Sin historial**: los 15 correos atrasados de la última semana **no** se
  reenvían. Si algún día los quiere, los pide.
- **`Reply-To` = Connie.** Historia corta: primero puse `cg@`, ella preguntó por
  qué, al revisar resultó que el original trae el mail del **cliente**, y lo dejé
  así. **El 17-ago a las 20:55 ella lo cambió: las respuestas de bd@ vuelven a
  ella.** Razón: bd reparte la cotización entre los **vendedores**, y son ellos
  los que hablan con el cliente. Así que el `Reply-To` del cliente se **pisa a
  propósito** — si se dejara pasar, bastaría que bd apretara Responder para
  escribirle al cliente antes de tiempo. Verificado: el mail del cliente no queda
  en ninguna cabecera del reenvío.
- **Aviso por Telegram:** solo cuando reenvía algo o cuando falla. Si no hay
  correos nuevos, silencio.

## Primer envío real — 17-ago-2026 23:35 ✅

Connie pidió probar con la solicitud que acababa de llegar (msg 38), sin esperar
a las 06:00. **Se levantó el seguro de hora y el sistema quedó vivo desde ahí.**

Se envió **por el script real del cron**, no a mano: así la prueba vale como
prueba del cron.

- Correo original: `1a012c026cce7d46`, del cliente `capitan11@cbqn.cl`
- Salió: `De: pfeifer.constanza@gmail.com` · `Para: bd@sudtec.cl` ·
  `RV: [Solicitud de presupuesto]` · `Responder a: pfeifer.constanza@gmail.com`
- **Verificado en la bandeja de enviados**, no solo por el código de respuesta
- **El correo del cliente no quedó en ninguna cabecera** ✔
- **Anti-duplicado probado en vivo:** segunda corrida seguida → «Sin correos
  nuevos». No reenvía dos veces.

## Lo que sigue pendiente

- El **arreglo de fondo**: por qué `bd@sudtec.cl` no recibe correos en los que
  figura como destinatario directo. Lo tiene que ver quien administre el correo
  de sudtec.cl. Pista: `X-MC-Relay: Junk` en el trayecto.

---

## 18-ago-2026 — Auditoría de políticas 2026

Connie pidió revisar las políticas nuevas de Meta y las que vienen para Google
Ads, y dejar la cuenta en orden. Resultado en [[politicas-2026]]
(`clientes/sudtec/politicas-2026.md`).

**Resumen:** los 13 anuncios están aprobados y el presupuesto sigue bajo el tope.
Tres hallazgos abiertos: el claim de certificación EN/NFPA no está respaldado en
el sitio, los anuncios dicen 24h mientras el sitelink dice 48h, y no existe
política de privacidad. **Meta no se pudo auditar: no hay integración de Meta Ads.**

Esperando 4 respuestas de Connie antes de tocar nada.

---

## 23-ago-2026 — Cómo van las campañas (Connie preguntó, msg 308)

Comparativo semana contra semana, cuenta `9907217991`:

| | 16-22 ago | 9-15 ago |
|---|---|---|
| Gasto | $71.008 | $55.062 |
| Conversiones | 27 | 31 |
| CPA | $2.630 | $1.776 |
| CPC | $390 | $324 |
| Impresiones | 1.340 | 1.361 |

**Lectura:** las impresiones están parejas — no perdimos presencia. Lo que subió
es el **precio del clic**, y las conversiones bajaron. `Competencias` arrancó esta
semana ($4.276 / 1 conv) y encarece el promedio, pero **`Campaña Sudtec` sola
también subió su CPA**, de $1.776 a $2.567: no es solo la campaña nueva.

Mes: $200.528 gastados, proyección $278.928. El presupuesto no se agota.

**No se tocó nada** — rige el congelamiento del viaje ([[congelar-cambios-viaje-china]]).
Es la primera semana mala seguida (`malos_seguidos: 1` en vigilancia_cambios.json);
si se repite, cruza el umbral y ahí se propone con cifras.

Sigue pendiente de su respuesta la **conversión secundaria limpia** (ofrecida msg 304).

---

## 24-ago-2026 — La caída de solicitudes se confirmó en el sitio (cron 09:00)

`vigilancia_ads.py` disparó `HAY-QUE-AVISAR` por solicitudes bajas. **Antes de
avisar se verificó contra el sitio, y la alerta resultó real**, no un artefacto
del baseline.

**Cuidado con el baseline del script:** compara los últimos 3 días contra un
promedio plano de 14 días, así que **un lunes siempre mide vie+sáb+dom** y
tiende a gritar por el fin de semana. Acá la sospecha de «es solo el finde» se
cayó: los sábados y domingos anteriores **sí** traían pedidos (9-ago: 2,
15-ago: 1, 16-ago: 3).

**Pedidos reales en WooCommerce** (no correos): vie 21 = **0**, sáb 22 = **0**,
dom 23 = **1** (orden 11610, 20:09 Chile). Mismo vie-dom de la semana anterior: **7**.

**El tráfico no bajó** — por eso importa:

| | impr | clics | costo |
|---|---|---|---|
| vie 21 | 66 | 13 | $9.419 |
| sáb 22 | 159 | 24 | $10.165 |
| dom 23 | 241 | 35 | $11.006 |

$30.590 en 3 días contra $24.368 el vie-dom anterior: **+26% de gasto para 1
solicitud en vez de 7**. Es la continuación del CPA en alza del comparativo del
23-ago, pero ahora se ve en pedidos reales.

**Descartado:** sitio responde HTTP 200; sin páginas editadas desde el 18-ago;
no es pérdida de correos (los pedidos tampoco existen en Woo).

**El contador de Google marcó 2-4 conversiones esos días** y el sitio recibió 0-1.
Otra confirmación de [[contadores-no-son-envios]].

**Presupuesto sin riesgo:** mes $211.467, proyección $280.067 de $300.000.

**No se tocó nada** — rige [[congelar-cambios-viaje-china]]. Se le pidió a Connie
(msg 322) permiso para **enviar una solicitud de prueba por el formulario**: es lo
único que no se puede descartar desde afuera. **Pendiente de su OK.**

### 24-ago 15:00-16:00 — investigación a fondo, y un diagnóstico equivocado de por medio

**Primero el error, que importa más que el resto:** le mandé a Connie (msg 328) la
teoría de que LiteSpeed servía páginas vencidas y el **nonce caducado** rompía el
cotizador. Ella aprobó actuar. **Probé antes de tocar y era falso**: YITH acepta el
nonce viejo igual. Corregido en msg 330. Detalle en [[litespeed-nonce-vencido-sudtec]].
**No se purgó la caché** — que además ya causó 500 en este sitio el 20-ago.

**La línea base, que es lo que faltaba** (pedidos de Woo, 38 días, convertidos a
hora de Chile):

- **1,92 solicitudes/día** de promedio · mediana **2**
- días en cero: **6 de 38 (16%)** · **racha máxima en cero: 2 días**
- **21-24 ago: 1 solicitud en total**, contra ~8 esperables
- probabilidad de que sea azar: **~0,4%** → el quiebre es real

⚠️ El conteo se hizo con `--limite 900000`; sin eso el helper corta en 6.000
caracteres y **da un número menor y creíble** ([[sudtec-wp-trunca-salida]]).

**Lo que se verificó sano** (todo de solo lectura):

| Chequeo | Resultado |
|---|---|
| `/lista-productos/` <i>(destino real de General e Improfor)</i> | 200, escritorio y móvil, 32 botones |
| Destinos con `?yith_wcan=1&product_cat=…` | 200, con botones |
| Endpoint `add_item` por `/?wc-ajax=yith_ywraq_action` | acepta y agrega |
| `/cotizacion-sudtec/` con sesión | muestra el formulario con el ítem |
| Términos de búsqueda 17-20 vs 21-24 | **misma calidad**, sin basura nueva |
| Snippets de Kai del 20-ago | solo aplican a taxonomías, **no** a `/lista-productos/` |

**Causa: NO encontrada.** Se dijo así, sin sustituto inventado.

**No se mandó la solicitud de prueba pese al «dale»**, y se le explicó por qué:
desde el contenedor **no hay navegador** (ni chromium, ni node, ni playwright), así
que solo se puede simular con `curl` sin ejecutar JS — justamente el tramo que falta
por probar. A cambio crearía un lead falso hacia `bd@`, que ya pasó el 20-ago. Se le
ofreció mandarla igual si la quiere.

**Pedido a Connie:** la prueba de 30 segundos en navegador sobre `/lista-productos/`.
Es la única concluyente. **Pendiente de su respuesta.**

**Observación menor:** el tráfico por «improfor» pasó de **15% a 22%** de los clics
(9 → 10 de 61 → 45). Convierte mal por naturaleza, pero no explica una caída de 10×.

### 24-ago 15:27 — ✅ Connie probó en navegador: el sitio está sano

Hizo la prueba pedida (msgs 332-334, con foto): **el botón funciona**, el producto
se agrega y sale el aviso. **Queda descartado el embudo como causa de la caída** —
el problema es de demanda o de anuncios.

De paso pidió cambiar los textos del aviso: ver
[[snippet-textos-cotizador]] (preparado, **no aplicado**, esperando su OK).

### 24-ago 15:28 — Revisión de grupos de anuncios (pedida por ella, msg 335)

14 días, 11 al 24-ago:

| Campaña | Grupo | Estado | Clics | Costo | CPC |
|---|---|---|---|---|---|
| Campaña Sudtec | **General** | ENABLED | 324 | **$120.117** | $370 |
| Competencias | Improfor | ENABLED | 21 | $5.702 | $271 |
| Campaña Sudtec | **Botas** | ENABLED | **1** | $618 | $618 |
| Campaña Sudtec | Cámara Termal · Botas de Bomberos · Hi lift | REMOVED | 0 | 0 | — |
| Competencias | fireground · maryun · Cespal Talca · Garmendia | PAUSED | 0 | 0 | — |
| Botas Bomberos | Grupo de anuncios 1 | ENABLED | 0 | 0 | — |

**Tres cosas que salen de ahí:**

1. **Concentración total en «General»: 95% del gasto y de los clics.** No hay nada
   que amortigüe si ese grupo se cae, que es justo lo que pasó estos 4 días.
2. **«Botas» está muerto:** 39 impresiones y 1 clic en dos semanas pese a todo el
   trabajo hecho encima. Ya estaba medido el 21-ago: **sus keywords de marca no
   tienen volumen en Chile**. No es configuración, es demanda inexistente.
3. **El CPA de Google engaña:** marca **52** conversiones en 14 días contra **27**
   solicitudes reales en Woo. **CPA real $4.683**, no ~$2.400
   ([[contadores-no-son-envios]]).

**No se propusieron cambios** — rige [[congelar-cambios-viaje-china]]. Ofrecida una
propuesta escrita para su vuelta.

### 24-ago 19:00 — pasada de reenvío: sin correos. El lunes sigue en cero.

Reenvío corrido **primero en simulación** ([[contadores-no-son-envios]] no, la
regla es la del 20-ago): si Connie hubiera hecho el envío de prueba que se le
pidió, no podía salir hacia `bd@` como si fuera un cliente. **No había nada**, así
que la precaución no costó nada y la regla queda ejercitada.

**Último pedido en Woo sigue siendo el #11610 del 23-ago 20:09.** O sea el lunes
24 va **0 cotizaciones a las 19:00**, con un histórico de ~2/día en día hábil.

Acumulado: 21 → **0** · 22 → **0** · 23 → **1** · 24 → **0** (a las 19:00).

**No se le avisó**: el cron manda silencio si no hay correos, y no hay hallazgo
nuevo que agregue a lo ya reportado en msg 331. Se reporta en la pasada de las
23:30 con el día cerrado, que ahí sí es un dato concluyente.

### 24-ago 19:55 — Puntaje de calidad y revisión creativa (pedido por Connie, msg 351)

**Puntaje de calidad, 30 días:** 232 keywords, solo **61 con QS asignado**.
**Promedio 4,3/10** y **31 de 61 bajo 5**.

| Keyword | QS | Anuncio | Página | Impr | Clics |
|---|---|---|---|---|---|
| equipos de bomberos (broad) | **8** | sobre prom | promedio | 2.058 | 278 |
| botas bombero (broad) | **5** | BAJO | **BAJO** | 381 | 56 |
| accesorios bomberos (exact) | 7 | sobre prom | **BAJO** | 78 | 11 |
| articulos para bomberos (exact) | 6 | promedio | **BAJO** | 161 | 18 |
| tienda de bomberos (exact) | 4 | promedio | **BAJO** | 30 | 7 |

**El patrón dominante: la componente que Google marca baja es la EXPERIENCIA DE LA
PÁGINA DE DESTINO, no el anuncio.**

**Hipótesis con base:** todos los anuncios de `General` apuntan a
**`/lista-productos/`**, el catálogo completo. Quien busca «botas bombero» aterriza
en una lista de todo y tiene que buscar. Eso explica a la vez el QS bajo de página
y una conversión pobre.

⚠️ **Se le dijo explícitamente que esto NO explica la caída de estos 4 días** — es
una debilidad de siempre, no un cambio reciente. Después del error del nonce
([[litespeed-nonce-vencido-sudtec]]) toca separar bien lo estructural de lo agudo.

**Fuerza de los anuncios:**

| Grupo | Anuncios | Fuerza |
|---|---|---|
| General | 2 | **BUENA** <i>(los que realmente corren)</i> |
| Botas | 1 | **BUENA** — nombra modelos: Lytos FR-1401 a 1406, Jolly, Blauer |
| Improfor | 2 | **POBRE** — esperable: es campaña de competencia y no se puede usar su marca |
| Cámara Termal · Botas de Bomberos · Hi lift | — | grupos eliminados, no corren |

**Tres defectos concretos, encontrados leyendo el creativo (msg 353):**

1. **Falta de ortografía EN VIVO** en un anuncio de General:
   «Uniformes con **certificacion** EN y NFPA» — sin tilde.
2. **Contradicción de plazo dentro del mismo grupo:** un anuncio promete
   «Cotización en **24h**» y el otro «Cotiza en Menos de **48 Hrs**». Compiten por
   las mismas búsquedas.
3. **Mezcla de tuteo y usted** entre anuncios («Solicite» vs «Cotiza»).

Sigue abierto lo del 18-ago: la afirmación de **certificación EN y NFPA** no está
respaldada en el sitio (riesgo de política, ver [[politicas-2026]]).

**No se tocó nada.** Ofrecido corregir tilde y plazo cuando ella diga.

### 24-ago 20:00 — «¿Pausamos el grupo Botas?» (Connie, msg 354)

**Respuesta: no, y la premisa no se cumple.** Ella suponía que Botas le estaba
quitando tráfico a General.

**Lo verificado antes de responder:**

1. **La correlación con el ruteo del 21-ago NO se sostiene.** Se midió el tráfico
   diario de las keywords de botas, 14 al 24-ago: **bajó** después del 21
   (16·10·29·34·14·14 → 6·2·7·4·5), no subió. La reversión del ruteo **no**
   inundó General de búsquedas de botas. Hipótesis descartada con datos.
2. **General ya captura las botas:** `botas bombero` (260 búsquedas/mes) vive en
   **General**, con 381 impresiones y 56 clics en 30 días. Botas recibe migajas.
3. **Pausar libera $44/día** de ~$9.800 diarios: **0,45%**. No mueve la aguja.
4. **Negativas revisadas: 74 de grupo + 23 de campaña = 97.** **HAIX no está en
   ninguna**, así que la propuesta del 21-ago sigue abierta y vale
   ([[botas-volumen-keywords]]: 420 búsquedas/mes de una marca que Sudtec no vende).
   Tampoco hay negativa `botas` en General — coherente con la reversión del 21.

**El diagnóstico invertido:** el grupo Botas es **el único que apunta a la página
correcta** (`/product-category/epp/botas/`) y su anuncio tiene fuerza **BUENA**.
General manda esas búsquedas al catálogo completo, que es justo donde Google marca
la página **bajo el promedio**. Pausar Botas empeoraría eso, no lo arreglaría.

**Propuesto (sin aplicar, rige [[congelar-cambios-viaje-china]]):**

- Volver a rutear botas al grupo Botas, **ahora que el bloqueo original ya no
  existe** — el 21-ago se revirtió porque el anuncio estaba rechazado por el 403,
  y hoy está aprobado con destino corregido.
- **Con regla de corte:** si en 5 días no levanta impresiones, revertir solo.
- **Negativa de HAIX**, que es ahorro sin contra.

### 24-ago 20:10 — ✅ Aplicados los dos cambios de Ads (Connie: «si dale a las dos», msg 356)

**Verificaciones previas, porque este mismo ruteo salió mal el 21-ago:**

- **El grupo Botas SÍ tiene cobertura** para atajar el tráfico: `botas bombero`,
  `botas de bomberos`, `botas para bomberos`, `botas incendio`,
  `botas para incendios forestales`, `botas seguridad incendio` — todas en
  **concordancia de frase** y ENABLED. `botas lytos` sigue pausada (volumen 0).
- **Sudtec tiene 0 productos HAIX** (`sudtec_wp.py productos --buscar haix`).

**1. Negativa `haix` BROAD a nivel de campaña** (Campaña Sudtec, `22490713380`).
`resourceName: customers/9907217991/campaignCriteria/22490713380~41753151`.

**2. Ruteo: se pausaron 3 keywords amplias de botas en General** (`181820804074`):

| Keyword | criterion_id |
|---|---|
| `botas bombero` BROAD | `297314270360` |
| `botas incendio` BROAD | `345382888741` |
| `bota bomberos` BROAD | `2369517656523` |

**Se eligió esto y NO la negativa amplia `botas` en General**, que es la
configuración que el 21-ago dejó el tráfico en blanco cuando el anuncio de Botas
estaba rechazado. Pausar keywords consigue el mismo ruteo y **se revierte
reactivando esas 3**, sin cortar tráfico de golpe.

**Verificado después:** todas las keywords de botas en General quedan PAUSED; las
del grupo Botas siguen ENABLED; la negativa `haix` aparece en la campaña.

⚠️ **Riesgo real declarado a Connie (msg 357):** la campaña usa
**MAXIMIZE_CONVERSIONS**, así que Google decide las pujas, y el grupo Botas
**casi no tiene historial de conversiones**. Puede no arrancar aunque tenga la
cancha libre. Las pujas por grupo (`cpc_bid_micros`) son irrelevantes con esa
estrategia.

**Regla de corte programada** (`crons/jobs.txt`, 29-ago 10:00, se borra sola):
si el grupo Botas no junta **≥20 impresiones** entre el 25 y el 28, se reactivan
las 3 keywords con los `resourceName` anotados arriba y se avisa.

**No se tocaron presupuestos ni pujas.**

### 24-ago 23:30 — Cierre del lunes: 1 cotización, reenviada

**Reenvío corrido primero en simulación** — mostró 1 pendiente. **Se envió muy
rápido después, sin inspeccionar antes qué era.** Se verificó *a posteriori* y por
suerte era legítima, pero el orden correcto es **mirar y después enviar**: la
simulación no sirve de nada si no se lee.

**#11612 · 24-ago 20:22 Chile · `ywraq-new`**
`Cuerpo de Bombero Ultima Esperanza` · `capitanprimera1927@gmail.com` (dominio
válido, chequeado por la regla del 20-ago). Reenviada a `bd@sudtec.cl`.

**Sin huecos:** los ids de Woo saltan (#11611 no existe como pedido), pero no
falta ninguna cotización.

**La racha, ya con el lunes cerrado:**

| día | cotizaciones |
|---|---|
| 21-ago | 0 |
| 22-ago | 0 |
| 23-ago | 1 (20:09) |
| 24-ago | **1 (20:22)** |

Sigue bajo la media de **1,92/día**, pero **menos dramático de lo que se veía a las
19:00**, cuando el lunes iba en cero. Se le dijo así de explícito.

**Observación sin conclusión:** las dos últimas entraron **pasadas las 20:00**,
cuando antes llegaban repartidas por todo el día (08:35, 12:13, 14:19, 15:55…).
Con n=2 no significa nada; queda anotado para mirar.

**Los cambios de Ads de hoy (ruteo de botas + negativa haix) empiezan a contar
desde el 25-ago.** Corte programado al 29.

### 25-ago 04:00 — ✅ Purga de caché ejecutada y verificada

**Estado ANTES (visitante normal, sin cache-buster):**

| página | caché generada | texto |
|---|---|---|
| `/` | 24-ago 20:35 | **nuevo** ✔ |
| `/lista-productos/` | 24-ago 20:55 | **nuevo** ✔ |
| `/servicios-sudtec/` | 24-ago 19:55 | CSS nuevo ✔ |
| `/product-category/epp/botas/` | **22-ago 03:30** | **viejo** ✗ |
| `/producto/set-alzaprima-…/` | **22-ago 19:20** | **viejo** ✗ |

**Hallazgo:** las páginas de más tráfico **se habían refrescado solas** anoche
(probablemente al guardar el form 6789 y al activar snippets, que disparan purgas
parciales). El TTL **no** era infinito como se supuso el 24 a las 15:00.

**Lo que seguía viejo eran las categorías y fichas de producto** — y ahí estaba lo
importante: `/product-category/epp/botas/` **es el destino del ruteo aplicado
ayer**. Sin purgar, el tráfico de botas habría empezado a llegar hoy a una página
de hace 3 días. Por eso la purga se ejecutó igual, en vez de darla por innecesaria.

**Ejecución:** snippet temporal con ruta admin-only →
`do_action('litespeed_purge_all')` + `\LiteSpeed\Purge::purge_all()` → ambas
respondieron. **Snippet borrado en el mismo turno** (endpoint en 404). Esta vez el
DELETE sí funcionó, con la secuencia vaciar+desactivar y después borrar.

**Verificación posterior:** las 5 páginas en **HTTP 200**, regeneradas 04:02,
**«Enviar cotización» presente y «Explorar la lista» en cero** en todas. Sin 500 en
ningún momento — la primera petición tardó 2,0s regenerando y la siguiente 0,37s.
Campos `field_4` y `field_9` siguen en `type="text"`.

**Cron borrado** (era de una vez).

---

## 27-ago-2026 · Se revirtió el ruteo de botas (Google Ads)

**Qué pasó.** El cron de vigilancia de cambios (09:30) dio **HAY-QUE-AVISAR** por
quinto día seguido. Cifras de los últimos 7 días contra la línea base (30 días
previos al 19-ago):

| | Ahora | Base | |
|---|---|---|---|
| Conversiones/día | **3,4** | 4,67 | **−27%** |
| CPA | **$3.084** | $1.675 | **×1,84** |
| Gasto 7d | **$74.012** | — | por **24** conversiones |
| Grupo «Botas de Bomberos» | **63** impresiones · **1** conversión | — | no despegó |

A la tasa anterior, esos $74.012 compraban **~44** conversiones en vez de 24.

**Decisión.** Se le presentaron las cifras a Connie con propuesta explícita y sin
tocar nada. Aprobó por chat (msg 490: *«si reactivemos entonces»*). Se
**reactivaron a ENABLED** las 3 keywords de botas en el grupo **General**
(`181820804074`), todas en concordancia **amplia**:

- `297314270360` — botas bombero
- `345382888741` — botas incendio
- `2369517656523` — bota bomberos

**Verificado con una relectura posterior**, no con el 200 del mutate. **Ningún
presupuesto tocado.**

### Dos cosas que conviene no perder

**1. Esto no explica toda la caída.** La mala racha arranca el **23-ago** y el
ruteo se cambió el **24-ago 20:10**: el deterioro **precede** al cambio. Los
sospechosos que quedan son los cambios del **19-ago** — «accesorios bomberos»
pasada a concordancia de **frase**, y las negativas **«reloj» / «relojes»**.
Hay un cron el **31-ago** que da veredicto y avisa **en los dos casos** (la
vigilancia diaria solo habla cuando algo está mal, así que una recuperación
pasaría en silencio).

**2. La regla automática que se había dejado para el 29-ago estaba rota por dos
lados**, y por eso se borró:

- Medía **solo impresiones** (umbral 20). El grupo llevaba **63 impresiones con 1
  conversión**: habría caído en la rama «no revertir» pese a no producir negocio.
  **Medir alcance en lugar de negocio da el veredicto contrario al correcto.**
- Filtraba por `ad_group.name = 'Botas'`, pero el grupo se llama **«Botas de
  Bomberos»**. Ese igual exacto no devolvía ninguna fila.

**Sigue pendiente de Connie** (congelado por el viaje, vuelve el 18-sep): las 3
negativas propuestas el 26-ago — «cotona ignífuga», «traje encapsulado» y «epp».
Ver `memory/estado/negativos_pendientes.json`.

## 30-ago-2026 · La vigilancia descarta el ruteo como causa

`vigilancia_cambios.py` dio **HAY-QUE-AVISAR**: **8 días seguidos** peor que antes de
los cambios del 19-ago. **2,7 conv/día** contra **4,7** de base y **CPA 3.928** contra
**1.675**. Ventana de 7 días: 19 conversiones, 74.640 CLP, 1.095 impresiones. Grupo
Botas: 69 impresiones, 1 conversión.

**El hallazgo no es que esté mal, es qué queda descartado.** El 27-ago se reactivaron
las 3 keywords de botas en General suponiendo que la causa era el ruteo. Tres días
después **no se recuperó y empeoró**: el 27 iba en 3,4 conv/día y CPA 3.084, hoy 2,7 y
3.928. **El ruteo no era la causa.**

Sospechosos que quedan, todos del 19-ago: **«accesorios bomberos» en concordancia de
FRASE** y las negativas **«reloj» / «relojes»**.

**Propuesto a Connie, no ejecutado:** revertir esos dos. **No se tocó nada** — la regla
es que no se cambia sin su OK, y la vigilancia solo avisa.

**Nota de criterio:** el aviso salió a las 09:30 de Chile = **21:30 en China**, justo a
la hora del show que ella tenía planeado en 芙蓉镇. Se mandó igual —callarse no es
opción— pero **diciéndole explícitamente que no corre y que lo vea mañana**. Un dato
sin urgencia no debería robarle la noche.

Mañana 31-ago 10:00 corre el cron del **veredicto formal** con la ventana 28–30, que le
avisa pase lo que pase. Ya se le anticipó que lo va a recibir, para que no le llegue
como repetición.

## 31-ago-2026 · La caída llega a las cotizaciones (día 9)

Las dos vigilancias dieron **HAY-QUE-AVISAR** el mismo día, y por primera vez el
daño se ve en el **negocio**, no solo en la cuenta de Ads:

- **Cotizaciones: 2 en 3 días** contra **6,4** esperadas para ese lapso (14 días: 30).
- **9 días seguidos** peor que antes del 19-ago: **2,3 conv/día** contra **4,7** de
  base, **CPA 4.263** contra **1.675**. Ventana 7 días: 16 conversiones, 68.207 CLP,
  908 impresiones. Botas de Bomberos: 54 impresiones, 1 conversión.
- **Gasto sano:** 278.927 CLP en el mes contra un límite de 300.000. El problema no
  es que gaste de más, es que rinde menos.

**La tendencia empeora, no se estabiliza:** el 27-ago iban 3,4 conv/día y CPA 3.084;
el 30-ago 2,7 y 3.928; hoy **2,3 y 4.263**. Refuerza lo del 30-ago: el ruteo no era
la causa.

**Enviado en UN solo mensaje (msg 599), no dos.** Los dos crons (09:00 y 09:30)
alertaron por separado, pero mandarle dos mensajes del mismo tema —y un tercero a
las 10:00 con el veredicto— es el ruido que ella pidió evitar. Se consolidó, se le
dijo que no corre para hoy (eran las **21:30 en China**) y se le anticipó que el
veredicto formal venía en camino para que no lo leyera como repetición.

**Propuesto, no ejecutado:** revertir «accesorios bomberos» de FRASE a amplia y sacar
las negativas «reloj» / «relojes». **Nada tocado** — sigue esperando su OK.

## 31-ago-2026 · Revert de los cambios del 19-ago (aprobado y ejecutado)

Connie aprobó por chat (msg 600, *«Dale nomad»* = dale nomás). Ejecutado y
**verificado por relectura**, no por el 200 del mutate.

### Lo que la lectura previa corrigió de mi propia propuesta

Yo le había dicho que el 19-ago «accesorios bomberos» pasó a concordancia de
**frase**. **Falso.** El `change_event` mostró que ese día se **pausaron amplia y
frase**, dejando **solo la exacta** activa. O sea la restricción fue más dura de lo
que yo tenía anotado. Se lo dije en el mismo mensaje en vez de dejarlo pasar.

**Regla:** antes de ejecutar un cambio aprobado, releer el estado real. La
aprobación era sobre la intención (volver a amplia), y esa se cumplió — pero el
mecanismo no era el que yo había descrito.

### Qué quedó hecho

- **`accesorios bomberos`** (grupo General `181820804074`): reactivadas
  **amplia** (`295755597536`) y **frase** (`452736550247`). Con la exacta
  (`321680463358`) que ya estaba activa, quedan **las tres ENABLED** = estado
  anterior al 19-ago.
- **Negativas `reloj` (`22229250`) y `relojes` (`10251086`)**: eliminadas de las
  **dos** campañas — `Campaña Sudtec` (`22490713380`) y `Competencias`
  (`23598502728`). Se habían creado juntas el **20-ago 03:15**, misma tanda.
  Relectura: **ninguna viva**.
- **Presupuestos NO tocados**, verificado después: Sudtec **9.100** CLP/día,
  Competencias **700**.

### Lo que NO se tocó, a propósito

La negativa de grupo **«relojes para bomberos»** (`1137551670671`, creada 19-ago
15:58) sigue viva. Es del mismo lote pero ella nombró solo `reloj`/`relojes`, y es
específica. Si el revert no levanta, es candidata.

### El matiz que se le dijo, no se escondió

De los dos cambios, **el que puede mover la aguja es la keyword amplia**. Las
negativas de reloj eran **sospechoso débil**: si Sudtec no vende relojes,
bloquearlas estaba bien. Se sacaron por venir en el paquete y porque reponerlas es
trivial. **Prometer menos de lo que se espera es mejor que vender una recuperación
que quizá no llegue.**

Veredicto prometido para el **3-sep**, con cron propio que avisa **en los dos
casos** (la vigilancia diaria solo habla cuando algo está mal).
