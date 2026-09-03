---
name: cotizaciones-del-sitio-son-el-termometro
description: Las conversiones de Google Ads en Sudtec han estado tanto en cero como infladas 2,6x; la única fuente fiable de si el negocio va bien son las cotizaciones de WooCommerce.
metadata:
  type: project
---

**3-sep-2026.** Connie contó (msg 683) que **ya había intentado arreglar la medición
y «todo bajó»**, que estuvo días sin conversiones y **tuvo que devolverlo**. Se cruzó
lo que reporta Google contra las cotizaciones reales del sitio y el resultado dio
vuelta el diagnóstico de dos semanas.

## Lo que mostró el cruce

| semana | cotizaciones en el sitio | conversiones en Ads | |
|---|---|---|---|
| 25-31 may | **19** | **0** | el sitio recibía, Google no contaba |
| 1-7 jun | 12 | 3,8 | contaba a medias |
| 8-14 jun | **10** | **0** | otra vez cero |
| 15-21 jun | 10 | 9,0 | coherente |
| 22-28 jun | 11 | **46,0** | ahora cuenta de más |
| agosto completo | **58** | **151,5** | **ratio 2,6x** |

**Las conversiones de Ads solo pueden venir de clics en los propios anuncios, así que
tienen que ser MENOS que el total de cotizaciones del sitio. Un ratio > 1 es
sobreconteo, no éxito.**

## Las dos conclusiones que cambian todo

1. **Cuando ella «rompió» la medición, el negocio no cayó.** El sitio siguió recibiendo
   10-19 cotizaciones semanales. **Devolvió un cambio que probablemente estaba bien**,
   porque el único termómetro que tenía era el que estaba roto.
2. **Buena parte de la «caída» de 4,67 → 1,0 conversiones/día que perseguí dos semanas
   es el sobreconteo desinflándose**, no el negocio muriendo. El ratio bajó solo:
   4,2x → 2,3x → 1,9x → 1,0x. Las cotizaciones reales de agosto por semana fueron
   **10 · 14 · 14 · 16**: estables, incluso al alza.

**Se le dijo con todas las letras que esto corrige lo que yo mismo le había
reportado.**

## Lo que SIGUE siendo real

- El **CPC se triplicó** (270 → 900 CLP) y llegan **la mitad de clics** por el mismo
  presupuesto. Eso se mide en clics y en pesos, **no depende del conteo**.
- Es un problema de **eficiencia**, no de demanda.

## La regla operativa

**Antes de afirmarle a Connie que el negocio de Sudtec subió o bajó, mirar las
cotizaciones de WooCommerce (`ywraq-new`), no las conversiones de Ads.** Ads sirve
para juzgar *la campaña* (clics, CPC, gasto); el sitio es el que dice si hay negocio.

**Y ahora sí se puede tocar la medición:** con el termómetro independiente, si Google
baja pero el sitio sigue recibiendo sus 12-16 semanales, se sabe que es el tag y no hay
que revertir. Eso es justo lo que le faltó la vez pasada.

## Dos trampas de datos que aparecieron en el camino

- **`per_page=40` devolvió exactamente 40**: estaba truncado y las semanas «vacías»
  eran artefacto. **Hay que paginar hasta que una página traiga menos que el tope.**
- Se verificó que los 132 pedidos comparados fueran **todos `ywraq-new`** y no otro
  tipo de pedido, antes de usarlos como cifra.

Va con [[contadores-no-son-envios]] y [[ads-hora-chile-woo-utc]].

## Cómo se verificó la fuente (Connie preguntó, msg 686)

Preguntó si las cotizaciones salían **directamente del sitio**. Sí, y así se sostiene:

- **Fuente:** API de WooCommerce de `www.sudtec.cl` como `admin_sudtec` — la misma base
  de datos del panel de WordPress. Endpoint `wc/v3/orders`, filtrado **solo por fecha**.
- **No se filtró por estado**, y se comprobó que la consulta sin filtro devuelve lo
  mismo que `status=any`.
- **`wc/v3/reports/orders/totals` es la prueba definitiva:** la tienda tiene **3.656
  pedidos y TODOS son `ywraq-new`**. Todos los demás estados están en **cero**. Ninguna
  cotización pudo escaparse por haber cambiado de estado.
- **Anti-caché:** el helper agrega `_nc` a cada GET porque LiteSpeed cachea `wp-json`
  (ver [[litespeed-cachea-la-api-rest]]). Sin eso habría leído copias viejas.
- **Paginación:** el primer intento pidió `per_page=40` y devolvió exactamente 40 —
  truncado. Se paginó hasta que una página trajo menos del tope: agosto pasó de 40 a
  **58**.

**Cifra para que ella misma verifique:** agosto completo = **58** solicitudes de
presupuesto en su panel.

## El límite de lo que se puede afirmar

Se cuentan **solicitudes de cotización, no ventas cerradas**. Lo demostrado es que
**la demanda no cayó** (12-16 por semana). Si esas cotizaciones terminaron en venta
está en el proceso comercial de Sudtec, **no es visible desde el sitio** — y se le dijo
así, sin estirar la conclusión.

