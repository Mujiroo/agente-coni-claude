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
