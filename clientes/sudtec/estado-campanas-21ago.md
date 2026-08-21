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
