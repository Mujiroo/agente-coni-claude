---
name: hora-de-connie-no-la-mia
description: El puente marca hora de Chile, pero Connie vive en hora de China; antes de juzgar si algo es urgente hay que convertir — y el desfase cambio de +12 a +11 el 6-sep-2026.
metadata:
  type: feedback
---

**26-ago-2026, y por poco cambia la respuesta entera.** Connie pidió ayuda para
tomar un tren. Su pasaje decía **«jue 27 ago, 9:52»** y el evento del puente
llegó marcado **19:44**. Leído así parecía *mañana*, con toda la noche por delante.

**Pero las 19:44 son hora de Chile, y ella vive en hora de China: +12.** Para ella
eran las **07:44 del jueves 27** — el tren salía en **dos horas**. La respuesta
correcta no era una guía tranquila, era *«parte a moverte ahora»*.

**La regla:** el puente sella los eventos en **America/Santiago**, mi zona, no la
suya. **Antes de evaluar si algo corre o espera, convertir a la hora de ella.**
Mientras esté en China: **hora de Chile + 12 = hora de Connie**, y muchas veces
también **+1 día**.

Esto vale para todo lo del viaje, no solo trenes: una hora médica, un cierre
bancario, un vuelo, un «¿alcanzo a…?». **Si la fecha del documento no coincide con
el día que yo creo que es, la equivocada es mi hora, no la suya.**

## ⚠️ El desfase NO es fijo: cambió a +11 el 6-sep-2026

**Chile entró en horario de verano el 6-sep-2026** (UTC-4 → UTC-3). Desde ese día
la cuenta es **hora de Chile + 11**, no +12. Verificado el 8-sep con `date` del
contenedor: **07:15 en Chile = 18:15 en Shanghái.**

**Nunca sumar el desfase de memoria.** La orden barata es
`TZ=Asia/Shanghai date`, y esa es la respuesta correcta siempre — un número
memorizado envejece con cada cambio de horario de verano, en cualquiera de los dos
países.

Los crons del viaje **ya estaban bien** (11:00 Chile = 22:00 China), porque se
calcularon con `zoneinfo` y no a ojo. Revisado el 8-sep, no hubo que tocar nada.
**Lo que estaba mal era esta memoria, no el sistema:** un dato correcto guardado sin
su fecha de vencimiento es una trampa a futuro.

Vuelve el **18-sep-2026**; después de eso vuelven a compartir zona horaria y esta
regla se apaga sola.

Relacionado: [[recordatorios-viaje-connie]], [[ads-hora-chile-woo-utc]], [[connie]]
