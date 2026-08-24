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

---

## 🔴 24-ago 15:50 — Hallazgo aparte: RUT y Teléfono no se pueden escribir

Revisando la estructura del formulario para responderle a Connie sobre el color,
apareció algo peor que lo estético. **Verificado en el HTML, no supuesto:**

| Campo | Tipo real | Consecuencia |
|---|---|---|
| **Rut** (id 4) | `type="number"` | El navegador **rechaza punto, guión y K**. `12.345.678-K` es imposible de ingresar. |
| **Teléfono** (id 9) | `type="number"` | No acepta `+56 9 …`: el signo y los espacios se bloquean. |
| Nº de Casa/Of (id 10) | `type="number"` | Correcto, ese sí es numérico. |
| Correo (id 1) | `type="email"` | Correcto. |

**Los dos primeros son obligatorios**, así que la persona completa el formulario,
se traba ahí y se va. En el teléfono además le sale teclado numérico.

**Cómo se comprueba:**

```bash
curl -s "https://www.sudtec.cl/servicios-sudtec/?cb=1" \
  | grep -oE '<input[^>]*id="wpforms-6789-field_(4|9)"[^>]*>'
```

**El arreglo NO es CSS ni JS.** Cambiar el `type` en el cliente no sirve: WPForms
**valida el número también en el servidor**, así que el envío se rechazaría igual.
Hay que cambiar el tipo de campo en el constructor, de **Numbers** a **Single Line
Text**.

**No se tocó:** eso altera la configuración del formulario y lo que recibe el
vendedor. Propuesto a Connie en msg 348, **esperando su OK**.

⚠️ **No se le vendió como la causa de la sequía de cotizaciones** — no hay dato de
desde cuándo está así, y hoy ya se cometió el error de afirmar un mecanismo sin
probar el último eslabón ([[litespeed-nonce-vencido-sudtec]]).

## Opinión de diseño que se le dio (msg 348)

- **Mantener el fondo negro:** coherente con el rubro y diferencia de la
  competencia, que va en blanco y azul.
- **Suavizar los campos:** blanco puro sobre negro es contraste máximo; los
  inputs se leen como agujeros y se llevan la atención.
- **Propuesto:** envolver el formulario en una **tarjeta** apenas más clara que el
  fondo, con borde sutil, para que se lea como un bloque.
- Hay una **foto de fondo casi invisible** tras el negro: subirla o sacarla.

---

## ✅ 24-ago 15:55 — Aplicados los dos cambios (Connie: «si porfavor», msg 349)

### A) Tipos de campo corregidos en el formulario 6789

**Cambio real en la definición del formulario**, no CSS:

| Campo | Antes | Ahora |
|---|---|---|
| **Rut** (id 4) | `number` | **`text`** |
| **Teléfono** (id 9) | `number` | **`text`** |
| Nº de Casa/Of (id 10) | `number` | `number` <i>(sin tocar, ahí corresponde)</i> |

**Respaldo previo:** `clientes/sudtec/respaldos/wpforms-6789-antes-24ago2026.json`
(3.610 bytes, la definición completa). Revertir = volver a poner ese
`post_content` en el post 6789.

**Cómo se hizo:** WPForms **no está expuesto en REST** (`wp/v2/wpforms/6789` da 404
y `wp/v2/types/wpforms` da 403). Se creó un snippet temporal con una ruta
admin-only que lee y escribe el `post_content` del post 6789 (JSON de WPForms), se
usó, **y se borró en el mismo turno**.

Las claves del campo (`id, type, label, description, required, size, placeholder,
default_value, css, connect_to`) son **las mismas** para `number` y `text`, por eso
el cambio es limpio y no deja campos huérfanos.

**Verificado en la página pública:** `type="text"` en los dos.

### B) La tarjeta (respuesta a «¿se ve bien el fondo negro?»)

Se mantuvo el negro y se atacó lo que de verdad molestaba:

- `#wpforms-6789` pasa a ser **tarjeta**: fondo `#15161a`, borde `#2c2f37`,
  radio 14px, sombra, `max-width:760px` centrado
- Inputs de blanco puro a **`#f4f5f7`** con borde `#3a3e47` → dejan de leerse como
  agujeros; en foco vuelven a blanco con halo celeste
- Etiquetas `#f2f3f5`, asterisco `#ff7a7a`, placeholders `#8b9098`
- En móvil, padding reducido y una sola columna

## ⚠️ Lo que queda pendiente de verificación

**No se probó un envío real.** Se cambió el tipo de dos campos, y lo único que
prueba que el correo sigue llegando es **mandar el formulario** — cosa que crearía
una consulta falsa al vendedor de Sudtec. **Se le pidió a Connie que haga el envío
de prueba** (msg 350) con su RUT y teléfono reales.

## Cabos sueltos

Snippets **16** y **18** (temporales) quedaron **inactivos y con el código
vaciado**; sus endpoints dan 404. La API responde `rest_cannot_delete` al borrar el
registro. Pedido a Connie borrarlos desde el panel.
