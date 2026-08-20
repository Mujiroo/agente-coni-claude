# SUDTEC — Por qué las categorías de producto se ven pobres

*Pedido de Connie el 20-ago-2026 (msgs 212 y 214). Ojo: me equivoqué dos veces
antes de dar con esto — ver «Lo que NO era» abajo.*

## La causa

**No existe plantilla de Elementor para el archivo de productos.** Las plantillas
del Theme Builder son (leídas por `wp/v2/elementor_library?context=edit`):

| id | Nombre | `_elementor_template_type` |
|---|---|---|
| 11274 | Cotizador | page |
| 11270 | Categorias | **section** (no es el archivo) |
| 11264 / 11261 / 11258 / 8383 | Contacto, Servicios, Quiénes somos, Blog | page |
| 9429 | productfix | loop-item |
| 9111 | entrada de blog | single-post |
| 7504 | Buscador | search-results |
| 7226 | Prod unico | product |
| 6279 / 2768 / 2385 | Home, kits | section / kit |

**Falta el tipo `product-archive`.** Sin él, `/product-category/<slug>/` cae en el
layout por defecto de WooCommerce: título suelto, `woocommerce-ordering`,
`woocommerce-result-count` y la grilla `columns-4` pelada. El resto del sitio está
diseñado; las categorías no.

⚠️ **La plantilla llamada «Categorias» (11270) despista: es de tipo `section`** —
un bloque de tarjetas CTA para una landing, no el archivo. Y sus enlaces apuntan a
`?yith_wcan=1&product_cat=...`, o sea **más URLs del patrón bloqueado**
(ver [[bloqueo-bots-htaccess-sudtec]] y `ads-403-destino.md`).

## Lo que NO era (dos diagnósticos míos equivocados)

1. **«Es el filtro».** No: la versión filtrada y el archivo muestran **las mismas
   fotos** y estructura casi igual (breadcrumbs, filtros YITH, orden, 4 columnas).
2. **«Son las fotos».** Hay un problema real de fotos —tres cámaras comparten un
   collage, ver `imagenes-productos.md`— pero **no es lo que ella preguntaba**. Me
   lo aclaró en el msg 214.

**Lección:** cuando dice «se ve mal», preguntar qué parte antes de invertir en
diagnosticar. Dos rondas se fueron en adivinar.

## Lo que se puede hacer desde la API (y lo que no)

🔴 **Crear la plantilla de archivo: NO.** Se arma en el **Theme Builder de
Elementor Pro**, editor visual. Escribir `_elementor_data` a mano para una
plantilla nueva —más sus condiciones de visualización— es a ciegas y sobre
producción. **Se dice así, no se promete.**

✅ **Estilos: SÍ, y de forma reversible.** El sitio expone
`code-snippets/v1/snippets` (plugin **Code Snippets** activo) y se puede leer y
crear. Un snippet de CSS se **desactiva en un click** si no gusta.

Mejoras concretas ofrecidas (msg 215):
- tarjetas de igual alto (hoy se desalinean)
- marco parejo para las fotos
- títulos y botones alineados a la misma altura
- aire entre productos y arreglo en móvil
- título de categoría con el estilo oscuro del resto del sitio

**Compromiso: preparar, mandar captura, y aplicar solo si le gusta.**

## Estado

🟡 Esperando que Connie elija: estilos ahora, o plantilla de verdad en Elementor
cuando vuelva del viaje (regresa el **18-sep-2026**).

## Cómo leer una plantilla de Elementor por API

    python3 bin/sudtec_wp.py api 'wp/v2/elementor_library/<id>?context=edit&_fields=id,meta'

**`context=edit` es la clave:** sin él, `meta` viene **vacío** y parece que no se
puede leer. Con él aparecen `_elementor_data` y `_elementor_template_type`.
