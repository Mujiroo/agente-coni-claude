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

**La hora, que es donde me equivoqué y vale la pena tenerlo claro:**

Mis crons corren en **America/Santiago** y ella está en **China (UTC+8)**: 12
horas de diferencia. Mi primer supuesto fue avisarle en **su** mañana —21:00 de
Chile del día anterior— porque di por hecho que las tareas eran suyas, para hacer
donde estuviera.

**Estaba mal, y ella lo corrigió:** *«quiero que sea noche en China para que en
Chile recién esté comenzando la jornada de esa fecha»*. La razón es que **las
tareas se ejecutan en Chile** —el banco, la boleta, la farmacia, Integramédica—,
no donde ella esté. Le sirve el aviso cuando **abre el día chileno**, aunque a
ella le llegue de noche.

**Queda entonces simple: 09:00 hora de Chile, en la fecha exacta de la tarea.**
09:00 en Chile = 21:00 en China del mismo día. Sin fechas corridas.

**La lección, más allá de este viaje:** al calcular un huso hay que preguntarse
primero **dónde ocurre la tarea**, no solo dónde está la persona. Si me hubiera
hecho esa pregunta, el desfase salía bien a la primera.

**Cada cron se borra a sí mismo** después de avisar, así que no quedan repitiendo
el año que viene.

Relacionado: [[connie]], [[notas-connie]]
