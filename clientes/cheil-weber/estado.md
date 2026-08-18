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

---

# Segunda versión — sobre la base oficial de Cheil (msg 104)

Connie mandó **otra presentación** como base y pidió: *«no quiero que muevas nada,
esa base se tiene que mantener como sea»*.

- **Presentación base:** `1QocZHmeIiSfYK8zsQFqAFGPbeymD4IK3tSqZvGQyOR0`
- **Slide base:** `g3f76204749a_3_67` («Los Pasos del Maestro»)

## Cómo se respetó la base: duplicar, no dibujar

En vez de reconstruir el diseño, se usó **`duplicateObject` sobre la slide base**,
12 veces. Cada copia trae la base **idéntica**: fondo amarillo, grupo de cabecera,
panel blanco inclinado (que es una **imagen**, no una forma) y el pie con «Cheil».

Solo se reemplazó el **texto** de los tres cuadros de la columna izquierda, y se
agregó el detalle **dentro** del panel blanco. **No se movió, redimensionó ni
borró ningún elemento de la base.**

**Verificado después de escribir:** la slide base sigue teniendo sus **5
elementos** y sigue diciendo «Los Pasos del Maestro» / «CONTENIDO RRSS».

## Tres tropiezos de la API, y cómo se resolvieron

1. **`The object ID length should not be less than 5`** — los ids `kw01` eran
   demasiado cortos. Slides exige **5 caracteres o más**.
2. **`The table column width must be at least 406400 EMU`** — una columna de 0,42"
   no pasa. El mínimo es **406400 EMU ≈ 0,44 pulgadas (32 pt)**. Se dejó una red
   de seguridad en el generador que sube cualquier columna por debajo del mínimo.
3. **`The slides should be in presentation order`** — cada `duplicateObject` se
   inserta **justo después** de la slide original, así que al duplicar en orden
   quedan al revés. Solución: **generar los duplicados en orden inverso** y
   olvidarse de `updateSlidesPosition`.

## El error que solo se vio mirando el render

`deleteText` + `insertText` **borra el estilo del texto**: los títulos quedaron en
un cuerpo diminuto en vez del Montserrat 28 bold de la base. La API respondió
**200 en todo**.

Se leyeron los estilos reales de la base y se restituyeron:

| Cuadro | Estilo de la base |
|---|---|
| Título | **Montserrat 28 pt bold**, negro, interlineado 80 |
| Antetítulo | Arial 15 pt, negro, interlineado 80 |
| Bajada | Arial 11 pt, negro, interlineado 100 |

> Es la tercera vez en el día que **«200 OK» no significa «quedó bien»**: pasó con
> LiteSpeed en Sudtec, con la maqueta de la primera versión y ahora con el estilo
> del texto. **Renderizar y mirar** es lo que lo detecta.

## Restricción heredada de la base

Los cuadros de texto de la base son chicos (título 3,06×0,81", bajada 2,79×0,76").
Como **no se pueden agrandar sin mover la base**, el texto de la izquierda se
escribió corto a propósito: antetítulo ~15 caracteres, título en 2 líneas y bajada
de ~120. **El detalle vive dentro del panel blanco.**

Zona segura útil dentro del panel inclinado: **x 3,95" a 9,00" · y 1,32" a 4,07"**.

## Estado

🟢 **Entregado.** La presentación quedó con 14 slides: la original en blanco, la
base intacta, y las 12 nuevas.
