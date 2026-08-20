# SUDTEC — Fotos de producto: el problema de los collages

*Detectado el 20-ago-2026 (Connie, msg 212: «se ve horrible la página de destino»).*

## Lo que NO es

- **No es el filtro.** Comparadas imagen por imagen, la versión filtrada
  (`/lista-productos/?yith_wcan=1&product_cat=X`) y el archivo de categoría
  (`/product-category/X/`) muestran **exactamente las mismas fotos**. Quitar el
  filtro no empeora el aspecto.
- **No es la grilla ni el recorte.** Los thumbnails ya son cuadrados parejos de
  **324×324**, y ambas plantillas usan Elementor con el mismo sidebar de filtros.

## Lo que SÍ es

Las imágenes cargadas **no son fotos de producto: son collages publicitarios**
(logo + bombero + maletín + cámara en un solo archivo).

Categoría **Cámaras Termales** (`camaras-termales-rescate`, id 311), 5 productos:

| Producto | Imagen | Estado |
|---|---|---|
| FLIR K53 | `K53.jpg` | ✅ foto propia y limpia |
| Cámara Termal FLIR K45 | `adalit4.png` | ❌ collage, **compartido** |
| Cámara termal Flir K-65 NFPA | `adalit4.png` | ❌ collage, **compartido** |
| Cámara Termal FLIR K55 | `adalit4.png` | ❌ collage, **compartido** |
| Cámara termal FLIR K2 TIC con MSX | `Flir-K2-banner.png` | ❌ collage |

**Un mismo archivo (`adalit4.png`) es la foto de tres cámaras distintas.** Por eso
en la grilla se ven tres productos idénticos en fila.

## No hay reemplazo en la biblioteca

Buscado en `wp/v2/media` por `flir`, `k45`, `k55`, `k65`, `k2`. Todo lo que existe:

- `flir` (232×217) y `1200px-flir_logo-svg` → logos
- `flir-renovado` (700×400) → banner
- `flir-k2-banner` y `flir-k2` → **los dos son collages** (se verificaron mirando
  los archivos, no solo el nombre)

**No hay ninguna foto limpia** de K45, K55, K-65 ni K2. Reasignar no arregla nada.

## Los dos caminos (planteados a Connie, msg 213)

1. **Parche:** recortar el collage para aislar la cámara. Queda más limpio, pero
   las tres seguirían compartiendo la misma foto — sigue estando mal.
2. **De raíz:** una foto por modelo, del proveedor o del catálogo de FLIR.

**Estado: esperando que elija. Los sitelinks quedan sin tocar** hasta entonces
(ella pidió «antes de cambiarlo»).

## Lo que sí está bien

La categoría **Botas** (`/product-category/epp/botas/`), que es el destino del
anuncio, tiene **8 productos con foto propia y limpia** cada uno: `botas.webp`,
`1-10.webp` y `FR-1401`…`FR-1406`. Ahí no hay nada que arreglar.

## Cómo revisar esto en otra categoría

    # imágenes que realmente renderiza la grilla, contadas y agrupadas
    curl -sS -L -A 'Mozilla/5.0 Chrome/126.0' "$URL" \
      | grep -oE '(src|data-src)="[^"]*wp-content/uploads[^"]*"' \
      | sed -E 's/.*\/([^\/"]+)"/\1/' | grep 324x324 | sort | uniq -c | sort -rn

Si un archivo aparece más veces de lo esperado, está compartido entre productos.
**Y mirar el archivo, no el nombre:** `Flir-K2.png` suena a foto de producto y es
un collage.

## 5 fotos de producto que ya NO existen en el servidor (20-ago-2026)

Medido pidiendo cada imagen de la grilla con user-agent de navegador:

| Categoría | Producto | Archivo | HTTP |
|---|---|---|---|
| Uniformes | Blauer ARMORSKIN® | `ARMORSKIN®.jpg` | **410 Gone** |
| Uniformes | Blauer ARMORSKIN® Polo Bicolor | `ARMORSKIN®-POLO-BICOLOR.jpg` | 404 |
| Uniformes | Chaqueta de micropolar Blauer | `CHAMARRA-AFELPADA-324x324.jpg` | 404 |
| Uniformes | Polo Bicolor de alto rendimiento | `POLO-BICOLOR-...-324x324.jpg` | 404 |
| Rescate | Arnés Petzl Newton Easyfit Hi-Viz | `SUDTEC-PETZL-...-324x324.jpg` | 404 |

**El navegador muestra el hueco de imagen rota.** Ningún CSS lo arregla: hay que
volver a subir la foto. Avisado a Connie (msg 219).

Dos detalles técnicos:

1. **Las dos ARMORSKIN llevan `®` en el nombre del archivo.** Al pedirlas hay que
   URL-encodear (`%C2%AE`) o da 404 por otra razón distinta a la real.
2. **Esas dos además no son cuadradas**: el `<img>` declara `324x182`, no `324x324`
   — WooCommerce no generó el recorte cuadrado. Con el snippet nuevo eso ya no
   descuadra la grilla (`aspect-ratio:1/1`), pero la foto sigue faltando.

**Cómo medirlo de nuevo:** parsear los `<img class="attachment-woocommerce_thumbnail">`
de la categoría, comparar `width` vs `height`, y pedir cada `src` con HEAD.
