# SUDTEC — Google Ads

*Auditoría del 17-ago-2026 (datos: últimos 30 días). Solo lectura, nada modificado.*

## La cuenta

- **SUDTEC**, id `9907217991` — `ENABLED`, no es de prueba
- **Moneda: CLP** · huso `America/Santiago`
- Las otras dos cuentas accesibles (`8700413993`, `9625473535`) devuelven
  `CUSTOMER_NOT_ENABLED`: no son de este cliente o están desactivadas.

> **Recordatorio de la regla dura:** CLP no tiene centavos. En la API los montos
> van en **micros**: `amount_micros = CLP × 1.000.000`. Un presupuesto de 9.100
> CLP/día es `9100000000`. Verificar SIEMPRE antes de escribir.

## Presupuesto: el límite del cliente es 300.000 CLP/mes

Google garantiza el tope mensual como **presupuesto diario × 30,4**.

| Campaña | Estado | Diario actual | Techo mensual | Gasto real 30d |
|---|---|---|---|---|
| Campaña Sudtec | ENABLED | 8.000 | 243.200 | **234.527** |
| Competencias | ENABLED | 2.000 | 60.800 | **3.922** |
| **Total** | | **10.000** | **304.000** ⚠️ | **238.449** |

**Dos problemas a la vez:**

1. El techo formal (**304.000**) **excede el límite de 300.000**. No ha explotado
   solo porque Competencias no gasta lo suyo.
2. Aun así quedaron **61.551 CLP sin usar** (20,5%) mientras la campaña buena se
   quedaba sin dinero todos los días.

## El hallazgo principal

**«Campaña Sudtec» toca su tope diario los 14 días seguidos revisados** (8.000 a
9.768 CLP/día, sin excepción).

- Cuota de impresiones: **17,9%**
- Perdida **por presupuesto: 80,5%**
- Perdida por ranking: **1,7%**

Los anuncios ganan las subastas; el dinero se acaba. **A 300.000 CLP/mes esta
cuenta captura menos de un quinto de la demanda que tiene disponible.** Vale la
pena que Connie se lo plantee al cliente: el techo no es la publicidad, es el
presupuesto.

## Rendimiento (30 días)

- **140 conversiones** (formulario de cotización), CPA **1.675 CLP**
- CTR **12,41%** · CPC medio **315 CLP** · 743 clics · 5.989 impresiones
- Móvil 70% del gasto (CPA 1.679) · Escritorio 29% (CPA 1.614) — sin diferencia
  relevante, no hay ajuste por dispositivo que valga la pena
- Tablet: 1.041 CLP, 3 clics, 0 conversiones (irrelevante)

### ⚠️ La medición no cuadra — verificar antes de confiar en la puja

Google reporta **140-143 conversiones**; a la casilla de Connie llegaron **55**
correos `[Solicitud de presupuesto]` de `cg@sudtec.cl` en el mismo período.
**Más del doble de diferencia.**

La acción está en `ONE_PER_CLICK`, así que no es doble conteo por recarga.
Hipótesis a descartar: la conversión dispara en carga de página y no en envío, o
existe un segundo formulario que no notifica a `cg@`.

**Importa porque las dos campañas usan `MAXIMIZE_CONVERSIONS`**: si la señal está
inflada, el sistema está pujando contra un número que no existe. **Esto se aclara
antes de optimizar nada más.**

*(Hay 7 acciones de conversión viejas en `REMOVED`/`HIDDEN`; las dos activas son
«Cotización formulario» —la que registra— y «Formulario de contacto - Enviar»,
que marca 0.)*

## Dónde se va la plata

| Palabra clave | Tipo | Gasto | Conv | CPA |
|---|---|---|---|---|
| equipos de bomberos | BROAD | 90.618 | 60 | **1.510** ✅ |
| equipo de protección personal | BROAD | 43.173 | 19 | **2.272** 🔴 |
| manguera de bomberos | BROAD | 18.206 | 11 | 1.655 |
| botas bombero | BROAD | 16.357 | 8 | 2.044 |
| accesorios bomberos | PHRASE | 9.146 | 2 | **4.573** 🔴 |

`equipo de protección personal` es **18% del gasto** con CPA 36% peor que el
promedio: término genérico que no dice «bomberos».

De 237 términos de búsqueda, **173 no trajeron ninguna conversión** (68.823 CLP,
58% del gasto rastreado). Marcas ajenas sin una sola conversión: **Maryun**
(2.784 CLP), **Holmatro**, **Holik**, **Sicor**. *Pendiente confirmar con Connie
si SUDTEC las vende antes de bloquearlas.*

## Estructura

- **Un solo grupo de anuncios («General») con 39 palabras clave**, mezclando
  botas, mangueras, guantes, cascos y herramientas de rescate bajo el mismo
  anuncio. Separarlo por familia es el cambio de mayor rendimiento cuando no se
  puede subir el presupuesto.
- Anuncios campaña principal: 6 activos — 3 en fuerza **GOOD**, 3 en **AVERAGE**
  (uno con solo 4 títulos de 15 posibles).
- Anuncios de Competencias: los 3 en fuerza **POOR** → explica el 45,8% perdido
  por ranking. Su CPA es **1.307**, mejor que la principal: hay algo bueno
  enterrado bajo anuncios malos.
- Recursos presentes: 22 sitelinks, 5 textos destacados, 4 fragmentos, 31
  imágenes, 2 videos. La cuenta está bien dotada en extensiones.

## Propuesta enviada a Connie (17-ago, msg 19) — PENDIENTE DE SU OK

| Campaña | Diario propuesto | Techo mensual |
|---|---|---|
| Campaña Sudtec | 8.000 → **9.100** | 276.640 |
| Competencias | 2.000 → **700** | 21.280 |
| **Total** | **9.800** | **297.920** ✅ |

Queda **2.080 CLP bajo el límite** y deja de estar por encima. Competencias
conserva 5× lo que realmente gasta.

Orden del resto: (2) recortar `equipo de protección personal`, (3) completar los
anuncios AVERAGE a 15 títulos, (4) separar el grupo «General» por familia de
producto, (5) rehacer los anuncios de Competencias.

## Estado

🟡 **Nada modificado.** Todo lo anterior es lectura. Esperando de Connie:
- OK al reparto de presupuesto
- respuesta sobre el descuadre de medición (140 vs 55)
- si SUDTEC vende Maryun / Holik / Holmatro / Sicor
