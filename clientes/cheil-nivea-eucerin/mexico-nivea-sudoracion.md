# México / NIVEA — Sudoración excesiva · ronda de QA

*18-ago-2026. Tercer país trabajado.*

- **Libro:** `How To Sweat Less, How to Prevent Sweating + Excessive Sweating - Reop - Beiersdorf EM`
  (`1N5Ks0BkIN5IV4wWJj2b1hKjy1CqkXMUEy7kCigod_ZQ`)
- **Pestaña:** `Mexico - NIVEA` (gid `1010830381`), sitio `https://www.nivea.com.mx/`
- Respaldo: `backup-mexico-nivea-18ago.json`

**13 celdas aplicadas y verificadas.** Controles: B3 = 14 · B4 = 54 · B5 = 147 ✅

| Celda | Cambio |
|---|---|
| **F57** | párrafo de Tono Natural alineado a la PDP + **fuera la nota de prueba instrumental** |
| **H64** | ancla → `NIVEA Tono Natural Derma Control Stick Antitranspirante 50 g` |
| **F66** | a singular → `Antitranspirante NIVEA MEN Derma Control Defend` |
| **F67** | párrafo MEN reescrito (fuera «protege de picores») + fuera la nota de prueba + **«piel sensible» destacado como ancla** |
| **H67 · I67** | ancla `piel sensible` → `nivea.com.mx/consejo/desodorante-para-piel-sensible` (**200 OK**) |
| **F72** | «prevenir el sudor» → «**controlar la sudoración**», con antitranspirantes |
| **F73** | `Preguntas Frecuentes (FAQ)` → `Preguntas frecuentes` |
| **F75** | «son ideales» → «**pueden ser una opción**» |
| **F77** | añadida la derivación a profesional de la salud |
| **F81** | ya no responde «Sí» rotundo sobre el peso |
| **F83** | ya no dice que beber agua mantiene el sudor bajo control |
| **F85** | «funcionen más efectivamente» → «**aplicación más uniforme**» |

## Esta vez el QA acertó — y conviene decirlo

Se verificaron las PDP de los dos productos. **Todo lo que propuso el QA está
respaldado**, casi literal:

- **Tono Natural Stick 50 g:** *«72H de Protección · Ayuda a reducir la aparencia
  de piel flácida y manchas oscuras después del rasurado · Recupera el tono de la
  piel natural · Fórmula avanzada con ácido hialurónico puro y vitamina C»*.
- **MEN Derma Control Defend Spray 150 ml:** *«72H de Protección · Fortalece y
  previene la irritación · Fórmula avanzada con ácido hialurónico puro y vitamina
  B5»*, y **«picor» no aparece en ninguna parte** → el reparo del QA era correcto.

⚠️ **Tropiezo de método que casi me hace equivocarme:** el HTML de nivea.com.mx
**parte las palabras** (`vitamin a C`, `hialurónicopuro`), así que un `grep` de
«vitamina C» devuelve **0 coincidencias aunque el claim sí esté**. Hay que mirar
el contexto, no confiar en el conteo. Vale para los otros países.

## Las notas de «prueba instrumental»: se eliminaron con fundamento

El QA pedía sacarlas *«salvo que exista un product deck local que lo respalde»*.
Se fue a mirar: **`B19` («BDF product deck used») sigue con el texto de plantilla**,
sin ninguna URL. No hay respaldo → **se eliminaron las dos** (la de 21-22
participantes en F57 y la de 20 en F67). Además, las PDP declaran las 72 h **sin
asterisco ni nota de participantes**, así que quitarlas deja el texto más alineado
con el sitio, no menos.

## 🔎 Tres cosas señaladas y NO tocadas

1. **El CTA de F57 quedó desalineado con su ancla.** Dentro de F57 el CTA sigue
   diciendo `<CTA: Nivea Derma Control Tono Natural >`, mientras **H64** pasó a
   `NIVEA Tono Natural Derma Control Stick Antitranspirante 50 g`. El QA solo pidió
   H64. Se dejó como lo pidió, pero conviene decidir cuál manda.
2. **`I59` apunta a un producto distinto del que dice su URL.** El slug dice
   `roll-on-…-defend-50ml`, pero el H1 de esa página es **«NIVEA Aerosol
   Antitranspirante Derma Control Defend 50ml»**. Es un lío del propio sitio, no
   de la planilla.
3. **F83 perdió un dato práctico.** El texto del QA reemplaza toda la respuesta y
   con eso desaparece la recomendación de **«6 a 8 vasos (1,5 a 2 litros) diarios»**.
   Se aplicó lo que pidió el QA; recuperarlo es una frase.

## 🐞 Un defecto SEO del sitio de NIVEA México (para Connie, que es la SEO)

La PDP de **Tono Natural Stick 50 g** tiene la **etiqueta `<title>` equivocada**:
dice *«Antitranspirante B&W Invisible Fresh Roll-On 50ml | NIVEA»*, que es **otro
producto**. El `h1` y el `og:title` sí son correctos.

Eso es lo que Google muestra en resultados: la página compite con el título de un
producto que no es. No es cosa de la planilla, pero es exactamente su tema.
