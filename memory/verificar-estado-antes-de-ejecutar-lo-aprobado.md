---
name: verificar-estado-antes-de-ejecutar-lo-aprobado
description: Una aprobación de Connie es sobre la intención, no sobre el mecanismo; releer el estado real antes de ejecutar, porque mi propia propuesta puede estar descrita mal.
metadata:
  type: feedback
---

**31-ago-2026.** Le propuse a Connie revertir «accesorios bomberos» *de concordancia
de frase a amplia*. Ella aprobó (msg 600, «Dale nomad»). Al ir a ejecutar, el
`change_event` de Google Ads mostró que **el 19-ago no se pasó a frase**: se
**pausaron amplia y frase** y quedó **solo la exacta**. La restricción era más dura
que la que yo tenía anotada.

**Why:** la aprobación cubría la **intención** (devolverle alcance a esa keyword), y
esa se cumplía igual. Pero si ejecuto a ciegas el mecanismo que yo describí —«pasar
de frase a amplia»— toco el criterio equivocado y dejo la restricción real intacta,
con ella creyendo que quedó revertido.

**How to apply:**

- Antes de ejecutar un cambio aprobado, **releer el estado real del recurso**. Mi
  propia descripción en el chat o en un archivo de estado **no es la fuente**.
- En Google Ads la fuente del pasado es `change_event`. Ojo: `DURING LAST_30_DAYS`
  falla con `START_DATE_TOO_OLD`; hay que pasar fechas explícitas de menos de 30 días.
- Si el estado real difiere de lo aprobado pero **la intención se cumple igual**, se
  ejecuta y **se le cuenta la diferencia en el mismo mensaje**. No se re-pregunta por
  un detalle que no cambia su decisión —sobre todo si es de noche donde ella está—
  ni se esconde para que la propuesta se vea prolija.
- `validateOnly: true` primero, y **verificar por relectura**: el 200 del mutate no
  es prueba de nada.

Relacionado: [[leer-estado-real-antes-de-proponer]], [[congelar-cambios-viaje-china]],
[[contadores-no-son-envios]]
