# Cheil — Weber Chile · deck de campaña digital sobre la base amarilla

*18-ago-2026 (msg 100). Primer trabajo de diseño de slides.*

- **Presentación:** `presentacion weber - campaña digital`
  (`1OyawlnmlAGBRjC8wVVi-nog2qmyTMH5bYuR13JR92-U`)
- **Formato del deck de Cheil:** 10 × 5,625 pulgadas (16:9)

## Qué se hizo

Connie mandó una **captura de la base amarilla de Cheil** y pidió rearmar sobre
ella el contenido de la presentación. Pidió explícitamente **agregar a la misma
presentación** (msg 102).

**Se agregaron 12 slides al final (índices 14 a 25). Las 13 originales quedaron
intactas** — verificado leyendo los `objectId` después de escribir.

| # | Slide | Tipo |
|---|---|---|
| 1 | Portada — Propuesta de Campaña Digital Weber Chile | divisor |
| 2 | Definición de audiencias objetivo | contenido |
| 3 | Estrategia por Canal Digital | divisor |
| 4 | Ecosistema y rol de plataformas | tabla |
| 5 | Integración con retail media | contenido |
| 6 | Plan de Inversión H2 2026 | divisor |
| 7 | Resumen ejecutivo del plan | tabla |
| 8 | Plan de medios: foco 100% digital | tabla |
| 9 | Retail Media | divisor |
| 10 | Plan de ejecución H2 2026 | contenido |
| 11 | Gobernanza: growth técnico estratégico | contenido |
| 12 | Sistema de medición y KPIs | tabla |

## La decisión de diseño que hay que saber

**No se usó la imagen como fondo.** La captura que mandó Connie trae **quemado el
título «Weber nunca me faltes»**; usarla de fondo lo habría repetido en las 12
slides. La base se **reconstruyó de forma nativa**: rectángulo amarillo, cabecera
con su línea, pie con la barra y «Cheil», y el panel blanco inclinado. Todo queda
editable y con el texto seleccionable.

**Dos tratamientos del panel blanco:**

- **Divisores** (portada y las tres separadoras): el **panel inclinado −11°**, tal
  como viene en la base.
- **Slides de contenido**: un **panel blanco horizontal**. Razón: dentro del panel
  inclinado el área rectangular útil se reduce a unas 5,2 × 2,75 pulgadas, y no
  caben las tablas sin achicar la letra a un tamaño ilegible. Se conserva el resto
  de la identidad (amarillo, cabecera, pie, panel blanco). **Está avisado a Connie
  por si prefiere el inclinado en todas.**

## Método: renderizar y mirar, no suponer

La API de Slides tiene `pages/<id>/thumbnail`, que devuelve un PNG del resultado.
Se usó en **tres iteraciones** antes de generar el deck completo:

1. El pie se salía del borde y «Cheil» quedaba cortado.
2. La línea de la cabecera pisaba la palabra «MATTER», y el texto se partía en dos
   líneas.
3. El panel inclinado sobresalía del lienzo.

> **Sin mirar el render, las tres habrían pasado como buenas:** la API responde
> 200 igual. Es el mismo patrón que LiteSpeed en Sudtec — *escribir bien no es lo
> mismo que verse bien*.

## Datos técnicos reutilizables

- `914400` EMU = 1 pulgada. El deck mide `9144000 × 5143500` EMU.
- Rotación: la API usa matriz afín. Para un elemento de `w × h` centrado en
  `(cx, cy)` y girado `θ`:
  `scaleX = scaleY = cos θ`, `shearX = −sin θ`, `shearY = sin θ`,
  `translateX = cx − (cos θ·w/2 − sin θ·h/2)`, `translateY = cy − (sin θ·w/2 + cos θ·h/2)`.
- Paleta usada: amarillo `#FCE84B`, tinta `#242121`, gris `#736E66`, blanco.
  Tipografía **Lato**.
- El constructor quedó en el scratchpad como `deck.py` + `weber.py`. **Si hay que
  repetir esto, conviene moverlo a `bin/`.**

## Estado

🟢 **Entregado.** Pendiente: que Connie revise y diga si quiere el panel inclinado
también en las slides de contenido.
