# Skills instaladas — cómo se usan juntas

Dos skills de Google Ads, ambas de GitHub y ambas **MIT**. No compiten: **una
enseña a operar y la otra a auditar.** Se cargan según lo que haya que hacer.

| Carpeta | Origen | ⭐ | Para qué |
|---|---|---|---|
| `google-ads/` | [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | 44.901 | **Operar**: armar campañas, estructura, keywords, match types, redactar RSA, decidir el día a día |
| `ads-auditoria/` | [`AgriciDaniel/claude-ads`](https://github.com/AgriciDaniel/claude-ads) | 8.253 | **Auditar**: diagnosticar una cuenta con método, exigir evidencia, puntuar, separar observación de recomendación |

## Cuál cargar

- **«Armemos / cambiemos / redactemos»** → `google-ads/`, y para decisiones sobre
  una cuenta viva **siempre** `references/google-search-playbook.md`: ahí viven
  los umbrales. Para anuncios, `references/rsa-output-spec.md` es obligatorio
  (15 titulares ≤30, 4 descripciones ≤90, y **verificar los caracteres contando,
  no a ojo**).
- **«Revisemos / qué está mal / por qué rinde así»** → `ads-auditoria/`, con
  `references/google-audit.md` y `references/thinking-framework.md`.

## Cuando se contradicen

Ya se toparon una vez, el 19-ago-2026, con las **keywords negativas**:

- La de **operar** trae listas de negativas de arranque (free, cheap, jobs,
  course, pdf…) para aplicar al construir.
- La de **auditar prohíbe** proponer negativas sin un informe de términos de
  búsqueda.

**La regla que quedó, y las concilia:**

> Las negativas **de higiene** —al construir un grupo nuevo, sobre términos que
> obviamente no son del negocio— salen de la lista de arranque, sin informe.
> Pero **afirmar que una keyword existente está desperdiciando plata, o recortar
> lo que ya corre, exige el informe de términos de búsqueda.**

El caso real que la originó: ese día propuse 22 negativas genéricas para Sudtec
sin informe (higiene, aceptable), pero la negativa de **«relojes»** solo quedó
justificada cuando **leí los términos de búsqueda** y vi que la keyword gastaba
en gente buscando relojes. Lo segundo es lo que exige evidencia.

**En general:** para **construir**, manda la de operar. Para **afirmar algo sobre
la cuenta**, manda la disciplina de evidencia de la de auditar.

## Lo que NO se copió

De la skill de auditoría se dejaron fuera las referencias de Meta, TikTok,
LinkedIn, Amazon, Apple, Pinterest, Reddit, X y YouTube: **no hay acceso a esas
plataformas** y solo ocuparían espacio. Si algún día se conecta alguna, se bajan
de `AgriciDaniel/claude-ads`, carpeta `ads/references/`.

Tampoco se copiaron scripts de instalación ni dependencias de Python de ninguno
de los dos repos: **solo markdown**.

Relacionado: [[skill-google-ads]], [[cuota-google-ads]]
