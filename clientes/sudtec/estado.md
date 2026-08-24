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
