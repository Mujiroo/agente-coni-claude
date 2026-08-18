# Chile / NIVEA — BB & CC Cream · ronda de QA

*18-ago-2026. Primer encargo real de Cheil que ejecuto.*

- **Libro:** `BB and CC Cream - Beiersdorf EM`
  (`1abzUqWgKRP1Jdix53mUvCvBcy8W6-t5J2_N-MSGBtrg`)
- **Pestaña:** `Chile - NIVEA` (gid `724781451`), sitio `https://www.nivea.cl/`
- **Focus keyword (F13):** `diferencia entre bb cream y cc cream`

## Cómo está armada la hoja (sirve para los otros países)

| Col | Qué es |
|---|---|
| A | etiqueta de la fila | 
| B / C | copy máster en **inglés** / largo |
| D / E | **anchor** y **URL destino** en inglés |
| **F** | **la traducción — acá van los cambios** |
| G | largo / frecuencia |
| **H / I** | **anchor y URL destino locales** |
| J / K | comentarios NIVEA / verificación |

### Los controles automáticos (filas 3-6) — leer las fórmulas, no suponer

| Celda | Fórmula | Qué exige de verdad |
|---|---|---|
| B3 | `=countif(F16:F87,"*"&F13&"*")` | **cuenta CELDAS** de F16:F87 que contengan la keyword, no repeticiones. Mínimo **6**. Ojo: **F88 en adelante no cuenta** (la FAQ queda fuera del rango). |
| B4 | `=len(F16)` | meta title **48-55** |
| B5 | `=len(F17)` | meta description **140-155** |
| B6 | `=countif(F31,F13)` | **sin comodines → exige que F31 sea EXACTAMENTE la keyword.** Ver nota abajo. |

## Cambios aplicados (12 celdas)

Respaldo de los valores anteriores: `backup-chile-nivea-bbcc-18ago.json`.

### Los 6 puntos del QA

1. **F16** meta title: 61 → **49** car, con la keyword exacta.
   `Diferencia entre BB cream y CC cream | Guía NIVEA`
2. **F17** meta description: 144 car, ahora con la keyword exacta.
3. **F29** y **F31** (teaser title y H1): fuera el «una».
   `¿Cuál es la diferencia entre BB cream y CC cream?`
4. **I55** URL local de rayos UV → `https://www.nivea.cl/consejos/solar/spf`
5. **F66** producto/claim/URL alineados: se reemplazó **solo el párrafo del
   producto** (FPS 50 → **FPS 30 - Tono Claro**), con el texto que dio el QA.
   Los otros 8 párrafos y el CTA quedaron intactos. Ya no se menciona FPS 50.
   **H66** pasó de `...FPS 50` a `...FPS 30 - Tono Claro` para que el anchor
   coincida con F66 e I66.
6. **I84** URL de NIVEA CC Fluid → Tono Claro.

### Lo que agregué porque hacía falta (no estaba en el QA)

- **H55 = `rayos UV`** y **H84 = `NIVEA Luminous630 CC Fluid 3-in-1`**: estaban
  **vacías**. El QA pedía la URL pero sin anchor el enlace no existe.
- **F30 y F32** (teaser description e image stage text) reescritas a
  `Descubre la diferencia entre BB cream y CC cream y todos sus beneficios`.
  **Motivo:** con solo los cambios del QA el contador B3 llegaba a 4 y la hoja
  exige **6 como mínimo antes de devolver la adaptación**. Con estas dos llega
  justo a 6. Fieles al inglés (*The Differences And the Benefits of BB and CC Creams*).

## Verificación posterior (leído de vuelta)

| Control | Antes | Ahora |
|---|---|---|
| Keyword en el artículo (mín. 6) | **0** | **6** ✅ |
| Meta-title 48-55 | 61 ❌ | **49** ✅ |
| Meta-description 140-155 | 144 ✅ | **144** ✅ |
| H1 contiene keyword | 0 | **0** ⚠️ ver abajo |

Las 4 URLs escritas o referidas devuelven **HTTP 200** (comprobado con curl).

## Pendientes / avisos dados a Connie

1. **B6 no puede pasar nunca.** `=countif(F31,F13)` va sin comodines, así que
   solo daría 1 si el H1 fuera literalmente `diferencia entre bb cream y cc
   cream`, sin signos ni pregunta — un H1 malo y distinto del máster inglés.
   **B3 sí usa `"*"&F13&"*"`**, o sea que quien armó la plantilla sabía hacerlo:
   **B6 parece un error de la plantilla**. No se tocó el H1 para maquillar el
   número.
2. **Claim «reduce visiblemente las manchas oscuras en 2 semanas»** — viene del
   texto del QA, no lo inventé. Es una promesa de resultado con plazo: conviene
   que esté aprobada para Chile antes de publicar.
3. **`I46` e `I55` apuntan ahora a la misma URL** (`/consejos/solar/spf`). No es
   un error, pero son dos enlaces del mismo artículo al mismo destino.
4. ~~F84 sigue llamando al producto «CC Fluid 3-in-1»~~ → **RESUELTO en la
   ronda 2** (ver abajo). Ella pidió unificarlo.
5. **Sin tocar, por ser decisión suya:** `B8` *First adaptation complete*, `B9`
   *Feedback amends complete* y `B10` (etiquetar a Atom) siguen en **No**.
6. Fuera del alcance del QA, siguen con `Local URL not found` las filas
   **19 y 20** (carrusel de productos) y `Not live Yet` la **24**.


---

# Ronda 2 — 18-ago-2026 (msg 55)

Connie pidió dos cosas: **«en el 4, por favor unifícalo»** y **«recuerda dejar en
negrita y rojo todos los anchor text que hiciste»**.

Respaldo previo (valores **y** formato): `backup-chile-nivea-bbcc-18ago-ronda2.json`.

## 1. Unificación del nombre de producto

Nombre local canónico (el del sitio, según la URL de I66/I84):
**`NIVEA Luminous630 Anti-Manchas Fluido de Día FPS 30 - Tono Claro`**.
Forma corta para el cuerpo del texto: **`NIVEA Luminous630 Anti-Manchas Fluido de Día`**.

| Celda | Antes | Ahora |
|---|---|---|
| **H84** | `NIVEA Luminous630 CC Fluid 3-in-1` | nombre local completo |
| **F84** ¶1 | `una pequeña cantidad de CC Fluid` | `una pequeña cantidad de fluido` |
| **F84** ¶2 | `NIVEA Luminous630 CC Fluid 3-in-1 ofrece…` | nombre local completo (es el ancla) |
| **F66** ¶4 | `NIVEA Luminous CC Fluid` | forma corta local |
| **F73** | `Incluir NIVEA CC Fluid en tu rutina… aplicarla` | forma corta local + **`aplicarlo`** (concordancia: «fluido» es masculino) |
| **F83** | `5. Aplica NIVEA CC Fluid` | `5. Aplica NIVEA Luminous630 Anti-Manchas Fluido de Día` |

**F73 y F83 iban más allá de lo que ella señaló** (el punto 4 era solo F84 vs
F66), pero dejarlas habría mantenido justo la inconsistencia que pidió sacar: el
artículo nombraba el producto de tres maneras. **En el máster inglés B73 y B83
también usan la forma corta** («NIVEA CC Fluid»), así que la versión local
replica esa estructura, no inventa una nueva. Queda avisado por si prefiere
revertir esas dos.

Barrido final: **no queda ninguna celda de la columna F con «CC Fluid»,
«3-in-1», «FPS 50» ni «Cellular»**.

## 2. Negrita + rojo en las anclas

**Éste era un error real mío de la ronda 1:** escribí F66 con `values.update`,
que **borra los `textFormatRuns`** de la celda. El párrafo quedó bien redactado
pero sin el formato de ancla — y F55 y F84 nunca lo tuvieron, porque las anclas
H55 y H84 las creé yo.

Formato de ancla que usa la plantilla (verificado leyendo las celdas que ya
estaban buenas, F46/F52/F81):

```json
{"foregroundColor":{"red":1},"bold":true,"foregroundColorStyle":{"rgbColor":{"red":1}}}
```

Aplicado a:

| Celda | Ancla puesta en rojo + negrita |
|---|---|
| **F55** | `rayos UV` (fila 55) |
| **F66** | `NIVEA Luminous630 …FPS 30 - Tono Claro` (fila 66) y `<CTA: Descubre Luminous630>` (fila 67) |
| **F84** | `NIVEA Luminous630 …FPS 30 - Tono Claro` (fila 84) |

En F55 se **conservaron** las tres negritas de los subtítulos numerados, y en F84
el rojo que ya tenía `ácido hialurónico`.

### La lección técnica (para no repetirla en los otros 5 países)

- **`values.update` borra el formato de texto de la celda.** Para escribir texto
  que lleva anclas hay que usar `spreadsheets.batchUpdate` con `updateCells` y
  `fields="userEnteredValue,textFormatRuns"`, mandando valor y formato juntos.
- Los `startIndex` son **offsets de caracteres**, y **el último tramo no puede
  empezar en el largo exacto del texto** (`startIndex` debe ser `< len`): si el
  ancla cierra la celda, no se agrega el tramo de reseteo. Eso devuelve un
  `400 TextFormatRun.startIndex must be less than the length`.
- Un bloque de contenido (una celda F) puede tener **varias anclas**, listadas en
  filas consecutivas de la hoja: F58 cubre las filas 58-60, F66 las 66-67, F81
  las 81-82 y F84 las 84-85. Al verificar, **no basta con mirar la fila** — el
  ancla de la fila 85 vive dentro de F84.

## Verificación (leída de vuelta de la hoja)

| Control | Valor |
|---|---|
| B3 keyword en el artículo (mín. 6) | **6** ✅ |
| B4 meta-title (48-55) | **49** ✅ |
| B5 meta-description (140-155) | **144** ✅ |
| B6 | **0** ⚠️ el error de plantilla ya explicado, sin tocar |

**Las 15 anclas locales de la pestaña quedaron en negrita + rojo en la columna F.**

## Sigue pendiente de ella (no se tocó)

- El claim **«reduce visiblemente las manchas oscuras en 2 semanas»** en F66
  (venía del texto del QA): promesa de resultado con plazo, conviene aprobarla
  para Chile antes de publicar.
- `I46` e `I55` apuntan a la misma URL.
- `B8`, `B9`, `B10` siguen en **No** — es decisión suya.
- Filas **19, 20** (`Local URL not found`) y **24** (`Not live Yet`).
