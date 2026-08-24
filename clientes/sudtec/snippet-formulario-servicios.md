# SUDTEC — Snippet del formulario de Servicios (APLICADO, snippet id 17)

*Pedido por Connie el 24-ago-2026 (msg 341, con foto): «el landing de servicios
hay un formulario, pero se ve horrible». Aprobado en msg 345.*

## Qué estaba mal (diagnóstico, no impresión)

La página es **`/servicios-sudtec/` (id 6468)** y el formulario es **WPForms Lite,
form 6789**. Cuatro causas concretas:

1. **Columnas con `float`**, el sistema viejo de WPForms: 8 campos con
   `wpforms-one-half` y `wpforms-first`. Cuando una etiqueta ocupa **dos líneas**
   («Nombre o Institución», «Correo electrónico») y la de al lado una, los bloques
   quedan de distinto alto y **los campos se desalinean**. Eso era lo «chueco».
2. **2 de los 10 campos usan `wpforms-field-medium`**, que en WPForms es **60% del
   ancho** → bordes irregulares y espacio muerto al lado.
3. **En móvil nunca colapsaba a una columna**: seguía en dos, apretadísimo.
4. **Etiquetas gris sobre fondo negro**, ilegibles.

Los 10 campos: 8 en media columna (Nombre, Rut, Giro, Dirección, Nº Casa/Of,
Comuna, Teléfono, Correo) + select «¿Qué servicios buscas?» y textarea «Mensaje»,
estos dos a ancho completo.

## Qué hace el snippet

Solo **CSS**, impreso en `wp_head` **únicamente si `is_page( 6468 )`**. No toca el
formulario, ni los campos, ni el correo que llega. **Borrarlo revierte todo.**

- Reemplaza los `float` por **grid de 2 columnas** → filas alineadas
- `display:flex; flex-direction:column` en cada campo + `margin-top:auto` en el
  control: **el input queda pegado abajo**, así calzan aunque la etiqueta ocupe
  distinto alto. Esta es la parte que arregla el problema de fondo.
- Campos al **100%** del ancho, con alto, borde y radio parejos
- Select y textarea a `grid-column:1/-1`
- Etiquetas en blanco; asterisco de obligatorio en `#ff6b6b`
- **`font-size:16px` en los inputs** → evita el zoom automático de iOS al enfocar
- `@media(max-width:767px)` → **una sola columna**

## Selectores verificados en el HTML real

| Cosa | Selector |
|---|---|
| contenedor | `#wpforms-6789` <i>(es un **id**, confirmado)</i> |
| grilla de campos | `.wpforms-field-container` |
| campo | `.wpforms-field` |
| etiqueta | `.wpforms-field-label` |
| botón | `button.wpforms-submit` <i>(queda **fuera** de la grilla, es hermano)</i> |

**Se comprobaron antes de escribir el CSS**, no se asumieron.

## Verificación hecha

- `code_error: null`, activo, scope `front-end`
- El bloque `<style id="kai-form-servicios">` **aparece** en `/servicios-sudtec/`
- **Control de fugas:** **0** apariciones en `/lista-productos/` y `/quienes-somos/`

## ⚠️ Todavía no lo ve el público

Como todo lo demás, LiteSpeed sirve la versión cacheada. Se ve con cualquier
parámetro que fuerce MISS: `https://www.sudtec.cl/servicios-sudtec/?ver=kai`
(enlace de vista previa que se le pasó a Connie en msg 346).

Queda visible con la **purga programada para el 25-ago 04:00**.
