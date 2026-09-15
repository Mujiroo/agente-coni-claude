---
name: ads-sudtec-pausado-15sep
description: Ads de Sudtec estuvo pausado el 15-sep-2026 de 09:24 a 10:31 Chile por el sitio saturado; ya está REACTIVADO. Queda verificar el 16-sep que vuelvan las cotizaciones.
metadata:
  type: project
---

**15-sep-2026.** Sitio con PHP saturado (~50 s) por bots en URLs de filtro YITH → 0 cotizaciones
desde el vie 11. Connie ordenó pausar (msg 1187, 09:24 Chile): **Campaña Sudtec** `22490713380` y
**Competencias** `23598502728`. Su novio arregló el `.htaccess` (msg 1196), el sitio volvió a ~2 s, y
Connie pidió reactivar (msg 1198). **Reactivadas 10:31 Chile, verificado por relectura: ENABLED/SERVING.**
Bomberos, Industrial y Forestal siguen pausadas como antes (no se tocaron).

**Why:** que no quede nadie creyendo que sigue pausado, ni el vigía disparando por eso.

**How to apply:**
- Si `vigilancia_ads.py` o `vigilancia_cambios.py` del 16-sep muestran gasto bajo del 15 o cero
  campañas en la ventana, es por esa hora de pausa: no alarmar.
- **El 16-sep revisar en WooCommerce que hayan vuelto las cotizaciones** (última antes del incidente:
  11648, vie 11-sep 17:43 Chile) y contárselo, como se le prometió en msg 1199. Si siguen en cero con
  el sitio rápido, mirar la regla del `.htaccess` que bloquea `product_cat`+`filter_marca`.

Detalle en `clientes/sudtec/estado.md`. Relacionado: [[bloqueo-bots-htaccess-sudtec]],
[[vigia-mide-la-metrica-rota]], [[cotizaciones-del-sitio-son-el-termometro]]
