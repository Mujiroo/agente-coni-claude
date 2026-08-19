---
name: recordatorios-viaje-connie
description: Connie viaja el 21-ago-2026 y me pidió avisarle sus tareas por chat; la trampa es el desfase horario, no las fechas.
metadata:
  type: project
---

**El 19-ago-2026 Connie pidió que yo le avise de sus tareas con fecha, porque
viaja el 21-ago y no va a revisar el calendario.** Los avisos van por Telegram y
están montados como crons en `crons/jobs.txt`.

**Las tareas** salieron de su Google Calendar primario y ella misma detalló cada
una por chat el 19-ago (msg 153):

- **4-sep-2026** — Le **depositan** el depósito a plazo. Tiene que **volver a
  depositarlo**, dejando **200.000 sin depositar**.
- **11-sep-2026** — **Enviar la boleta de Sudtec.**
- **14-sep-2026** — Dos cosas: **Nico** va a buscar el medicamento **Eutirox**, y
  ella **pide hora para la eco** en Integramédica.

**La trampa, y es la parte importante:** mis crons corren en **America/Santiago**
y ella va a estar en **China (UTC+8)**. Son **12 horas de diferencia**. Un aviso
a las 09:00 de Chile le llega a las **21:00** de su día — inútil para una tarea
que hay que hacer esa jornada.

Por eso los crons están **corridos un día hacia atrás a propósito**: disparan a
las **21:00 de Chile del día anterior**, que son las 09:00 de China del día de la
tarea. Si alguien mira `jobs.txt` y ve fechas que no cuadran, **no es un error**;
está explicado en el comentario del archivo.

**Resuelto:** es **China**, lo confirmó ella el 19-ago. El calendario se llama
«VIAJE TOKYO» pero ese nombre está viejo — **no fiarse del nombre del
calendario**.

**Sobre cómo lo pidió:** escribió *«avísame en la noche para que en Chile sea de
mañana»*, con los países cambiados de lugar. Lo que quiere es evidente por el
sentido del encargo —recibir el aviso **en su mañana**— y así quedó: 21:00 de
Chile (noche acá) = 09:00 en China. Se lo confirmé con las dos horas explícitas
para que pudiera corregirme si me equivocaba.

**Sigue pendiente: la fecha de vuelta.** Mientras no la sepa, cualquier aviso
posterior mantiene el huso de China.

**Cada cron se borra a sí mismo** después de avisar, así que no quedan repitiendo
el año que viene.

Relacionado: [[connie]], [[notas-connie]]
