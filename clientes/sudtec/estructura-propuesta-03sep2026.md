# Estructura nueva propuesta — Sudtec Google Ads (3-sep-2026)

**Pedido de Connie (msg 667):** crear campañas con grupos por categoría, **todas
PAUSADAS**, para no correr hasta que vuelva del viaje (**18-sep-2026**).
**Corrección suya (msg 668):** ver primero el ejemplo. **Nada creado.**

**Base:** las categorías **reales** de WooCommerce (`wc/v3/products/categories`), no
categorías inventadas. Cada grupo apunta a **su** página de categoría.

## La estructura (3 campañas · 17 grupos)

### 1 · Bomberos — el núcleo (256 productos)

| Grupo | Página de destino |
|---|---|
| Botas | `/product-category/epp/botas/` |
| Cascos | `/product-category/epp/cascos/` |
| Uniformes | `/product-category/epp/uniformes/` |
| Guantes | `/product-category/epp/guantes/` |
| Rescate Vehicular | `/product-category/rescate/rescate-vehicular/` |
| Rescate en Altura | `/product-category/rescate/rescate-en-altura/` |
| Herramientas de Rescate | `/product-category/rescate/herramientas-rescate/` |
| Cámaras Termales | `/product-category/rescate/camaras-termales-rescate/` |
| Estabilización y Cojines | `/product-category/rescate/estabilizacion/` |
| Mangueras | `/product-category/material-de-agua/mangueras-de-combate-incendios/` |
| Pitones | `/product-category/material-de-agua/pitones/` |
| Espuma y CAFS | `/product-category/material-de-agua/cafs/` |

### 2 · Industrial / Hazmat (31 productos)

Rescate Pesado · Descontaminación · Tapa Fugas —
`/product-category/industrial/{rescate-pesado-industrial,descontaminacion,tapa-fugas}/`

### 3 · Forestal (11 productos)

Herramientas Forestales · Botas Forestales —
`/product-category/material-forestal/{herramientas,botas-material-forestal}/`

## Por qué 3 campañas y no una por categoría

Ella pidió «una por categoría». **Se le dijo el costo antes de ejecutar:**

- **El grupo manda la relevancia** (página de destino + tema de keywords). Toda la
  ganancia de ordenar por categoría se obtiene **igual** con 3 campañas que con 8.
- **La campaña manda el presupuesto y el aprendizaje de puja.** La cuenta hace
  **111 conversiones/mes**; el playbook pide **~30 por campaña** para que el smart
  bidding aprenda. Con 8 campañas quedan ~14 cada una: **ninguna aprende.**
- Se separaron solo las dos que tienen **razón de negocio** para presupuesto propio:
  **Industrial/Hazmat** (otro comprador) y **Forestal** (estacional).

**Se le dijo explícitamente que si igual prefiere una por categoría, se hace.**

## Por qué esto ataca el hallazgo crítico de la auditoría

`G24` — experiencia de página **BELOW_AVERAGE** en casi todo el gasto alto, porque
casi todos los anuncios apuntan a `/lista-productos/`. Con un grupo por categoría,
**cada anuncio llega a la página de su producto**. La página entra en el Nivel de
calidad y el Nivel de calidad define el CPC, que se triplicó (270 → 900 CLP).
También cierra `G03` (el grupo `General` como cajón de sastre).

## Bloqueado esperando decisión de Connie

1. **Presupuestos.** No se ponen cifras sin que las confirme, ni en campañas
   pausadas — regla dura de `CLAUDE.md`. Moneda **CLP**, factor **×1** (sin
   centavos): `amount_micros = pesos × 1.000.000`.
2. **¿Anuncios?** Un grupo sin RSA no sirve al activarse. Si dice que sí, se
   redactan con `memory/skills/google-ads/references/rsa-output-spec.md`
   (15 titulares ≤30 caracteres, 4 descripciones ≤90, **contando caracteres, no a ojo**).

## Compromisos dados

- Todo se crea en **PAUSED** y se **verifica por relectura** de la cuenta, no por el
  200 del mutate.
- **No se toca nada de lo que corre hoy.** Es estructura nueva en paralelo.
