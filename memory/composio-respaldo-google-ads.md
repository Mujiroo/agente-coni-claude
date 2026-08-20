---
name: composio-respaldo-google-ads
description: Composio llega a Google Ads con cuota independiente de Maton; es el plan B cuando Maton devuelve RESOURCE_EXHAUSTED.
metadata:
  type: feedback
---

**Idea de Connie el 20-ago-2026 (msg 210), verificada y correcta.**

Cuando Maton devuelve `RESOURCE_EXHAUSTED` en Google Ads, **no hay que quedarse
ciego**: Composio tiene el toolkit `googleads` **ACTIVE**, con las **mismas 3
cuentas** (`8700413993`, `9625473535`, `9907217991` = Sudtec).

**La prueba:** se corrió por Composio exactamente la consulta que Maton acababa de
rechazar por cuota. **Pasó.** Las cuotas son **independientes** — developer token
distinto.

**Cómo se usa:**

    COMPOSIO_MULTI_EXECUTE_TOOL → GOOGLEADS_SEARCH_STREAM_GAQL
      { "customer_id": "9907217991", "query": "SELECT ... FROM ..." }

Acepta GAQL igual que Maton. `GOOGLEADS_LIST_ACCESSIBLE_CUSTOMERS` lista cuentas.

**Lo que esto NO cambia:** la cuota de Composio tampoco es infinita, así que sigue
en pie agrupar consultas y guardar el JSON antes de filtrar. Ver
[[cuota-google-ads]]. Para Google en general, **Maton sigue siendo la vía
principal**; Composio es respaldo.

**Detalle útil:** `COMPOSIO_SEARCH_TOOLS` devuelve el estado de conexión de los
toolkits sin el efecto secundario de generar enlaces de autorización, a diferencia
de `COMPOSIO_MANAGE_CONNECTIONS` con `action: add`. Para solo mirar, `action:
"list"` tampoco tiene efecto secundario.
