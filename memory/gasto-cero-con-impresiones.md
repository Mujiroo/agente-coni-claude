---
name: gasto-cero-con-impresiones
description: En Google Ads, gasto en cero con impresiones > 0 NO significa que la campaña dejó de mostrarse; en CPC se paga por clic, así que puede ser simplemente cero clics.
metadata:
  type: feedback
---

**El 21-ago-2026 le reporté a Connie que la campaña de Sudtec «se quedó sin plata
cerca de las 17:00 y **dejó de mostrarse**, última impresión 17:00».** La primera
mitad era cierta; **la segunda era falsa**, y tuve que corregirla al día siguiente
cuando ella cruzó los datos por su cuenta y preguntó cómo entonces habían llegado
cotizaciones a las 22:00.

El desglose real por hora del 21-ago mostraba **17 impresiones entre las 17:00 y
las 23:00**. La campaña siguió apareciendo toda la tarde. Lo que se detuvo fue el
**gasto**, no la exhibición: no hubo ni un clic en esas 7 horas.

**El error de razonamiento:** miré la columna de gasto, la vi en cero desde las
17:00 y deduje que no había exhibición. Pero en un modelo **CPC se paga por clic**,
así que **gasto = 0 con impresiones > 0 es perfectamente normal** — significa que
se mostró y nadie hizo clic.

**Regla:** impresiones y gasto son dos señales distintas y hay que leerlas por
separado.

| Impr | Gasto | Qué significa |
|---|---|---|
| 0 | 0 | Ahí sí dejó de mostrarse (presupuesto agotado, pausada, sin demanda) |
| > 0 | 0 | Se mostró, nadie hizo clic. **No es una avería.** |
| > 0 | > 0 | Operación normal |

**Por qué importa más de lo que parece:** «dejó de mostrarse» es una afirmación
sobre el alcance de la campaña, y ella toma decisiones de presupuesto con eso.
Decirlo mal la empuja a subir plata para arreglar algo que no estaba roto.

**Antes de afirmar que una campaña dejó de mostrarse, pedir explícitamente
`metrics.impressions` por hora y mirarlo.** No inferirlo del gasto.

Relacionado: [[ads-hora-chile-woo-utc]], [[skill-google-ads]], [[leer-estado-real-antes-de-proponer]]
