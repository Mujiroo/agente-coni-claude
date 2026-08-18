# Sudtec — meta descripciones y alt de productos

*Pedido de Connie el 18-ago-2026 (msg 83). **Auditoría hecha, nada escrito
todavía** — el sitio es producción y espera su OK.*

## El tamaño real del trabajo

Catálogo leído entero por la API de WooCommerce: **307 productos**
(300 publicados, 5 borradores, 1 pendiente, 1 privado).

### Meta descripciones (Rank Math, meta `rank_math_description`)

| | |
|---|---|
| Productos **con** meta description | **127** |
| Productos **sin** meta description | **180** |
| Sin meta **title** (`rank_math_title`) | 258 — *no lo pidió, pero es el mismo trabajo* |

**Con qué material se puede escribir cada uno de los 180:**

- **76** tienen **descripción corta** — es la mejor base, ya está redactada.
- **103** no tienen corta pero **sí descripción larga** con características,
  medidas y normas.
- **1 solo** producto no tiene ningún texto: habría que escribirlo con el nombre
  y la categoría, o preguntarle a Sudtec.

> O sea: **179 de 180 tienen fuente real**. No hay que inventar nada.

### Alt de imágenes (meta `_wp_attachment_image_alt`)

| | |
|---|---|
| Imágenes asociadas a productos | 730 (**658 únicas**) |
| **Imágenes sin alt** | **509 asignaciones · 469 únicas** |
| Productos sin ninguna imagen | 6 |

Los nombres de archivo son **inservibles** para SEO y accesibilidad:
`WhatsApp-Image-2026-02-18-at-17.08.16.jpeg`,
`e494ab29-24b5-4dbe-b0f5-dcc377aaff75-scaled.webp`. Por eso el alt aquí sí
cambia algo real.

## Un dato que apareció de paso

El sitio **tuvo Yoast antes de Rank Math**: quedan 96 `_yoast_wpseo_metadesc` y
otros metas huérfanos. Se revisó si servían para rellenar los que faltan:
**0 productos** sin Rank Math tienen texto de Yoast aprovechable. No hay atajo
por ahí, pero tampoco estorban.

## Cómo se escribirían (criterio propuesto)

**Meta descripciones**
- 140-155 caracteres, con el **nombre del producto** y su **uso real**.
- Sacadas **solo del texto que ya tiene el producto**. **Nada de inventar
  certificaciones, normas ni plazos** — es la misma regla que dejó la auditoría
  de anuncios de agosto, donde aparecieron 3 claims sin respaldo en el sitio.
- La tienda es de **cotización**, no de venta directa: el cierre natural es
  «cotiza», no «compra».

**Alt**
- Describe **lo que se ve**, no una repetición de la keyword.
- Cuando un producto tiene 6 fotos casi iguales, los alt **varían** (producto
  completo, detalle, en uso…). Repetir el mismo texto 6 veces es peor que nada.

## Estado

🟡 **Esperando OK de Connie.** Propuesto: piloto de **5 productos** primero, se
los muestro, y recién con su visto bueno va la tanda completa.

**Vía técnica ya verificada de lectura:** `wc/v3/products` (307 leídos sin
problema). La escritura sería `wc/v3/products/<id>` con `meta_data` para la
descripción, y `wp/v2/media/<id>` con `alt_text` para el alt. **Falta probar la
escritura** — se probará en el piloto, no en masa.
