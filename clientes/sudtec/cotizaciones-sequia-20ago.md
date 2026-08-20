# SUDTEC — «No ha llegado ninguna cotización» (20-ago-2026 12:52)

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
