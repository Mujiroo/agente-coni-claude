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

- **1-sep-2026** — Revisar **si le cobraron Google Workspace** (pedido el
  20-ago, msg 272). Está **también en su Google Calendar** (evento
  `0617vhc3a9d2qujkvtu193r99g`, 10:00 Chile), pero se duplicó por Telegram porque
  durante el viaje no revisa el calendario.
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

**Después precisó la hora: las 22:00 de su noche en China.** Y ahí aparece una
segunda trampa: **Chile entra en horario de verano el 6-sep-2026** (UTC-4 →
UTC-3), justo en medio de las tres fechas. El mismo instante en China cae en una
hora distinta de Chile antes y después:

| Fecha | Hora en Chile | = en China |
|---|---|---|
| 4-sep | **10:00** | 22:00 |
| 11-sep | **11:00** | 22:00 |
| 14-sep | **11:00** | 22:00 |

Por eso los tres crons **no tienen la misma hora**. Verificado con `zoneinfo`, no
a ojo. Si alguien los "empareja", dos avisos llegan una hora antes.

**Dos lecciones, más allá de este viaje:**

1. Al calcular un huso, preguntarse primero **dónde ocurre la tarea**, no solo
   dónde está la persona. Si me lo hubiera preguntado, salía bien a la primera.
2. **Un cron con fecha fija cruzando un cambio de horario no es una hora, son
   dos.** Comprobar el offset **de cada fecha** con `zoneinfo` antes de escribir
   la línea.

**Cada cron se borra a sí mismo** después de avisar, así que no quedan repitiendo
el año que viene.

Relacionado: [[connie]], [[notas-connie]]


## Regla que quedó (20-ago-2026)

**Cuando pida «agrégame algo al calendario» durante el viaje, hacer las dos cosas:**
crear el evento **y** montar el aviso por Telegram.

El calendario solo no le sirve — ella misma dijo que no lo va a revisar, y ese fue
justamente el motivo de montar estos crons. Crear únicamente el evento sería cumplir
la letra del pedido y fallar el objetivo.

**La hora siempre igual: 22:00 de China**, que es cuando en Chile empieza la
jornada. Ojo con el cambio de horario chileno del **6-sep-2026** (UTC-4 → UTC-3):
antes de esa fecha son las **10:00** de Chile, después las **11:00**.
