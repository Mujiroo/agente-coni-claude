# SUDTEC — Volumen real de las keywords del grupo Botas (21-ago-2026)

*Responde la pregunta que Connie hizo el 20-ago (msg 201): «¿verificaste que
tuvieran búsquedas?». La respuesta honesta es que **no**, y ahora se midió.*

## Los números (Planificador, Chile, español)

| Keyword | Búsquedas/mes | Competencia | ¿Está en el grupo? |
|---|---|---|---|
| `botas lytos` | **0** | — | sí ← **la propuse yo** |
| `botas blauer` | **10** | — | sí ← **la propuse yo** |
| `botas jolly` | **10** | LOW | sí |
| `botas bombero` | **260** | HIGH | sí |
| **`botas de bomberos`** | **390** | HIGH | **SÍ** ← *(ver corrección abajo)* |
| `botas haix bomberos` | 210 | MEDIUM | no |
| `botas bombero haix` | 210 | MEDIUM | no |
| `botas bombero forestal` | 70 | HIGH | no |
| `botas para bomberos` | 50 | HIGH | **sí** ← *(ver corrección abajo)* |
| `botas estructurales bomberos` | 50 | MEDIUM | no |

## Lo que esto significa

**Las keywords de marca que propuse no las busca nadie.** El razonamiento del
19-ago fue: *«Lytos son 6 de las 8 botas y no aparece en ninguna keyword de la
cuenta»* — o sea, se validó contra el **catálogo**, no contra la **demanda**.

**Calzar con el catálogo no implica que exista búsqueda.** Connie lo dudó de
inmediato; el dato le dio la razón.

**Y explica el grupo sin impresiones:** si casi todas sus keywords tienen volumen
cero, no hay subasta a la que entrar. No era solo el rechazo del anuncio.

## Propuesto a Connie (msg 275), sin aplicar

1. **Agregar `botas de bomberos`** — 390/mes, la más buscada, y **no está en el
   grupo**.
2. **Pausar `botas lytos`** — 0 búsquedas.
3. **`blauer` y `jolly` en concordancia exacta** — con 10/mes no justifican amplia,
   que gastaría en tráfico que no corresponde.

## 🔎 Hallazgo lateral: HAIX

`botas haix bomberos` (210) + `botas bombero haix` (210) = **420 búsquedas/mes de
una marca que Sudtec NO vende** (el catálogo tiene Lytos, Jolly y Blauer).

Conviene **negativa** para no pagar esos clics — o evaluar traer la marca, pero eso
es decisión comercial de ella.

## La lección

**Validar contra el catálogo y validar contra la demanda son dos cosas distintas.**
Antes de proponer una keyword nueva, mirar su volumen; cuesta una llamada al
Planificador y evita armar un grupo que no puede arrancar.


---

# ⚠️ CORRECCIÓN — 21-ago-2026 05:30

**La columna «¿Está en el grupo?» de arriba estaba mal en dos filas.** Se llenó de
memoria, sin consultar los criterios reales del grupo. Al ir a aplicar los cambios
que Connie aprobó (msg 276) se leyó el grupo `197186444097` y aparecieron **9
keywords**, no las 4 que yo suponía:

| Keyword | Match | Estado | Serving |
|---|---|---|---|
| `botas de bomberos` | PHRASE | ENABLED | ELIGIBLE |
| `botas bombero` | PHRASE | ENABLED | ELIGIBLE |
| `botas para bomberos` | PHRASE | ENABLED | ELIGIBLE |
| `botas para incendios forestales` | PHRASE | ENABLED | ELIGIBLE |
| `botas incendio` | PHRASE | ENABLED | ELIGIBLE |
| `botas seguridad incendio` | PHRASE | ENABLED | RARELY_SERVED |
| `botas jolly` · `botas blauer` · `botas lytos` | PHRASE | ENABLED | ELIGIBLE |

**`botas de bomberos` (390/mes) ya estaba**, activa y elegible. La propuesta 1
(«agregarla») era un **no-op**.

## Y eso tumba la conclusión principal

**«El grupo no arranca porque sus keywords tienen volumen cero» es falso.** Las dos
más buscadas —`botas de bomberos` (390) y `botas bombero` (260)— estaban dentro,
activas y elegibles. El volumen cero de las de marca es real, pero **no** es la
causa.

## La causa real (medida el 21-ago)

1. **La campaña usa `MAXIMIZE_CONVERSIONS`.** El `cpc_bid_micros` de los grupos es
   el mismo default (1.000.000 micros) y **no se usa**: la puja la decide Google.
   La hipótesis «la puja del grupo es baja» está descartada.
2. **La negativa `botas` (broad) que se agregó en el grupo General el 19-ago
   bloquea también las keywords propias de General**: `botas bombero`,
   `bota bomberos` y `botas incendio` — y `botas bombero` era la que traía
   **393 impresiones y 8 conversiones**.
3. **Con Maximize Conversions, el presupuesto va donde hay historial de
   conversión.** El grupo Botas parte en cero, así que recibe muy poco:
   **1 impresión en 7 días**, contra **1.472** de General.

O sea: el tráfico que convertía se sacó de donde convertía y se mandó a un grupo
sin historial, en una campaña que reparte por historial.

## Estado

Aplicado el 21-ago (aprobado por Connie, msg 276): `botas lytos` **pausada**;
`botas blauer` y `botas jolly` pasadas a **exacta** (se quitó el criterio en frase
y se creó uno nuevo — el match type no se puede editar).

**Revertido el 21-ago 05:30, con OK de Connie (msg 281).** Se quitó la negativa
`botas` (id `18320463`) del grupo General. Verificado: no queda ninguna negativa
con «bota» en General, y **`botas bombero` volvió a ENABLED + ELIGIBLE**. El grupo
Botas sigue activo — dejó de bloquear a General, nada más.

No se recomendó esperar: bajo Maximize Conversions el grupo nuevo no iba a
acumular historial sin presupuesto, y sin historial no iba a recibir presupuesto.
La espera solo habría costado más días de la keyword que convertía bloqueada.

**Para cuando Connie vuelva:** si quiere el grupo Botas con vida propia, la vía es
**campaña aparte con presupuesto propio**. Dentro de una campaña con Maximize
Conversions no existe forma de reservarle presupuesto a un grupo. Implica plata
nueva, así que lo decide ella (y ojo con la moneda: CLP, factor ×1).

## La lección, corregida

La de ayer («validar contra el catálogo no es validar contra la demanda») sigue en
pie, pero la de hoy es más básica: **antes de proponer agregar algo, leer lo que ya
está.** Media consulta habría evitado proponer una keyword que llevaba semanas
adentro — y habría evitado la explicación equivocada que se construyó encima.
