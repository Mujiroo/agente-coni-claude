---
name: maton-google-slides
description: Maton tiene una novena app conectada, google-slides, que no figura en CLAUDE.md.
metadata:
  type: reference
---

**Maton ya no tiene 8 apps sino 9: `google-slides` está conectada y ACTIVE**
desde el 18-ago-2026 19:49 UTC. `CLAUDE.md` todavía dice ocho y no la nombra.

Se usa igual que el resto, contra la API nativa:

```bash
bash bin/maton.sh 'google-slides/v1/presentations/<id>'
bash bin/maton.sh 'google-slides/v1/presentations/<id>:batchUpdate' -X POST -H 'Content-Type: application/json' -d @cuerpo.json
```

Probado en lectura el 18-ago con la presentación de Weber: devuelve `slides`,
`layouts`, `masters` y `pageSize` completos.

**Dato útil:** los decks de Cheil vienen en **10 x 5.625 pulgadas** (16:9), que en
EMU es 9144000 x 5143500. Las medidas de la API van en EMU: 914400 EMU = 1 pulgada.

Relacionado: [[cheil-nivea-eucerin]]
