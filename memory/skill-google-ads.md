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
