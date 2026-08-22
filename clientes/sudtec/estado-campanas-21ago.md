# SUDTEC — Estado de las campañas, 21-ago-2026 13:50

*Connie preguntó (msg 285): «revisar cómo van las campañas, no ha llegado ninguna
cotización». Esto es lo que se midió.*

## Las campañas están corriendo

Nada pausado ni caído. **Hoy hasta 13:50:** 41 impresiones · 10 clics · 7.320 CLP
· 3 «conversiones» (ver más abajo por qué van entre comillas).

## Causa 1 — la campaña vive topada de presupuesto

| Métrica | Campaña Sudtec |
|---|---|
| Presupuesto diario | **9.100 CLP** |
| Cuota de impresiones | **13,4%** |
| Perdida por **presupuesto** | **84,4%** |
| Perdida por ranking | 2,1% |
| CPC medio | **337 CLP** |

**Los anuncios sí compiten** —solo 2,1% se pierde por ranking—, pero el
presupuesto se acaba y dejan de mostrarse. Aparece en **1 de cada 7** búsquedas
que podría.

Y como el CPC sube, el mismo presupuesto compra menos cada semana:

| Fecha | Impr | Clics | Gasto | Conv |
|---|---|---|---|---|
| 14-ago | 267 | 31 | 8.305 | 5 |
| 17-ago | 328 | 41 | 9.716 | 4 |
| 19-ago | 182 | 29 | 11.132 | 3 |
| 20-ago | 165 | 24 | 11.964 | 2 |

## Causa 2 — la conversión mide lo que no es

Hay **una sola** acción de conversión: **«Cotización formulario»**. En GTM
(contenedor `GTM-NGQV7WCW`) la etiqueta `awct` dispara con el **trigger 22
«Envio de formularioo»**, de tipo `formSubmission` y **sin ningún filtro**.

Un `formSubmission` sin filtros cuenta **cualquier formulario del sitio**, no solo
la solicitud de cotización.

**Se ve hoy:** Ads reporta **3 conversiones** y en el sitio **no hay ninguna
cotización nueva**.

**Y pesa el doble**, porque la campaña usa **MAXIMIZE_CONVERSIONS**: reparte el
presupuesto guiándose por ese número. Está optimizando hacia un dato sucio.

*(Existe además un trigger 18 «Envío de formulario», también `formSubmission`, que
no está enganchado a ninguna etiqueta.)*

## Las cotizaciones, de verdad

| Pedido | Fecha (UTC) | Quién |
|---|---|---|
| 11609 | 21-ago 02:18 | Bomberos Curacautín |
| 11608 | 21-ago 02:10 | Bomberos Curacautín |
| 11607 | 20-ago 19:03 | **PRUEBA SUDTEC** (test de Connie, no cuenta) |
| 11602 | 19-ago 21:51 | Optima Industrial |

**El sitio guarda las fechas en UTC** (Chile = UTC−4). O sea las dos de Curacautín
entraron el **20-ago a las 22:10 y 22:18 hora de Chile**, y **hoy 21-ago no ha
entrado ninguna**.

Con solo 10 clics en el día, cero cotizaciones no es estadísticamente raro — pero
encima de la caída de tráfico sí explica la sensación de Connie.

## Propuesto a Connie (msg 287), sin aplicar

1. **Arreglar la etiqueta** para que cuente solo la cotización real. Es gratis y
   hace que el presupuesto que ya se gasta se use bien. **Es el de mayor palanca.**
2. **Después el presupuesto.** Con 84% de la demanda sin cubrir, subirlo es lo que
   más movería la aguja — pero es plata de ella: **el monto lo decide ella y no se
   toca solo.** Ojo: CLP no tiene centavos, el factor es **×1**.

## Lo que NO fue

**No fue el cambio de esta mañana.** El tope de presupuesto y la etiqueta mal
configurada son anteriores. Quitar la negativa `botas` (05:30) solo devolvió
tráfico a General; hoy el grupo Botas ya registró 3 impresiones.

---

# Cierre del 21-ago (18:55) — Connie volvió a preguntar (msg 290)

## Cómo cerró el día

**52 impresiones · 12 clics · 9.389 CLP · 0 cotizaciones.**

El presupuesto diario son **9.100 CLP** y se gastaron **9.389**: la campaña **se
quedó sin plata cerca de las 17:00** y dejó de mostrarse (última impresión 17:00).

## El CPC se duplicó

| | CPC medio |
|---|---|
| Hoy 21-ago | **782 CLP** |
| Media 7 días | **337 CLP** |

Evolución del CPC por día: 268 (14-ago) → 237 (17) → 441 (18) → 384 (19) →
498 (20) → **782 (21)**.

Y las impresiones al revés: 267 → 328 → 200 → 182 → 165 → **52**.

**Con presupuesto fijo y CPC al doble, el derrumbe de impresiones es aritmética.**

**No lo causó el cambio de las 05:30**: el desglose por hora muestra CPC alto ya a
la 01:00 (799/clic) y a las 02:00 (1.042/clic), antes de tocar nada.

## Dónde se va la plata — 453 términos de la semana

**El 87% del gasto (29.737 de 34.111 CLP) fue a búsquedas con CERO conversiones.**

| Término | Costo 7d | Clics | Conv |
|---|---|---|---|
| `improfor` | 2.943 | 9 | 0 |
| `halligan` | 2.532 | 3 | 0 |
| `segurycel santiago` | 1.320 | 1 | 0 |
| `segurycel` | 1.081 | 2 | 0 |
| `maryun puerto montt` | 640 | 2 | 0 |
| `improfort` | 614 | 1 | 0 |

**Segurycel, Maryun e Improfor son competencia.** El grupo General ya tiene
negativas para `steelpro`, `vicsa safety`, `romak`, `garmendia`, `improfor store`,
`workwear center`, `cespal talca`, `safety store`, `rmh`, `holmatro chile` — pero
**no** para `segurycel`, `maryun` ni `improfort`, así que ese tráfico se cuela.

*(Ojo: `improfor store` está bloqueado en EXACTA, lo que no bloquea `improfor` a
secas. La negativa exacta no cubre las variantes.)*

## Propuesto a Connie (msg 291), NADA aplicado

1. **Negativas `segurycel`, `maryun`, `improfort` en General** — gratis, frena la
   sangría de inmediato. *Esperando su OK.*
2. **Arreglar la etiqueta de conversión** (msg 287). *Esperando su OK.*
3. **Revisar la campaña Competencias**: 2.943 CLP en 7 días por `improfor`, cero
   cotizaciones. Es decisión comercial de ella.
4. **Después el presupuesto** — plata suya, monto lo decide ella. CLP = factor ×1.

## Hipótesis que une los dos hallazgos

La etiqueta cuenta como conversión **cualquier** formulario del sitio. La campaña
usa **Maximize Conversions**. Si Google cree que clics de búsquedas como
`segurycel` o `halligan` «convierten» —porque alguien usó el buscador del sitio—
**puja más caro por ellos**. Eso explicaría a la vez el CPC disparado y que el 87%
del gasto no produzca cotizaciones.

**No está probado**, pero es consistente con todo lo medido y es una razón más
para arreglar la etiqueta antes que subir el presupuesto: subir plata con una
señal sucia solo hace el problema más caro.

## Sigue sin respuesta

La autorización para **enviar una cotización de prueba** (msg 289) y descartar que
el formulario esté roto desde anoche. Sin eso, esa hipótesis queda abierta.

---

# APLICADO 21-ago 19:05 — negativas de competencia (Connie, msg 292: «hace el 1»)

Creadas en el grupo **General** (`181820804074`), las tres **BROAD** y ENABLED:

| Término | criterion_id |
|---|---|
| `segurycel` | 364551321517 |
| `maryun` | 320624629372 |
| `improfort` | 367217732843 |

Verificado por consulta: las tres activas. General queda con **74** negativas.

**Por qué BROAD y no EXACT.** La negativa exacta solo bloquea la consulta
idéntica: por eso `improfor store` (EXACT, ya existente) **no** evitaba el gasto en
`improfor` a secas ni en `improfort`. En amplia, la negativa bloquea cualquier
consulta que **contenga** el término, así que cubre `segurycel santiago` y
`maryun puerto montt`. Sudtec no vende ninguna de esas marcas → sin riesgo de
bloquear tráfico propio.

**Libera ~4.655 CLP/semana** que se iban en esos términos con cero conversiones.

**Ojo para el futuro:** las negativas de marca de competencia en General están casi
todas en EXACTA (`steelpro`, `vicsa safety`, `romak`, `garmendia`, `workwear
center`, `cespal talca`, `safety store`, `rmh`, `holmatro chile`). **Probablemente
estén filtrando igual** por variantes y consultas largas. Vale la pena revisarlas
—no se tocaron ahora porque Connie autorizó solo las tres.

## Sigue pendiente de ella

1. Etiqueta de conversión (msg 287) — **el de mayor impacto**.
2. Campaña Competencias: 2.943 CLP/7d por `improfor`, cero cotizaciones (msg 291).
3. Permiso para enviar una cotización de prueba (msg 289).
4. Presupuesto — su decisión, CLP factor ×1.

---

# Cierre 21-ago 23:30

**El día cerró con CERO cotizaciones.** Última real: 20-ago 22:18 hora de Chile
(pedidos 11608 y 11609, ambos de Bomberos de Curacautín).

## El formulario NO está roto (verificado sin escribir)

| Comprobación | Resultado |
|---|---|
| `/cotizacion-sudtec/` (la página real) | **200**, con el formulario renderizado |
| `/cotizacion/` | 301 → redirige, normal |
| `/lista-productos/` | 200, con los botones YITH |
| Plugin YITH Request a Quote Premium | **active** |
| Prueba propia de Connie (pedido 11607) | entró bien el 20-ago 19:03 UTC |

*(Ojo: `/lista-de-cotizacion/` da 404, pero ese slug me lo inventé yo al tantear —
no es la página real. No es un síntoma.)*

**Lo que NO se pudo verificar:** que el envío se complete de punta a punta. Eso
exige mandar el formulario de verdad. Se le pidió permiso a Connie (msg 289), no
lo dio, y **se retiró el pendiente** (msg 294): con todo lo demás sano, no
justifica crear un pedido falso en producción.

**Explicación más probable del cero de hoy:** no hubo tráfico. **52 impresiones**
contra 165 de ayer, con el presupuesto agotado a las 17:00.

## Contexto para leer los próximos días

**22-ago es sábado.** Las cotizaciones de bomberos e instituciones caen fuerte el
fin de semana: **un sábado en cero es normal y no indica falla.** El primer día
útil para juzgar si las negativas de competencia ayudaron es el **lunes 24-ago**.
Así se le advirtió, para que no lea el sábado como una emergencia.

## Estado de los pendientes de Connie

| Pendiente | Estado |
|---|---|
| Negativas de competencia | ✅ **aplicado** (msg 292) |
| Etiqueta de conversión | ⏳ esperando OK — **el de mayor impacto** |
| Campaña Competencias (`improfor`, 2.943 CLP/7d, 0 conv) | ⏳ esperando |
| Presupuesto | ⏳ decisión suya · CLP factor ×1 |
| Cotización de prueba | ❌ **retirado**, ya no hace falta |
| Llamar a Bomberos de Curacautín (933964206) | ⏳ en su cancha |

---

# 22-ago-2026 08:40 — Connie preguntó por la aparente contradicción (msg 295)

*«Si el dinero se acabó el otro día a las 17 hrs, cómo es que llegaron
cotizaciones a las 22 hrs? ¿Hay algún grupo gastando más de lo normal y no
convirtiendo?»*

## Respuesta 1: no había contradicción — son DOS DÍAS distintos

- Las cotizaciones de las 22:00 fueron el **jueves 20-ago** (#10065 a las 22:10,
  #10066 a las 22:18, hora de Chile).
- El presupuesto que se agotó a las 17:00 fue el **viernes 21-ago**.

**El 20-ago la campaña gastó hasta las 23:00** (total 11.965 CLP) y tuvo clics
pagados justo en esa franja: **22:00 → 2 clics / 1.566 CLP** y **23:00 → 3 clics /
683 CLP**. Las dos cotizaciones calzan con esos clics.

## ⚠️ Corrección de lo que se le dijo el 21-ago

Se le reportó que el viernes la campaña «se quedó sin plata cerca de las 17:00 y
**dejó de mostrarse** (última impresión 17:00)». **La segunda mitad es falsa.**

El desglose por hora del 21-ago muestra **17 impresiones entre las 17:00 y las
23:00** — siguió apareciendo. Lo que se detuvo fue el **gasto** (último a las
16:00), no la exhibición. No hubo ni un clic en esas 7 horas.

**Lección:** gasto en cero con impresiones > 0 NO es «dejó de mostrarse». En un
modelo CPC se paga por clic: cero gasto puede significar simplemente cero clics.
Mirar impresiones y gasto por separado antes de concluir.

## ✅ Zona horaria de la cuenta Ads: America/Santiago (moneda CLP)

Verificado con `SELECT customer.time_zone, customer.currency_code FROM customer`.
**`segments.hour` de Google Ads ya viene en hora de Chile** — no hay que
convertirlo. Ojo con no confundirlo con WooCommerce, que **sí** guarda en UTC y
hay que restarle 4 horas. Son dos convenciones distintas en el mismo análisis.

## Respuesta 2: no hay un grupo desviado — hay UNO SOLO que gasta

Gasto por grupo, últimos 7 días (total **68.886 CLP**):

| Campaña | Grupo | Estado | Impr | Clics | Gasto | «Conv» |
|---|---|---|---|---|---|---|
| Campaña Sudtec | **General** | ENABLED | 1.256 | 171 | **64.823** | 27 |
| Competencias | **Improfor** | ENABLED | 76 | 13 | **4.062** | 1 |
| Campaña Sudtec | Botas | ENABLED | 7 | 0 | 0 | 0 |
| *(resto)* | Cámara Termal, Hi Lift, Botas de Bomberos, Garmendia, Maryun, Cespal Talca, fireground | REMOVED/PAUSED | 0 | 0 | 0 | 0 |

**General concentra el 94% del gasto.** El desperdicio no es un grupo suelto: está
**dentro de General**, a nivel de término de búsqueda.

## Hallazgo nuevo: no es solo la competencia — los términos PROPIOS están caros

De los 438 términos de la semana (34.206 CLP), el **84% del gasto (28.839 CLP) fue
a búsquedas con cero conversiones**. Pero al mirar el top por gasto aparece algo que
antes no se había separado: **búsquedas legítimas de Sudtec a ~1.000 CLP el clic**.

| Término | Gasto 7d | Clics | CPC | Conv |
|---|---|---|---|---|
| `improfor` | 3.537 | 11 | 322 | 0 |
| `halligan` | 1.975 | 2 | **988** | 0 |
| `cascos incendios forestales` | 1.630 | 2 | **815** | 1 |
| `segurycel santiago` | 1.320 | 1 | 1.320 | 0 |
| `hachas para bomberos` | 1.124 | 1 | **1.124** | 0 |
| `elementos de proteccion personal` | 1.060 | 1 | 1.060 | 0 |
| `chaqueta de bomberos de chile` | 1.047 | 1 | 1.047 | 0 |
| `ropa ignifuga` | 1.042 | 1 | 1.042 | 0 |

**`halligan`, `hachas para bomberos`, `cascos incendios forestales`, `ropa
ignifuga` son productos que Sudtec SÍ vende.** No se bloquean. Pero a 1.000 CLP el
clic, un presupuesto de 9.100 se agota en **9 visitas**. Ese es el cuello real, y
es distinto del problema de la competencia (que ya se atacó con las negativas).

## 🔎 Prueba dura de que la etiqueta cuenta de más

- **Google Ads reporta 27 conversiones** en el grupo General (7 días).
- **El sitio recibió 18 cotizaciones en total** entre el 15 y el 21 de agosto,
  **contando todas las fuentes** (orgánico y directo incluidos), y una de esas 18
  fue la prueba de la propia Connie (#10064).

Ads dice haber generado **más conversiones que las cotizaciones que el sitio
recibió por todos los canales juntos**. Eso cierra la duda: la etiqueta cuenta
formularios que no son solicitudes de cotización.

*(Se le pasó como argumento en msg 298 para destrabar la autorización.)*

## Presupuesto: se está pasando del diario, y eso no se había reportado

Nominal **9.100 CLP/día**, pero Google permite gastar hasta el doble en un día
mientras cuadre el promedio del mes:

| Día | Gasto |
|---|---|
| 18-ago | 10.589 |
| 19-ago | 11.132 |
| 20-ago | **11.965** |
| 21-ago | 9.419 |

**Agosto 1-22: 190.133 CLP.** Media diaria 9.054 → **proyección de mes ~281.000**
contra el tope duro de **300.000** del cliente. Alcanza, pero con menos holgura de
la que sugiere el «9.100 diario». **No se toca el monto: es decisión de ella.**

## Enviado a Connie (msgs 296, 297, 298) — pendiente de su OK

1. **Arreglar la etiqueta de conversión** — ahora con la prueba 27 vs 18.
2. **Pausar el grupo Improfor** — 4.062 CLP/7d, cero cotizaciones.
3. Presupuesto: informado, sin tocar.

Se le recordó que **hoy es sábado** y un fin de semana en cero es normal; el primer
día útil para juzgar las negativas del viernes es el **lunes 24-ago**.

## Cómo reproducir

    # hora a hora (ojo: ya viene en hora de Chile)
    SELECT campaign.name, segments.date, segments.hour, metrics.impressions,
           metrics.clicks, metrics.cost_micros, metrics.conversions
    FROM campaign WHERE segments.date BETWEEN '2026-08-19' AND '2026-08-22'

    # gasto por grupo
    SELECT campaign.name, ad_group.id, ad_group.name, ad_group.status,
           metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
    FROM ad_group WHERE segments.date DURING LAST_7_DAYS

    # cotizaciones reales (restar 4 h: vienen en UTC)
    python3 bin/sudtec_wp.py api 'wc/v3/orders?per_page=60&_fields=id,number,date_created&orderby=date&order=desc'

Las 5 consultas de Ads fueron por **Maton**, que respondió sin problemas de cuota.

---

# 22-ago 08:45 — «¿Deberíamos pausar el grupo Improfor?» (msg 299)

Connie pidió opinión, **no autorizó nada**. Se le recomendó **no pausar todavía**
(msgs 300 y 301).

## 🔑 El dato que cambia la respuesta: los presupuestos NO son compartidos

| Campaña | Estado | Estrategia | Presupuesto | ¿Compartido? |
|---|---|---|---|---|
| **Campaña Sudtec** | ENABLED | MAXIMIZE_CONVERSIONS | **9.100 CLP/día** | **No** |
| **Competencias** | ENABLED | MAXIMIZE_CONVERSIONS | **700 CLP/día** | **No** |

**Pausar Improfor NO libera un peso para Campaña Sudtec.** Son presupuestos
separados (`explicitly_shared = false`): la plata no se traspasa, solo deja de
gastarse. Por eso pausarla **no ayuda** al cuello de botella real, que es el 84% de
impresiones perdidas por presupuesto en la campaña principal.

**Esto se verificó antes de opinar**, porque el argumento intuitivo —«ese gasto
podría estar en General, que sí convierte»— **habría sido falso** y la habría
llevado a esperar una mejora que no iba a ocurrir.

## Por qué no pausar todavía

1. **Es el 2,8% del gasto de la cuenta** (700/día ≈ 21.000/mes). No puede ser la
   causa de que la cuenta rinda poco.
2. **13 clics no son muestra.** Con la tasa histórica (~10-15%) lo esperable eran
   1-2 cotizaciones; cero cabe en la varianza. Es el mismo razonamiento que se
   aplicó el 20-ago con la «sequía» y que resultó correcto.
3. **Es nueva, no lleva meses fallando.** Sus 4.062 CLP de 30 días son exactamente
   los mismos 4.062 de los últimos 7 → **empezó a gastar esta semana**.
4. **Corre con la etiqueta sucia.** Competencias también usa MAXIMIZE_CONVERSIONS,
   así que hoy puja guiada por un dato falso. Juzgarla ahora es juzgarla con la
   balanza mala.

## Plan propuesto

1. Arreglar la etiqueta (la usan **las dos** campañas).
2. Dejar Improfor 2-3 semanas con datos limpios.
3. **Mediados de septiembre:** si sigue en cero cotizaciones **reales**, pausar con
   fundamento.

## Si ella decide pausar igual

Se le dijo que se pausaría **la campaña completa**, no el grupo: **Improfor es el
único grupo activo que le queda a Competencias** (fireground, Maryun, Garmendia y
Cespal Talca ya están PAUSED). Dejar la campaña encendida y vacía solo genera
confusión al releerlo.

## Grupos con gasto, últimos 30 días

| Campaña | Grupo | Impr | Clics | Gasto | «Conv» | CPC |
|---|---|---|---|---|---|---|
| Campaña Sudtec | General | 5.716 | 724 | **242.495** | 135 | 335 |
| Competencias | Improfor | 76 | 13 | 4.062 | 1 | 312 |
| Competencias | fireground *(hoy PAUSED)* | 154 | 15 | 3.923 | 3 | 262 |

Nota: el CPC de Improfor (**312**) está **por debajo** del de General (335). El
problema de Improfor no es que sea caro por clic, es que no hay evidencia todavía
de que convierta.
