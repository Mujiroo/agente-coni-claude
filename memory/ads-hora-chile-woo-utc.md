---
name: ads-hora-chile-woo-utc
description: En el mismo análisis de Sudtec conviven dos zonas horarias — Google Ads ya entrega hora de Chile y WooCommerce entrega UTC; mezclarlas produce conclusiones falsas.
metadata:
  type: reference
---

Cuando cruzo **clics de Google Ads** con **cotizaciones de WooCommerce** —cosa que
hago seguido en Sudtec para ver si el gasto produce solicitudes— estoy juntando dos
fuentes con **convenciones horarias distintas**:

| Fuente | Zona | Qué hacer |
|---|---|---|
| **Google Ads** (`segments.hour`, `segments.date`) | **America/Santiago** | **Nada.** Ya viene en hora de Chile |
| **WooCommerce** (`date_created` de `wc/v3/orders`) | **UTC** | **Restar 4 h** (3 h desde el 6-sep-2026, horario de verano) |

**Verificado el 22-ago-2026** contra la cuenta:

    SELECT customer.id, customer.currency_code, customer.time_zone FROM customer
    -> SUDTEC · CLP · America/Santiago

Lo de Woo se había confirmado antes cruzándolo con la prueba que hizo Connie a las
15:03 de Chile: la API la marcaba `2026-08-20T19:03:03` → UTC−4.

**El riesgo concreto:** si le aplico la resta de 4 horas a los datos de Ads
«para dejarlos en hora de Chile», los corro 4 horas hacia atrás y todo el cruce
queda desalineado. Un pico de clics de las 22:00 aparecería a las 18:00 y parecería
que las cotizaciones nocturnas no vienen de la campaña.

**Al escribir un análisis que mezcle ambas, decir en el texto qué zona está usando
cada cifra.** Así el que lo relea después —yo incluido— no vuelve a dudarlo.

La moneda de la cuenta es **CLP**, que **no tiene centavos**: `cost_micros / 1e6`
da pesos directos y el factor para presupuestos es **×1**, nunca ×100.

Relacionado: [[gasto-cero-con-impresiones]], [[cuota-google-ads]]
