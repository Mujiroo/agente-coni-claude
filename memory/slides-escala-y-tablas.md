---
name: slides-escala-y-tablas
description: En Google Slides las formas se normalizan a una base de 3,28" y el tamaño vive en scaleX/scaleY; y las tablas crecen solas más allá del alto que uno pide.
metadata:
  type: reference
---

**Dos trampas de la API de Google Slides que ya costaron rehacer diapositivas**
(19-ago-2026, armando el comparativo Kai vs Windsor.ai).

**1 · Las formas no guardan el tamaño que uno pidió.** Al crear una forma con
`createShape` y un `size` de, digamos, 0,055 × 3,34 pulgadas, Slides la guarda
como **3,28 × 3,28 pulgadas** y expresa el tamaño real en el `transform`
(`scaleX ≈ 0,0168`, `scaleY ≈ 1,018`).

Consecuencia: **`updatePageElementTransform` con `applyMode: ABSOLUTE` y
`scaleX: 1` no deja la forma como estaba — la infla a 3,28 pulgadas.** Así
convertí dos barras finas de acento en dos bloques de color gigantes que taparon
media diapositiva. Si hay que reescalar, primero se lee el `size` real del
elemento y se calcula `scale = medida_deseada / size_base`.

Lo más simple es **no reescalar**: crear la forma con la medida correcta de una
y, si quedó mal, borrarla y crearla de nuevo.

**2 · Las tablas crecen solas.** El `height` que se le pasa a `createTable` es un
piso, no un techo: cada fila se estira para caber su contenido. Una tabla de 11
filas a 9 pt pidiendo 2,62" terminó midiendo 3,85" y se salió de la diapositiva.
A 8 pt con `spaceAbove`/`spaceBelow` en 0 cada fila queda en ~0,30", que sí se
puede presupuestar.

**3 · Los `objectId` deben tener 5 caracteres o más.** `s01` y `r001` dan
`400 INVALID_ARGUMENT`.

**Cómo verificar sin ojos:** exportar a PDF no sirve si no hay `poppler-utils`.
Lo que sí funciona es pedir la miniatura de cada página y **mirarla**:

```bash
bash bin/maton.sh 'google-slides/v1/presentations/<id>/pages/<pageId>/thumbnail?thumbnailProperties.thumbnailSize=LARGE'
# devuelve contentUrl -> curl -o slide.png "<url>" -> herramienta Read
```

Sin ese paso no hay forma de saber que un texto se desbordó: la API responde
**200 igual**. Relacionado: [[maton-google-slides]], [[contadores-no-son-envios]]
