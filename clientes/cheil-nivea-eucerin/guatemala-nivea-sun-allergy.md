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


---

# Ronda 2 — cuerpo del artículo (msg 74)

*Mismo día. Respaldo: `backup-guatemala-ronda2-18ago.json` (guarda texto **y**
`textFormatRuns` de cada celda).*

**5 celdas, 12 ediciones**, todas verificadas leyendo de vuelta. Controles
intactos: **B3 = 23 · B4 = 54 · B5 = 154**.

| Celda | Qué se hizo |
|---|---|
| **F36** | 2º párrafo reescrito: la variación depende del **tipo de alergia**, no del tipo de piel |
| **F39** | 1er párrafo sin la repetición «suele/suelen» y sin «únicamente»; cierre nuevo derivando a un profesional (fuera «para que te tranquilice») |
| **F44** | fuera «también conocida como intoxicación solar» · **«Uticaria» → «Urticaria»** · definición de reacción fotoalérgica reescrita |
| **F50** | fuera el claim de que el sol mejora la dermatitis atópica · punto 2 reescrito sin lista de fármacos y con la advertencia de no suspenderlos · punto 3 acotado |
| **F53** | frase rota del paño frío arreglada · antihistamínicos ya no «actúan sobre la causa» · corticosteroides solo por indicación profesional |

## Lo delicado: el formato sí estaba en juego acá

A diferencia de la ronda 1, **F39, F44 y F53 sí tienen `textFormatRuns`**
(subtítulos en negrita y anclas en negrita+rojo). Escribirlas con `values.update`
habría borrado el formato — el error de la ronda 1 de Chile.

Se usó `updateCells` con `fields="userEnteredValue,textFormatRuns"`, **recalculando
los offsets**: se expande el formato a una lista por carácter, se aplican los
reemplazos arrastrando el formato del punto de inserción, y se reagrupan los
tramos. Los tramos con formato quedaron **4, 4 y 9** — los mismos que antes — y
las anclas siguen sobre `NIVEA Repair & Care`, el CTA y `Piel seca o escamosa`.

*El script quedó como referencia para los otros países.*

## Una redacción es mía, no del QA

El QA pidió «aclarar que las reacciones a ingredientes de protectores solares
pueden ocurrir, pero no son generales» **sin dar el texto**. Se escribió:

> «Entre los desencadenantes descritos se encuentran sustancias presentes en
> fragancias y desinfectantes y, en algunos casos, ingredientes de ciertos
> protectores solares, aunque no se trata de reacciones generalizadas.»

Está avisado a Connie por si quiere otra formulación.

## 🔴 Pendiente que nadie ha pedido y conviene resolver

**`I53` e `I55` apuntan a `nivea-repair-and-care-crema-400ml…`, que da 404** — es
**la misma URL muerta** que había en F21 y que ya se reemplazó. O sea: el cuerpo
del artículo sigue enlazando a un producto que no existe en Guatemala, dos veces.

Además el texto de F53 **nombra el producto como «NIVEA Repair & Care»**, que es
el nombre del máster inglés, no el nombre local.

**Propuesta (no aplicada, esperando decisión de Connie):** apuntar I53 e I55 a
`…/crema-corporal-regeneracion-intensiva-con-glicerina-250-ml-40058086802450046.html`
(**200 OK**, es el equivalente local del Repair & Care) y unificar el nombre del
producto en F53 y en las anclas H53/H55 — el mismo criterio que se aplicó en
Chile.

## Detalle menor observado

El ancla roja de F39 viene **partida** desde antes (`Piel seca` + un carácter sin
formato + `o escamosa`), aunque H40 declara el ancla completa `Piel seca o
escamosa`. Se **preservó tal cual** en vez de corregirla, para no meter cambios
que nadie pidió. Se arregla en un minuto si Connie quiere.


---

# Ronda 3 — producto local, terminología y sección reemplazada (msg 76)

*Respaldo: `backup-guatemala-ronda3-18ago.json`. **7 celdas F + 9 celdas H/I**,
todas verificadas leyendo de vuelta. Controles: **B3 = 24** (subió de 23: la nueva sección F67 también nombra la keyword) · B4 = 54 · B5 = 154.*

| Celda | Qué se hizo |
|---|---|
| **F53** | producto cambiado a **NIVEA Crema Corporal Regeneración Intensiva**, con copy corregido (ver abajo) |
| **H53 · H55** | ancla → `NIVEA Crema Corporal Regeneración Intensiva` |
| **I53 · I55** | URL → la del Regeneración Intensiva **(200 OK, no la que dio el QA)** |
| **F58** | las quemaduras ya no «se producen donde no se usó crema solar»: ahora protección insuficiente o mal reaplicada |
| **F61** | `SPF`→`FPS` · `Permanezca`→`Permanece` · consejo 3 reescrito para que no invite a exponerse |
| **F63** | «gama de Cremas Solares» → «gama de **protectores solares** NIVEA» |
| **F64** | cremas/lociones → **protectores solares** · `SPF`→`FPS` · «exposición **al** sol» · CTA nuevo |
| **H64** | ancla → `Protectores solares NIVEA` |
| **F66 · F67** | sección del Derma Skin Clear **reemplazada** por el protector facial local |
| **H67 · I67 · H68 · I68** | anclas y URL del protector facial **(200 OK)** — antes decían `Local URL not found` |

## 🔴 El QA volvió a dar una URL muerta

Para `I53` e `I55` el QA propuso
`…/crema-para-cuerpo-piel-extra-seca-y-piel-aspera-400-ml-40058086802520046.html`
→ **404**. Es **exactamente la misma URL** que ya había propuesto para F21 en la
ronda 1 y que también estaba muerta.

**Se usó la PDP viva del producto que el propio QA nombró**
(`NIVEA Crema Corporal Regeneración Intensiva`):
`…/crema-corporal-regeneracion-intensiva-con-glicerina-250-ml-40058086802450046.html`
→ **200 OK**.

> **Patrón que conviene recordar para los otros países:** las URLs que trae este
> QA hay que comprobarlas una por una. Van dos de dos malas.

## 🔴 Y dos claims del QA no están en la ficha

El copy que el QA propuso para F53 decía *«Su fórmula con **Sérum de Humectación
Profunda**, glicerina y dexpantenol… proporciona hasta **72 horas** de
humectación»*. Contra la PDP real:

| Claim del QA | Qué dice la ficha |
|---|---|
| «Sérum de Humectación Profunda» | **no aparece** — la ficha habla de «fórmula rica en glicerina» |
| «hasta 72 horas de humectación» | **48 hrs**: *«Sensación de alivio para piel extra seca por 48 hrs»* |
| glicerina · dexpantenol · piel extra seca | ✅ correctos |
| «suave y tersa» | la ficha dice «suave y **elástica**» |

**Texto que se escribió** (mismo sentido, cifras reales):

> «Cuando la piel ya no esté irritada ni dañada, puedes aplicar NIVEA Crema
> Corporal Regeneración Intensiva. Su fórmula rica en glicerina y con dexpantenol
> ayuda a cuidar la piel extra seca, calma la piel áspera y brinda sensación de
> alivio por 48 horas, dejándola suave y elástica.»

*Nota a favor del QA:* su apertura («cuando la piel ya no esté irritada») calza
con la advertencia de la propia ficha, que dice **«evitar el contacto con la piel
irritada»**. Se conservó tal cual.

## La sección F66/F67 la redacté yo

El QA pidió reemplazar la sección del *Derma Skin Clear* por «el protector facial
local para piel sensible» **sin dar el texto**. Se escribió desde los claims de la
PDP real, ninguno inventado: piel del rostro más expuesta · FPS 50 · apto para
piel sensible · fórmula no grasosa ni pegajosa · sin aroma · dermatológicamente
probado.

⚠️ **Un claim que conviene que Connie mire:** la PDP lista entre sus beneficios
**«Protección contra la alergia al sol»**. Es el claim más pertinente del artículo
y **es de NIVEA**, no inventado, pero es el más sensible. Se incluyó como *«entre
sus beneficios NIVEA indica la protección frente a la alergia al sol»*. Si
prefiere sacarlo, es una línea.

## Dos cosas señaladas y no tocadas

1. **H64 vs I64:** el ancla ahora dice «Protectores solares NIVEA» pero la URL
   sigue apuntando al listado **«Leche solar»**. Existen dos listados más arriba
   que calzan mejor y responden 200:
   `…/productos/proteccion-solar` y `…/productos/proteccion-solar/proteccion-solar`.
2. **F70** («Protección solar para piel sensible: NIVEA Sun Protect & Sensitive
   FPS50») es el producto **corporal**, dentro de una sección que F65 titula como
   de protectores **faciales**. Ahora que F66 es el facial de piel sensible, los
   dos títulos se parecen mucho. Decisión de Connie.
