---
name: skill-google-ads
description: Tengo instalada una skill de Google Ads de GitHub; hay que leerla antes de cualquier trabajo de Ads, y su playbook de Search ya contradice cosas de la cuenta de Sudtec.
metadata:
  type: reference
---

**El 19-ago-2026 Connie pidió buscar en GitHub una skill de Google Ads bien
puntuada, y después pidió quedarse con las dos mejores** para poder «operar y
auditar como un profesional». Quedaron instaladas **las dos**:

- `memory/skills/google-ads/` — **operar** (104 KB)
- `memory/skills/ads-auditoria/` — **auditar** (116 KB)

**`memory/skills/README.md` explica cuál cargar en cada caso y qué hacer cuando
se contradicen.** Leer ese archivo primero.

**De dónde salió:** [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills),
**44.901 estrellas**, licencia MIT, actualizado el mismo 19-ago-2026. Copié solo
la carpeta `skills/ads/` (markdown), **sin** scripts de instalación ni
dependencias de Python.

**Cómo usarla:** leer `SKILL.md` y, para decisiones sobre una cuenta viva,
`references/google-search-playbook.md`. **Los umbrales viven en las referencias,
no en el SKILL.md** — la propia skill lo advierte.

**Las piezas que más sirven:** `google-search-playbook.md` (escalera de intención,
estructura de cuenta, match types, negativas, ritual semanal de términos de
búsqueda), `conversion-tracking.md`, `audit-guardrails.md`.

**Lo que ya detectó sobre Sudtec** al cruzarla con la auditoría del 17-ago:

1. **Keywords compitiendo consigo mismas.** «articulos para bomberos»,
   «accesorios bomberos», «guantes de bomberos», «fireground» y «equipos de
   bomberos» están cada una en **dos concordancias a la vez**. La skill lo llama
   pujar contra tu propia cuenta y partir los datos.
2. **La escalera de intención está al revés.** Manda empezar por **marca**
   («siempre encendida, el clic más barato») y recién después ir a competencia.
   Sudtec tiene competencia corriendo (improfor, fireground, casco sicor) y marca
   casi apagada. Refuerza lo que ya le recomendé el 19-ago.
3. **Presupuesto de marca nunca compartido**, y **una campaña que no llega a
   15-30 conversiones al mes no alimenta el smart bidding**. «Competencias» gastó
   3.922 de 60.800: es una campaña muerta de hambre que habría que fusionar.

**Se contradicen en un punto**, y la regla para conciliarlas está en
`memory/skills/README.md`: las negativas **de higiene** al construir no necesitan
informe de términos de búsqueda; **afirmar que una keyword existente desperdicia
plata, sí**.

Relacionado: [[skill-seo-de-connie]], [[vigilancia-ads-429-transitorio]]

## 3-sep-2026 · Las skills explican el desangre, y frenan el próximo cambio

Connie preguntó por ellas (msg 662). Al releerlas contra el trabajo del día
aparecieron tres cosas que valen para adelante:

**1. La regla de la amplia** (`google-search-playbook.md`, línea 64), textual:
*«Introduce Broad only after: 30+ conversions/month in the campaign, AND smart
bidding live, AND a tight negative list. Broad without all three is a donation to
Google.»*

Sudtec cumplía **dos de tres**: 111 conversiones en 30 días ✅, smart bidding ✅,
pero **la lista de negativas NO estaba apretada** — las 20 que existían estaban en
concordancia **exacta** y no frenaban nada. **Esa era la pata que faltaba**, y
explica por qué la amplia se abrió a 429 búsquedas. Ver
[[negativa-frase-bota-la-familia]].

**2. La disciplina de cambio** (`ads-auditoria/references/bidding-strategies.md`):
antes de tocar la puja hay que *«confirmar que ningún cambio concurrente de
presupuesto, conversión, segmentación, creativo o política enturbie la
interpretación»*. **Hoy se cambió segmentación (10 negativas), así que cualquier
cambio de estrategia de puja queda congelado** hasta leer el efecto. No se hacen
dos cambios a la vez.

**3. Se contradicen otra vez, y ahora en algo que importa.** La de **operar** da
umbrales fijos (~15-30 conversiones/mes para smart bidding, 30+ para amplia). La de
**auditar** dice explícitamente *«Do not apply fixed target multipliers, fixed
minimum conversion counts, or a fixed adjustment cadence across accounts»*.

**Cómo conciliarlas:** los umbrales de la de operar sirven como **semáforo de
diseño** —¿esta campaña tiene volumen para sostener amplia?—, no como veredicto
sobre una cuenta viva. Para juzgar la cuenta manda la evidencia propia, que es lo
que pide la de auditar. **Cuando choquen en algo que cambie una decisión, decírselo
a Connie y explicar cuál se siguió.**

**Dato de consolidación pendiente:** `Competencias` lleva **7 conversiones** en 30
días, muy por debajo del umbral. La skill de operar mandaría **fusionarla**. No se
propone todavía: hoy esa campaña es justamente el destino al que se están ruteando
las búsquedas de marca ajena, y hay que ver cómo queda antes de moverla.

