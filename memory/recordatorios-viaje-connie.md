---
name: recordatorios-viaje-connie
description: Connie viaja el 21-ago-2026 y me pidió avisarle sus tareas por chat; la trampa es el desfase horario, no las fechas.
metadata:
  type: project
---

**El 19-ago-2026 Connie pidió que yo le avise de sus tareas con fecha, porque
viaja el 21-ago y no va a revisar el calendario.** Los avisos van por Telegram y
están montados como crons en `crons/jobs.txt`.

**Las tres tareas** salieron de su Google Calendar primario (leído, no supuesto):

- **4-sep-2026** — Depósito a plazo
- **11-sep-2026** — Boleta Sudtec
- **14-sep-2026** — Pedir hora eco en Integramédica

**La trampa, y es la parte importante:** mis crons corren en **America/Santiago**
y ella va a estar en **China (UTC+8)**. Son **12 horas de diferencia**. Un aviso
a las 09:00 de Chile le llega a las **21:00** de su día — inútil para una tarea
que hay que hacer esa jornada.

Por eso los crons están **corridos un día hacia atrás a propósito**: disparan a
las **21:00 de Chile del día anterior**, que son las 09:00 de China del día de la
tarea. Si alguien mira `jobs.txt` y ve fechas que no cuadran, **no es un error**;
está explicado en el comentario del archivo.

**Dos cosas sin confirmar** (preguntadas el 19-ago, ojo al leer esto):

1. **Su calendario primario se llama «VIAJE TOKYO»**, pero ella dijo China. Si en
   realidad es Japón (UTC+9), el disparo correcto son las **20:00 de Chile**, no
   las 21:00. Una hora de diferencia.
2. **No sé la fecha de vuelta.** Mientras no la sepa, todo aviso posterior a
   septiembre queda con el mismo supuesto de huso.

**Cada cron se borra a sí mismo** después de avisar, así que no quedan repitiendo
el año que viene.

Relacionado: [[connie]], [[notas-connie]]
