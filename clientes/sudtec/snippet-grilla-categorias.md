# SUDTEC — Snippet de estilos de la grilla de categorías

*Aplicado el 20-ago-2026 con autorización explícita de Connie (msg 218), ajustado
tras su feedback (msg 220).*

## Qué es

**Code Snippets, snippet id 10**, scope `front-end`, activo:

    KAI · Grilla de categorías de producto (20-ago-2026) — BORRAR ESTE PARA REVERTIR TODO

Es un `add_action('wp_head', ...)` que imprime un `<style id="kai-grilla-categorias">`
**solo si `is_product_taxonomy()`**. No toca base de datos, productos ni plantillas.
**Borrarlo o desactivarlo revierte todo.**

## El dato del tema que explica el problema principal

El sitio usa **Storefront** con la clase de body `right-sidebar`. Storefront
**reserva ~26% del ancho** para `#secondary.widget-area` **aunque esté casi vacía**
—en Sudtec solo tiene un teléfono—, así que `#primary.content-area` iba flotado al
74% y la grilla quedaba **corrida a la izquierda** con una franja blanca al lado.
Eso fue exactamente lo que Connie reclamó.

La corrección, sin borrar el sidebar (pasa a ir debajo):

    #primary.content-area{width:100%!important;float:none!important;margin-right:0!important}
    #secondary.widget-area{width:100%!important;float:none!important;clear:both;margin-top:30px}

Y la grilla centrada, que además centra las filas incompletas:

    ul.products{display:grid!important;justify-content:center;
                grid-template-columns:repeat(auto-fit,minmax(200px,250px))}

## Lo demás que hace

- tarjetas flex de igual alto, con borde y radio
- `aspect-ratio:1/1` + `object-fit:contain` en la foto (marco cuadrado, sin recortar)
- título a 2 líneas con `-webkit-line-clamp`, `min-height:2.7em`
- botón *Agregar a cotizador* con `margin-top:auto` y ancho completo
- 2 columnas en `max-width:767px`
- encabezado de categoría centrado

## Selectores reales del sitio (verificados)

| Cosa | Selector |
|---|---|
| contenedor | `ul.products.columns-4` |
| tarjeta | `li.product` |
| título | `.woocommerce-loop-product__title` |
| botón | `.add-request-quote-button` (YITH, no `add_to_cart`) |
| título categoría | `.woocommerce-products-header__title.page-title` |

## Móvil (pedido de Connie, msg 228)

Verificado pidiendo las páginas con **user-agent de iPhone y de Android**, no
asumido. Ambos snippets llegan al teléfono, con `viewport` presente.

Ajustes propios de pantalla chica en el snippet 10:

- `@media(max-width:767px)` → 2 columnas forzadas
  (`repeat(2,1fr)!important`, porque el `minmax(200px,250px)` del escritorio
  colapsaría a 1 sola columna), `gap:12px`, padding de tarjeta 10px,
  título 13.5px, botón 12.5px
- `@media(max-width:360px)` → `gap:9px`, padding 8px, título 12.5px

**Dato de caché:** LiteSpeed guarda **versiones separadas para móvil**. Hay que
probar con UA de teléfono aparte; verificar solo en escritorio no dice nada del
móvil.

## Verificación hecha

✅ Aparece en `/product-category/uniformes/`, `/epp/botas/` y
`/camaras-termales-rescate/`
✅ **NO** aparece en home, `/contacto-sudtec/`, ficha de producto ni
`/lista-productos/`
✅ `code_error: null`, `active: true`

Se verificó con `?cb=<random>` para saltar la caché de LiteSpeed — **sin eso se lee
una versión vieja y parece que el cambio no entró**.

## Antes y después

Publicado para que Connie lo revise desde el teléfono:
https://claude.ai/code/artifact/e43bd00b-8b71-4b29-b3bc-33e260cb7893

## Cómo crear/editar snippets por API

    python3 bin/sudtec_wp.py api 'code-snippets/v1/snippets?_fields=id,name,scope,active'
    python3 bin/sudtec_wp.py escribir code-snippets/v1/snippets --datos x.json --confirmar
    python3 bin/sudtec_wp.py escribir code-snippets/v1/snippets/10 --datos y.json --confirmar

Campos: `name`, `desc`, `code`, `tags`, `scope`, `active`, `priority`.
**El `code` NO lleva `<?php`.** Para CSS conviene un string PHP en comillas simples
→ **el CSS no puede contener comillas simples**.

---

# Snippet 2 — «Seguir viendo productos» al final de las categorías

*Pedido de Connie el 20-ago-2026 (msg 226): que el visitante sepa que hay más
productos y pueda seguir «vitrineando».*

**Code Snippets, snippet id 11**, scope `front-end`, activo:

    KAI · Seguir viendo productos al final de las categorías (20-ago-2026) — BORRAR ESTE PARA REVERTIR

## Qué hace

Engancha en `woocommerce_after_shop_loop` (prioridad 30) y, solo si
`is_product_taxonomy()`, imprime un bloque con enlaces y un CTA. La lista de
enlaces se elige en cascada:

1. **Subcategorías** del término actual → título *«Explora dentro de X»*
   (ej. `/product-category/rescate/` muestra sus 7 hijas)
2. Si no tiene hijas, **categorías hermanas** → *«También te puede servir»*
   (ej. `/epp/botas/` muestra Uniformes, Cascos, Guantes, Cinturones, Esclavinas)
3. Si tampoco, **categorías principales** → *«Otras categorías»*

Cada chip muestra el **número de productos** de esa categoría. Abajo, un botón
**Ver todo el catálogo** → `/lista-productos/`.

## La decisión de las URL (importante, no cambiarla sin pensar)

Los chips enlazan a **`/product-category/<slug>/`**, NO a
`/lista-productos/?yith_wcan=1&product_cat=<slug>`.

**Por qué:** para el visitante es equivalente, pero las URL de filtro son las que
el `.htaccess` bloquea con 403 a los robots. Llenar el sitio de enlaces internos
hacia ellas le daría a Googlebot **cientos de 403 internos**, con daño en orgánico.
Ver [[bloqueo-bots-htaccess-sudtec]].

Verificado: los 5 chips de la categoría Botas responden **200 a AdsBot**.

El botón grande sí va a `/lista-productos/` (limpia, sin parámetros), que es lo que
Connie pidió.

## Verificación hecha

✅ Botas → *También te puede servir*, 5 chips · Rescate → *Explora dentro de
Rescate*, 7 chips · Cámaras termales → 6 chips
✅ `code_error: null`, sin warnings ni fatals en el HTML
✅ **NO** aparece en home, `/contacto-sudtec/`, ficha de producto ni
`/lista-productos/`

## Detalle que casi se pasa

La primera versión salió **sin tildes** («Tambien», «catalogo», «categorias»)
porque se escribió el PHP evitando acentos por precaución. **Se ve mal en un sitio
de cliente.** El transporte JSON del helper es UTF-8 y los acepta sin problema: se
corrigieron y se verificó en la página pública.
