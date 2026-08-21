# SUDTEC — «No ha llegado ninguna cotización» (20-ago-2026) — CERRADO: era un día flojo

## Los datos

- **Última cotización: 19-ago 21:51** (#10063). Desde medianoche del 20-ago, **cero**.
- **Primer cambio mío en el sitio: 10:47** del 20-ago.
- → **Hubo ~11 horas sin cotizaciones ANTES de que yo tocara nada.** La sequía no
  la causaron mis cambios.

## Volumen normal de la cuenta

| Día | Solicitudes |
|---|---|
| 19-ago | 6 |
| 18-ago | 3 |
| 17-ago | 2 |
| 16-ago | 3 |
| 15-ago | 1 |
| 14-ago | 3 |
| 13-ago | 3 |
| 12-ago | 2 |

**Promedio ~3/día.** Entran a cualquier hora, incluida madrugada (00:33, 00:52,
02:42, 04:43). Ayer la primera fue a las **12:35**.

Con **6 clics** hoy y tasa de conversión histórica ~10%, lo esperable a esa hora
era **menos de 1**. Cero a las 12:52 es **bajo pero dentro de lo normal**.

## Estado de las campañas (verificado por Composio)

| Campaña | Estado | Hoy |
|---|---|---|
| Campaña Sudtec | **ENABLED · SERVING** | 26 impr · 6 clics · 4.027 CLP |
| Competencias | ENABLED · SERVING | 8 impr · 0 clics |
| Prueba Max Rendimiento | REMOVED | — |
| Botas Bomberos (campaña) | REMOVED / ENDED | — |

Presupuesto de Campaña Sudtec: **9.100 CLP/día**.

⚠️ Las **26 impresiones** de hoy contra 180–330 de días normales llaman la
atención, **pero los datos del día en curso de Google llegan con retraso**. No se
reportó como alarma; queda para reverificar en la pasada de las 19:00.

## Lo que se verificó del cotizador

✅ El botón `add-request-quote-button` **está presente** en fichas de producto,
categorías y Lista Productos, con sus `data-wp_nonce`.
✅ El JS del plugin (`yith-woocommerce-request-a-quote-premium/frontend.min.js`)
carga con **200**.
✅ El endpoint de WooCommerce `/?wc-ajax=get_refreshed_fragments` responde **200**
con JSON válido.

## ❌ Lo que NO se pudo probar, y por qué

Se intentó reproducir el «agregar al cotizador» por AJAX con los parámetros exactos
que usa el plugin (`context=frontend`, `action=yith_ywraq_action`,
`ywraq_action=add_item`, `product_id`, `wp_nonce`, `yith-add-to-cart`, `quantity`).
Devolvió **400 / `0`**.

**Pero eso no prueba nada:** los controles con una acción inexistente y con
`admin-ajax.php` sin parámetros devuelven **exactamente lo mismo**. Este sitio
responde `400/0` a cualquier llamada a `admin-ajax`, así que **no se puede
distinguir "el handler falla" de "respuesta genérica"**.

**Conclusión honesta: desde fuera no se puede certificar el envío.** Se le pidió a
Connie la prueba de 30 segundos en navegador — es la única concluyente.

## Nota de transparencia

Cerca de las **11:00**, la purga total de caché provocó **500 transitorios** unos
minutos mientras el sitio regeneraba. Pudo costar alguna visita en esa ventana,
pero **no explica las horas previas**. Ver [[verificar-sin-rompe-cache]].

## Cómo reproducir esta revisión

    python3 bin/sudtec_wp.py api 'wc/v3/orders?per_page=25&_fields=id,number,date_created,status&orderby=date&order=desc'

Y por Composio: `campaign.status`, `campaign.serving_status` y métricas
`DURING TODAY` + `LAST_7_DAYS`.


## Pasada de las 15:00 — dato que acota el problema

**El script de reenvío (`reenvio_sudtec.py`) tampoco encontró correos nuevos** de
`cg@sudtec.cl`. Eso es **corroboración independiente**: no es que las
cotizaciones no se vean en WooCommerce, es que **no llegan correos tampoco**.

Descarta un fallo de visualización o de la API de Woo. El embudo está seco de
verdad.

### Cifras a las 15:00 (vía Maton, que recuperó cuota)

| | Hoy 15:00 | Días normales (completos) |
|---|---|---|
| Impresiones | **38** | 158–328 |
| Clics | **9** | 24–41 |
| Gasto | 5.951 de 9.100 CLP | ~8.000–11.000 |
| Conversiones | **0** | 3–9 |

**Lectura honesta:** con 9 clics y tasa histórica ~15%, lo esperable era **1–2**
cotizaciones. **Cero es bajo pero no imposible** — no alcanza para declarar avería.

Lo llamativo son las **impresiones**, muy por debajo. Puede ser el retraso conocido
de los datos del día en curso. **No se reportó como diagnóstico**, solo como
observación, para no repetir la falsa alarma de la mañana.

### Sigue bloqueado en lo mismo

**La prueba del navegador (agregar al cotizador) es la única concluyente** y solo
la puede hacer ella. Se insistió (msg 250) explicando por qué: desde fuera el sitio
responde igual ante una llamada válida y una inválida, así que no se puede
certificar el envío.

**Criterio para mañana:** si el 21-ago amanece con cotizaciones normales, fue un día
flojo. Si sigue en cero con clics entrando, es avería y hay que mirar el formulario
y el registro de conversiones.


## ✅ Cierre — 15:03: el formulario funciona

Connie hizo la prueba en navegador (msg 251) y **funcionó**. Confirmado por datos:
entró la solicitud **#10064** (Set Alzaprima Mighty Strut), `ywraq-new`, 15:03.

**Conclusión: no había avería. Fue un día flojo.** Con 9 clics reales y tasa
histórica ~15%, lo esperable era 1–2 cotizaciones; salió cero. Cabe en la varianza.

## ⚠️ El efecto secundario que casi se escapa

**La prueba generó DOS correos de cotización reales**, y el cron de reenvío de las
19:00 los habría mandado a `bd@sudtec.cl` **como si fueran un cliente**. Alguien
habría salido a perseguir una alzaprima inexistente.

Se detectó corriendo el script **en modo simulación** (sin `--enviar`), que imprime
lo que haría:

    [SIMULACION] reenviaria  id=1a0208e48decebae  ...  ->  bd@sudtec.cl
    [SIMULACION] reenviaria  id=1a0208e59322e341  ...  ->  bd@sudtec.cl

**Acción tomada:** los dos ids se agregaron a `reenviados` en
`memory/estado/reenvio_sudtec.json`, con un bloque `excluidos_a_proposito` que deja
constancia del motivo y de cómo revertirlo.

**Por qué se actuó sin preguntar:** mandar el correo es **irreversible y hacia un
tercero**; no mandarlo no pierde nada y se deshace en un segundo. Ante la duda, el
lado seguro es no enviar. Se le avisó de inmediato y se le ofreció soltarlos.

## Pendiente de su decisión

La solicitud **#10064 sigue viva** como `ywraq-new` y va a contar en los listados y
en las cifras del 20-ago. **No se borra sin su OK** (borrar un pedido no se
deshace). Preguntado en msg 252.

## Regla que queda

**Cuando alguien pruebe un formulario de producción, revisar qué automatismos se
disparan detrás.** Acá había un cron que convertía una prueba en un lead falso. La
prueba resuelve una duda y crea otra.

Y: **`reenvio_sudtec.py` sin `--enviar` es simulación** — usarlo siempre antes de
asumir qué va a mandar.


## ✅ 23:30 — llegaron dos y se cerró el tema

En la pasada de las 23:30 el reenvío mandó **2 solicitudes reales** a `bd@sudtec.cl`:

| Pedido | Hora (Chile) | Producto |
|---|---|---|
| **#10065** | 22:10 | Sujeción para cabinas de camiones LUKAS |
| **#10066** | 22:18 | Set Glassmaster |

Ambas de **Primera Compañía Cuerpo de Bomberos de Curacautín**.

**Confirma el diagnóstico:** no había avería. Formulario, campañas y reenvío
funcionan; el 20-ago fue un día flojo con la mayor parte del tráfico de botas caído
en el hueco del ruteo.

### ⚠️ El correo del solicitante tiene una errata

    primeracia.cbcuracautin@gmail.con     ← termina en .con, no .com

**Comprobado: el dominio `gmail.con` no resuelve.** Cualquier respuesta a esa
dirección **rebota** y se pierde un cliente que pidió **dos** productos.

Avisado a Connie (msg 274) para que quien tome la cotización pruebe con `.com` o
los ubique por otra vía.

**Vale como chequeo de rutina:** al reenviar cotizaciones, **validar que el dominio
del correo del solicitante exista**. Es barato y evita perder leads reales.

## 🕐 Dato técnico importante: WooCommerce guarda las fechas en UTC

`date_created` de `wc/v3/orders` viene en **UTC**, no en hora de Chile. Se confirmó
cruzándolo con la prueba de Connie: la planilla marcaba `2026-08-20T19:03:03` y ella
la hizo a las **15:03** de Chile → **UTC-4**.

**Restar 4 horas** (o 3 desde el 6-sep, con el horario de verano) antes de
comparar con horas locales o con lo que ella diga. Si no, se concluyen cosas falsas
sobre a qué hora entra el negocio.
