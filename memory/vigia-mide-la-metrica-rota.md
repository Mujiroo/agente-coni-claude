---
name: vigia-mide-la-metrica-rota
description: vigilancia_cambios.py dispara HAY-QUE-AVISAR contando conversiones de Google Ads, que es justo el contador roto; antes de alarmar hay que cruzarlo con las cotizaciones reales del sitio.
metadata:
  type: project
---

**8-sep-2026.** El cron de las 09:30 dio **HAY-QUE-AVISAR**: *«17 días seguidos peor,
2,3 conversiones/día contra 4,7 de base, CPA 4.897 contra 1.675»*. Leído tal cual, eso
se reenvía como emergencia.

**No se reenvió. Se cruzó primero contra WooCommerce, y el veredicto se dio vuelta.**

| Fuente | Dice |
|---|---|
| Vigía (conversiones de Ads) | 🔴 17 días de derrumbe |
| **Cotizaciones reales del sitio, 7 días** | 12 → **1,71/día** |
| **Cotizaciones reales, 14 días** | 27 → **1,93/día** |
| **Línea base histórica** (300 pedidos, 165 días) | **1,8/día** |

**Está exactamente en su promedio de siempre.** El negocio no cayó.

## Por qué el vigía se equivoca por diseño

**`bin/vigilancia_cambios.py` mide conversiones de Google Ads**, y ese contador es el que
ya sabemos roto ([[cotizaciones-del-sitio-son-el-termometro]]): venía **inflado 2,6x** y
lo que el vigía lee como caída es **el sobreconteo desinflándose**, no ventas perdidas.

**El vigía va a seguir dando rojo mientras el desinfle continúe**, y cada vez va a
parecer que empeora. **No es un bug del script: es que mide la métrica equivocada.**

## La regla

**Antes de reenviarle una alarma de Ads, cruzarla con las cotizaciones de WooCommerce.**
Son dos minutos ([[linea-base-cotizaciones]] tiene el comando y la línea base por día de
la semana) y es la diferencia entre avisarle de un incendio real y arruinarle el día con
un número roto — estando de viaje y embarazada, encima.

**Y avisar igual, no callarse:** se le mandó la alarma **con la corrección al lado**, no
en vez de. Un cron que dispara y un agente que no dice nada se ve idéntico a un agente
caído.

**PROPUESTO y pendiente de su OK (msg 956):** cambiar el vigía para que mida cotizaciones
del sitio en lugar del contador de Ads. **Nada tocado** — ni las campañas
([[congelar-cambios-viaje-china]]) ni el script.

Relacionado: [[contadores-no-son-envios]], [[gasto-cero-con-impresiones]],
[[vigilancia-ads-429-transitorio]]
