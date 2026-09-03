# Auditoría Google Ads — Sudtec (`9907217991`)

**Fecha:** 3-sep-2026 · **Ventana:** 30 días (3-ago a 2-sep-2026) · **Zona:** America/Santiago · **Moneda:** CLP
**Método:** `memory/skills/ads-auditoria` (AgriciDaniel/claude-ads) — catálogo `references/google-audit.md`,
puntaje determinístico de `references/scoring-system.md`, marco de `references/thinking-framework.md`.
**Motor de puntaje:** `scratchpad/score.py` (reproducible, no estimado a ojo).

> Sin nota en letras, por contrato de la skill. La salud va **siempre** acompañada de la cobertura
> y de la ventana de datos.

## Resultado

categoría       salud  cobertura   (peso pass/known · desconocido)
Medición          36%        73%   (4/11 · 4)
Términos          14%       100%   (2/14 · 0)
Estructura        14%       100%   (2/14 · 0)
Calidad            0%       100%   (0/9 · 0)
Anuncios          80%       100%   (4/5 · 0)
Extensiones       40%       100%   (2/5 · 0)
Puja              25%       100%   (1/4 · 0)

SALUD GLOBAL      24%
COBERTURA         94%   (evidencia disponible sobre controles aplicables)
ventana de datos: 30 días (3-ago a 2-sep-2026) · zona America/Santiago · CLP

FALLOS CRÍTICOS: 3
  G46 · Medición · 'Formulario de contacto - Enviar' tiene ventana de clic de 1 DIA
  G16 · Términos · 77% del gasto de la keyword principal en búsquedas no bomberiles
  G24 · Calidad · experiencia de página BELOW_AVERAGE en casi todo el gasto alto

FALLOS ALTOS: 7
  G14 · Términos · las 20 negativas previas estaban en EXACTA y no frenaban las variantes
  G17 · Términos · amplia activa sin la lista de negativas apretada que exige el playbook
  G03 · Estructura · el grupo 'General' es cajón de sastre: EPP, bomberos, botas, mangueras juntos
  G05 · Estructura · no hay campaña de MARCA separada
  G08 · Estructura · una sola keyword se llevó el 61,6% del presupuesto de septiembre
  G20 · Calidad · QS 1 en 'improfor' (9.184 CLP) y en 'arnés de seguridad para alturas'
  G39 · Puja · la campaña gasta el presupuesto completo con CPA inflado

## Los 3 fallos críticos, con evidencia y mecanismo

### G46 · La ventana de conversión es de 1 día

`Formulario de contacto - Enviar` (LEAD_FORM_SUBMIT, primaria) tiene
`click_through_lookback_window_days = 1`. La segunda primaria, `Cotización formulario`,
tiene 30.

**Mecanismo:** Sudtec vende por cotización a cuerpos de bomberos y municipios — decisiones
que tardan días. Con ventana de 1 día, **toda conversión que ocurre 48 h después del clic
no existe** para Google. Eso no solo subreporta: **envenena el smart bidding**, que aprende
de esas señales y puja hacia el tráfico que convierte rápido, no hacia el que compra.

**Sospecha que esto explica parte del colapso** (4,67 → 1,0 conv/día). No está probado:
habría que ver desde cuándo está en 1 día. `change_event` puede decirlo.

### G16 · El 77% del gasto de la keyword principal no es del negocio

`equipo de protección personal` (amplia) se abrió a **432 términos**. El corte:

| | gasto 30d | conversiones | CPA |
|---|---|---|---|
| términos que dicen bombero/rescate/incendio | 9.981 (23%) | 6,0 | **1.664** |
| el resto | 34.203 (77%) | 5,0 | 6.841 |

El núcleo rinde igual que la base de la cuenta (1.675). La cola se come el presupuesto.

**Ya mitigado hoy en parte:** 10 negativas de frase cortan 17.798 CLP/30d sin perder ninguna
conversión. CPA de esa keyword: 4.017 → 3.039.

### G24 · La experiencia de página está BELOW_AVERAGE en casi todo el gasto alto

`post_click_quality_score` = BELOW_AVERAGE en `manguera de bomberos`, `articulos para
bomberos`, `improfor`, `accesorios bomberos`, `herramientas de bomberos`, `arnés de
seguridad`, `casco sicor`. **Ninguna keyword llega a ABOVE_AVERAGE.**

**Causa probable:** casi todos los anuncios apuntan a `https://www.sudtec.cl/lista-productos/`,
un listado genérico. El único que apunta a una categoría real es el de Botas
(`/product-category/epp/botas/`).

**Es el hallazgo de mayor palanca:** la página de destino entra en el Nivel de calidad, y el
Nivel de calidad entra en el CPC. El CPC se triplicó (270 → 900 CLP). Arreglar destinos
ataca la causa; las negativas solo tapan la fuga.

## Los 7 fallos altos

| ID | Hallazgo |
|---|---|
| G14 | Las 20 negativas previas estaban en **concordancia exacta**: `www apro` no frenaba «www apro cl» |
| G17 | Amplia corriendo sin la lista de negativas apretada que el playbook exige como condición |
| G03 | El grupo `General` es cajón de sastre: EPP, bomberos, botas y mangueras en el mismo grupo |
| G05 | **No hay campaña de marca.** El playbook la manda siempre encendida: es el clic más barato |
| G08 | Una sola keyword se llevó el **61,6%** del presupuesto de septiembre |
| G20 | **QS = 1** en `improfor` (9.184 CLP) y en `arnés de seguridad para alturas` (3.679) |
| G39 | La campaña gasta el presupuesto completo con el CPA inflado |

## Lo que está sano (para no romperlo)

- **Anuncios: 80% de salud.** CTR de cuenta **12,24%**; el principal 12,43% y trae el **84%**
  de las conversiones. **El creativo no es el problema.** Todos APPROVED.
- **Ritmo de gasto:** proyección 285.027 contra tope de 300.000.
- **Sitelinks e imágenes** presentes en la campaña principal.
- **Competencias** convierte a CPA **1.885**, cerca de la base.

## Contradicciones, supuestos y datos faltantes (exigido por la skill)

- **`equipo de protección personal` no reporta `quality_info`.** No se interpreta: queda
  `unknown`. No se sabe si es falta de volumen o algo más.
- **G-CT1 (doble conteo): `unknown`.** Hay dos primarias de categoría `SUBMIT_LEAD_FORM`.
  Podrían estar contando el mismo envío dos veces. **No es verificable por API** — hay que
  mirar el disparo real en el sitio.
- **Cobertura 94%:** el 6% que falta es medición (GA4, doble conteo).
- **Las dos skills se contradicen** en umbrales fijos de conversiones. Se siguió la de
  auditar (evidencia propia) para juzgar la cuenta, y la de operar como semáforo de diseño.
- **Las 3 negativas frenadas** (`scott`, `holmatro`, `rosenbauer`) no se aplicaron porque su
  familia de frase contiene una búsqueda que sí convirtió.

## Próximos pasos, con dueño y ventana

| # | Acción | Dueño | Ventana de medición | Reversión |
|---|---|---|---|---|
| 1 | **Subir la ventana de conversión de 1 a 30 días** en `Formulario de contacto - Enviar` | Kai, con OK de Connie | 2 ciclos de conversión | Volver a 1 día; es un campo, se deshace solo |
| 2 | **Mandar los anuncios a la categoría que corresponde**, no a `/lista-productos/` | Connie decide destinos; Kai los aplica | 30 días (QS tarda) | URL anterior guardada |
| 3 | Leer el efecto de las 10 negativas | Kai | **3 días** | Quitar las negativas |
| 4 | Vaciar o poblar la lista de negativas de cuenta (hoy tiene 0 miembros) | Kai | — | Quitar miembros |
| 5 | Evaluar campaña de **marca** | Connie (presupuesto) | 30 días | Pausar |

**Regla que se respeta:** no se toca la puja mientras haya un cambio de segmentación en curso
(disciplina de cambio de `bidding-strategies.md`). Las 10 negativas son de hoy.

**Nada de esta auditoría se ejecutó.** Lo único aplicado hoy fueron las 10 negativas que
Connie aprobó explícitamente (msg 660).
