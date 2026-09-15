---
name: ads-sudtec-pausado-15sep
description: Desde el 15-sep-2026 09:24 Chile las 2 campañas de Sudtec están PAUSADAS por orden de Connie (sitio con PHP saturado); las alertas de gasto cero y sequía del vigía son esperables.
metadata:
  type: project
---

**15-sep-2026, 09:24 Chile.** Connie ordenó *«Pausa ads por el momento»* (msg 1187) después
de la alerta de sequía + sitio lento (msg 1186). Pausadas **Campaña Sudtec** `22490713380` y
**Competencias** `23598502728`. Detalle en `clientes/sudtec/estado.md`.

**Why:** el formulario de cotización pasaba por un PHP que tardaba ~50 s; se pagaban clics que
no podían cotizar.

**How to apply:**
- Mientras siga pausado, `vigilancia_ads.py` va a dar **HAY-QUE-AVISAR por gasto de ayer en
  cero** (y probablemente sequía). **Es la pausa, no una falla**: no reenviarlo como alarma.
  Si hay que decirle algo, una línea recordando que está pausado a pedido suyo, y cómo va el sitio.
- **No reactivar sin su «reactiva ads»**, y antes de reactivar verificar que PHP responda.
- Reactivar solo esas dos campañas, no las tres que ya estaban pausadas antes.

Relacionado: [[congelar-cambios-viaje-china]], [[vigia-mide-la-metrica-rota]], [[bloqueo-bots-htaccess-sudtec]]
