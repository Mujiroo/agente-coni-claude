# Colombia / NIVEA — Keywords de categoría BODY («NIVEA vs All»)

*Pedido el 20-ago-2026 (msgs 243-244). Entregado en planilla.*

## El encargo real

Viene de un WhatsApp de **Alex Sabogal, PM Lead de Andean** a **Pato**:

- Van a encender la campaña **«Nivea Vs All»** en **Colombia**
- Es de **cremas corporales** de NIVEA
- Van contra su **competidor #1: Lubriderm**
- Iniciativa de **TikTok + Search**
- Piden *«las keywords más relevantes para body en Nivea»* para setear la campaña

## Entregable

Planilla: **NIVEA vs All · Colombia — Keywords BODY (ago 2026)**
`1nstuPCSbtuK7eK6iDqVR3Wm8Cr_SBK1IEYSWzeVdueo`
(ella primero mandó un Doc y luego pidió trabajarlo en Sheets)

- **Pestaña «Lectura estratégica»** — el análisis
- **Pestaña «Keywords»** — 255 términos con métricas, con filtro y mapa de calor

## Fuente de los datos

**Planificador de Palabras Clave de Google Ads**, vía Maton:

    google-ads/v23/customers/9907217991:generateKeywordIdeas
    geoTargetConstants/2170 (Colombia) · languageConstants/1003 (español)

Tres llamadas con semillas de categoría, marca/competidor y necesidad →
**15.477 keywords** con volumen → filtradas a **12.048 relevantes a body** →
curadas a **255** por grupo.

⚠️ **El filtro importa:** las semillas de «crema hidratante» traen mucho de
**rostro**, que no es el encargo. Se excluyó cara, facial, rostro, capilar,
desodorante, solar, etc.

## 🔑 El hallazgo

**La categoría en Colombia se busca por MARCA, no por genérico.**

| Término | Búsquedas/mes |
|---|---|
| lubriderm | **22.200** |
| lubriderm tapa dorada | **12.100** |
| nivea | 9.900 |
| crema nivea | 9.900 |
| lactovit crema | 9.900 |
| cerave crema hidratante | 8.100 |
| **crema corporal** (genérico) | **2.400** |
| crema para el cuerpo | 1.000 |
| hidratante corporal | 140 |

**Lubriderm solo tiene ~9× el volumen del genérico principal.** Armar la campaña
sobre genéricos deja fuera la mayor parte de la demanda.

**Y no es un solo rival:** Lactovit (9.900) y CeraVe (8.100) pesan casi como
Lubriderm. El brief nombra solo a Lubriderm.

## Grupos entregados

`1. Lubriderm` (conquista) · `2. Marca NIVEA` (defensa) · `3. Otros competidores` ·
`0. Categoría corporal` · `4. Necesidad/problema` · `5. Transaccional` ·
`6. Informacional (SEO)`

Las **informacionales van marcadas como NO aptas para Search pagado**: son para
contenido y guiones de TikTok.

## Advertencia que quedó en la planilla

Se puede **pujar** por `lubriderm` como keyword, pero **la marca ajena no puede
aparecer en el texto del anuncio**. Google acepta la puja y rechaza el copy.

## Semrush

**No está conectado y no se puede consultar.** Haría falta una credencial de API
de Semrush (la pone Nicolás).

Se le explicó el matiz: para **volumen**, el Planificador de Google es la fuente
original —Semrush estima a partir de datos como estos—. Lo que Semrush sí daría y
aquí no hay: **dificultad de posicionamiento, backlinks y qué rankea hoy cada
competidor**. Quedó preguntado si lo pide.

## Para repetirlo en otro país

Cambiar solo el `geoTargetConstant`: Chile 2152 · Colombia 2170 · México 2484 ·
Perú 2604 · Ecuador 2218 · Guatemala 2320.


## Formato (pedido en msg 246: «se ve muy desordenado»)

**Aprendizaje:** escribir los datos no es entregar. Un volcado de `values.update`
sin formato se lee como desorden aunque el contenido sea bueno. **El formato va en
la misma tanda que los datos, no como paso aparte.**

### Código de color, igual en las dos pestañas

| Grupo | Fondo | Texto | Por qué ese color |
|---|---|---|---|
| 1. Lubriderm | `F8E9E7` | `7A2E2E` | rojo — el rival a conquistar |
| 2. Marca NIVEA | `E6F2EC` | `1E6E4B` | verde — lo propio, defensa |
| 3. Otros competidores | `FDF1EA` | `8A5A08` | ámbar — conquista ampliada |
| 0. Categoría corporal | `E8EEF7` | `12315C` | azul — genéricos |
| 4. Necesidad / problema | `F3EDF8` | `5B3E7A` | violeta — dolor del usuario |
| 5. Transaccional | `E9F4F7` | `12657A` | celeste — cerca de la compra |
| 6. Informacional | `F1F3F6` | `5A6472` | gris — NO va a Search pagado |

La tabla de grupos de «Lectura estratégica» está pintada con **los mismos colores**,
así funciona de **leyenda** sin ocupar espacio extra.

### Lo aplicado

- **Lectura estratégica:** bandas azul marino en los títulos de sección, cifras de
  Lubriderm en rojo y de NIVEA en verde (la brecha se ve sin leer), advertencia en
  ámbar, cuadrícula oculta para que parezca documento.
- **Keywords:** formato condicional por grupo con `CUSTOM_FORMULA`
  (`=REGEXMATCH($B2,"^N. ")`), degradado de calor en la columna de volumen,
  competencia Alta en rojo / Baja en verde, fila fija y filtro básico.

### Detalles de la API de Sheets que sirven

- El color por categoría se hace con `addConditionalFormatRule` + `CUSTOM_FORMULA`
  sobre la fila completa; **la referencia debe ser `$B2`** (columna fija, fila
  relativa a la primera fila del rango).
- `hideGridlines` va en `updateSheetProperties`, no en el formato de celda.
- El **nombre del archivo** se cambia con `updateSpreadsheetProperties`. Estaba en
  «Hoja de cálculo sin título» — un entregable a cliente no puede salir así.


## 20-ago 15:26 — Connie descartó pagar; guía para que ella misma busque en Semrush

Después de evaluar DataForSEO decidió **no pagar nada** (msg 261) y pedir una lista
de keywords para buscar ella en su Semrush Guru, que **sí funciona en el navegador**
(lo roto es solo la API).

**Entregado:** pestaña **«Qué buscar en Semrush»** en la misma planilla
`1nstuPCSbtuK7eK6iDqVR3Wm8Cr_SBK1IEYSWzeVdueo`.

⚠️ **La planilla que ella mandó (`1p4gHF9tzir...`) NO es accesible**: da
`PERMISSION_DENIED` incluso para **leer**, con la cuenta
`pfeifer.constanza@gmail.com`. Está creada con otra cuenta suya. Avisado.

### Contenido de la guía

- **14 semillas de categoría** con la razón de cada una (no una lista suelta)
- **9 semillas de marca**, Lubriderm en rojo, NIVEA en verde
- **Dominios verificados con `curl`** para el Keyword Gap:

| Rol | Dominio | Nota |
|---|---|---|
| Propio | `nivea.com.co` | 200 |
| Competidor #1 | `lubriderm.com.co` | **tiene dominio propio en Colombia** |
| Competidor | `lactovit.co` | 200 (`lactovit.com.co` no existe) |
| Competidor | `cetaphil.com.co` | 200 |
| Competidor | `cerave.com` | **no tiene `.co`**, usa el global |
| Referencia | `eucerin.com.co` | misma casa (Beiersdorf) |

- **El paso 3, Keyword Gap, es el que importa:** pestaña *Missing* = donde el rival
  rankea y NIVEA no aparece. **Eso es exactamente lo que pidió Alex** y no se puede
  obtener de datos de publicidad.
- Dos advertencias: **no mezclar rostro** (Semrush trae CeraVe/Cetaphil faciales) y
  **conservar la columna Intent**.

### 🐞 Error de formato que hubo que corregir

Las bandas de sección se aplicaron con **índices calculados a mano sobre la lista
que se iba a escribir**, y quedaron **corridas**: la banda de «PASO 2» cayó encima
de una semilla.

**Regla:** después de escribir en una hoja, **releer y localizar las filas por su
contenido** antes de formatear. Nunca asumir que el índice de la lista en Python
coincide con la fila de la hoja — las filas vacías y las de una sola celda
desplazan la cuenta.

La corrección incluyó **limpiar todo el formato previo** del rango antes de volver
a aplicar; si no, quedan restos del formato mal puesto.
