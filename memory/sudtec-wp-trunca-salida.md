---
name: sudtec-wp-trunca-salida
description: bin/sudtec_wp.py corta la salida en 6.000 caracteres por defecto; sin --limite los listados largos llegan truncados y los conteos salen mal.
metadata:
  type: reference
---

**`bin/sudtec_wp.py` tiene `--limite` con valor por defecto 6000** y aplica ese
corte al JSON que imprime (`json.dumps(...)[:a.limite]`, línea 165).

**El 22-ago-2026 conté cotizaciones sobre un JSON truncado sin darme cuenta.** El
síntoma fue confuso: `json.load` reventó con
`Invalid control character at: line 306 column 8 (char 6000)` — ese **char 6000**
era la pista, pero primero lo atribuí al contenido. Después, al pedir 3 páginas de
100 pedidos, **las tres devolvieron exactamente 6001 bytes**, que es la señal
inequívoca.

**Regla: en cualquier listado largo, pasar `--limite` alto.**

    python3 bin/sudtec_wp.py api 'wc/v3/orders?per_page=100&page=1&...' --limite 900000

**Dos señales de que estás mirando datos cortados:**

1. Varias respuestas distintas con **el mismo tamaño exacto** en bytes.
2. Un error de JSON que cae **justo en el carácter 6000**.

**Por qué importa más de lo que parece:** un conteo sobre datos truncados **no da
error**, da un número menor y creíble. Si no me hubiera fijado, le habría reportado
a Connie una línea base de cotizaciones equivocada y habríamos decidido sobre ella.

Relacionado: [[ads-hora-chile-woo-utc]], [[leer-estado-real-antes-de-proponer]]
