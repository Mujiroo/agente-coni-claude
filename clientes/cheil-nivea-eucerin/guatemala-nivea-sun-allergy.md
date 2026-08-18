# Guatemala / NIVEA — Sun Allergy · ronda de QA

*18-ago-2026. Segundo encargo real de Cheil.*

- **Libro:** `Sun Allergy - reop - Beiersdorf EM`
  (`1J4hO10yzqUHaBMhEBZP6cYwuGZpw2hGj4VOZ-pxGk2w`)
- **Pestaña:** `Guatemala - NIVEA` (gid `1255178144`), sitio `https://www.nivea.com.gt/`
- **Focus keyword (F13):** `alergia al sol`
- Respaldo de los valores anteriores:
  `backup-guatemala-nivea-sunallergy-18ago.json`

## Aplicado (8 celdas) y verificado leyendo de vuelta

| Celda | Cambio |
|---|---|
| **F21** | producto → *Crema Corporal Milk Nutritiva Piel Extra Seca* (**200 OK**), **elegido por Connie** el 18-ago 13:52 |
| **F16** | meta title — ver la nota de abajo, **no es el texto literal del QA** |
| **F17** | meta description del QA, tal cual · **154 car** ✅ |
| **F22** | producto → protector solar facial piel sensible FPS 50 (**200 OK**) |
| **F25** | artículo → `…/proteccion-solar/quemaduras-solares-117` (**200 OK**) |
| **F28** | teaser title → `Alergia al sol: causas, alivio y prevención` |
| **F30** | H1 → igual que F28 |
| **F34** | en la tabla de contenidos: «Cómo tratar…» → «**Cómo aliviar los síntomas de** la alergia al sol» |

Controles después del cambio: **B3 = 23** ✅ · **B4 = 54** ✅ · **B5 = 154** ✅ ·
B6 = 0 (estaba en 0 desde antes, no es regresión).

## Los dos problemas que trajo el propio QA

### 1. El F16 que sugirió el QA no cabe en la hoja

`Ayuda para la alergia al sol: causas, alivio y prevención` mide **57
caracteres**, y el control B4 exige **48-55**. Aplicarlo tal cual rompía la hoja.

**Se aplicó la misma frase sin el artículo «la»** →
`Ayuda para alergia al sol: causas, alivio y prevención` = **54**, que además es
exactamente el largo que tenía el título anterior. Conserva las tres palabras que
el QA pedía (*causas, alivio, prevención*) y saca «Remedio», que era el reparo de
fondo.

### 2. 🔴 La URL de reemplazo para F21 también está caída

El QA dijo que la URL de F21 daba error —**cierto**, `nivea-repair-and-care-crema-400ml`
devuelve **404**. Pero **el reemplazo que propuso también da 404**:
`crema-para-cuerpo-piel-extra-seca-y-piel-aspera-400-ml-40058086802520046.html`
→ redirige a `sitecore/service/notfound.aspx`.

**Resuelto:** se le ofrecieron dos productos vivos y **Connie eligió la Crema
Corporal Milk Nutritiva Piel Extra Seca**, que ya quedó escrita en F21. Las dos
opciones que se le presentaron:

- `…/crema-corporal-humectante-nivea-body-milk-nutritiva-para-piel-extra-seca-75010545091100046.html`
  → *Crema Corporal Milk Nutritiva Piel Extra Seca* (**200**) — es el que más se
  acerca a «piel extra seca» que pedía el QA.
- `…/crema-corporal-regeneracion-intensiva-con-glicerina-250-ml-40058086802450046.html`
  → *Crema Corporal Regeneración Intensiva* (**200**) — es el equivalente local
  del *Repair & Care* que estaba originalmente.

## Hallazgo extra: la tabla de contenidos no coincide con los títulos reales

No lo pidió el QA, pero F34 promete secciones con nombres que **no son** los que
llevan los encabezados del artículo:

| F34 dice | El título real dice |
|---|---|
| Cómo aliviar los síntomas de la alergia al sol *(recién cambiado)* | **F52:** Cómo controlar los síntomas de la alergia al sol |
| Información general | **F56:** Datos generales |
| 4 consejos para prevenir la alergia al sol | **F60:** 4 consejos para evitar una alergia solar |

Se dejó **como lo pidió el QA**. La decisión de alinear TOC y encabezados es de
Connie.

## Verificación de URLs (todas comprobadas con curl)

| URL | Estado |
|---|---|
| F21 anterior (repair-and-care) | **404** 🔴 *reemplazada* |
| F21 reemplazo sugerido por el QA | **404** 🔴 *descartada* |
| **F21 nueva** (milk nutritiva piel extra seca) | 200 ✅ |
| F22 nueva (facial piel sensible FPS 50) | 200 ✅ |
| F23 (sin tocar) | 200 ✅ |
| F25 nueva (quemaduras solares) | 200 ✅ |
| F26, F27 (sin tocar) | 200 ✅ |

## Nota de método

Las celdas F16:F34 **no tienen `textFormatRuns`** (se comprobó antes de escribir),
así que aquí `values.batchUpdate` era seguro. En hojas con anclas en negrita+rojo
hay que usar `updateCells` — ver `chile-nivea-bb-cc-cream.md`.
