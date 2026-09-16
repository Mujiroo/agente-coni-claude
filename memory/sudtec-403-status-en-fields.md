---
name: sudtec-403-status-en-fields
description: En sudtec.cl el WAF del hosting responde 403 si la query lleva `status` dentro de `_fields`; no es la credencial ni el bloqueo de bots.
metadata:
  type: reference
---

**16-sep-2026.** `wc/v3/orders?per_page=100&_fields=id,number,status,date_created_gmt`
devolvió **HTTP 403** con una página HTML genérica del servidor (**1591 bytes**, que
es la firma para reconocerla de lejos).

**Aislado probando parámetro por parámetro:**

| Consulta | Resultado |
|---|---|
| `wc/v3/orders?per_page=100&_fields=id,number,date_created_gmt` | **200** |
| `wc/v3/orders?per_page=10&_fields=id,number,status,date_created_gmt` | **403** |
| `wc/v3/orders?per_page=100&_fields=id,date_created_gmt` | **200** |
| `wc/v3/orders?per_page=10&status=any` | **200** |

**El disparador es la palabra `status` DENTRO de `_fields`.** Como parámetro
suelto (`status=any`) pasa sin problema. Es una regla de WAF del hosting, no de
WordPress.

**Why:** perdí varias llamadas creyendo que era un problema de acceso. Los dos
sospechosos naturales estaban descartados: `estado` daba **administrator** con
`manage_woocommerce`, `diagnostico` daba las **3 respuestas distintas** (o sea la
app password viaja bien, ver [[litespeed-cachea-la-api-rest]]), y el bloqueo de
bots del `.htaccess` solo golpea URLs con `filter_`/`yith_wcan=`
([[bloqueo-bots-htaccess-sudtec]]), que no era el caso.

**How to apply:**
- **No pedir `status` en `_fields`.** Si hace falta el estado, traer el objeto
  completo (sin `_fields`) o filtrar con `status=<valor>` como parámetro.
- Un **403 con HTML de ~1591 bytes** en este sitio = WAF, no credencial. Antes de
  dudar del acceso, quitar parámetros de a uno hasta que pase.
- Casi todas las cotizaciones son `ywraq-new` de todos modos, así que para contarlas
  el `status` rara vez se necesita.

Relacionado: [[sudtec-wp-trunca-salida]], [[ads-403-robot-vs-navegador]]
