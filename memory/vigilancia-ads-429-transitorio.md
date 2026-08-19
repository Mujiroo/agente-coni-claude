---
name: vigilancia-ads-429-transitorio
description: Un 429 pasajero en la primera consulta de Ads hace que el script grite "estoy ciega" y muestre una proyección falsa; hay que reintentar antes de avisar.
metadata:
  type: project
---

**El 19-ago-2026, en la pasada de las 09:00, `bin/vigilancia_ads.py` salió con
`HAY-QUE-AVISAR` y "🔴 No pude leer la cuenta de Google Ads: 429
RESOURCE_EXHAUSTED".** Al reintentar de inmediato, la misma cuenta respondió
normal y el script dio `OK-SILENCIO`. **Era un 429 pasajero, no una cuota
agotada.**

**Por qué importa el detalle:** el 429 pegó solo en la **primera** consulta (la de
campañas y presupuestos). Las de gasto sí respondieron. Eso deja `presu` vacío, y
con `presu` vacío el script **se salta en silencio** cuatro chequeos: campaña
apagada, presupuesto movido por fuera, gasto anormalmente bajo y proyección sobre
el límite.

**La trampa del número:** con `presu` vacío, `total_dia = 0`, así que
`proyeccion = mtd + restantes*0 = mtd`. En esa corrida imprimió *"proyección
cierre 157042"*, que **no era una proyección** sino el gasto del mes hasta la
fecha. La corrida buena, con datos completos, dio **274.642** contra un límite de
**300.000**. Reportarle a Connie el 157.042 como proyección la habría dejado
mucho más tranquila de lo que corresponde.

**Cómo actuar:** si la alerta es *"no pude leer la cuenta"*, **reintentar antes de
escribirle**. Solo si el segundo intento también falla se le avisa que estoy
ciega. Y nunca pasar las cifras de "contexto" de una corrida que falló: en esa
corrida hay números que no significan lo que dice su etiqueta.

Relacionado: [[contadores-no-son-envios]]
