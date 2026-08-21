---
name: litespeed-cachea-la-api-rest
description: En sudtec.cl LiteSpeed cachea las respuestas de wp-json por URL exacta; el helper pedía siempre per_page=20 y devolvía cotizaciones viejas.
metadata:
  type: project
---

**21-ago-2026, Sudtec.** `sudtec_wp.py cotizaciones` mostraba como más reciente la
cotización **#11602 del 19-ago**, cuando en el sitio ya existían **11607, 11608 y
11609**. No era la API ni la credencial: **LiteSpeed cachea las respuestas de
`wp-json` y la clave del caché es la URL exacta.**

**La prueba que lo dejó claro:**

| Llamada | Devuelve |
|---|---|
| `wc/v3/orders?per_page=20` | 11602 ← copia vieja |
| `wc/v3/orders?per_page=19` | 11609 ← real |
| `wc/v3/orders?per_page=20&_kai=<random>` | 11609 ← real |

El helper siempre pedía `per_page=20`, así que esa URL tenía copia guardada desde
antes de que existieran las nuevas. Las URLs poco usadas salían frescas — por eso
el bug era invisible: *cualquier* consulta ad-hoc daba bien y solo mentía el
comando de todos los días.

**Arreglado:** `llamar()` en `bin/sudtec_wp.py` agrega `_nc=<epoch_ms>` a **toda
petición GET**. Verificado después del cambio: `cotizaciones` ya muestra 11609
primero.

**Lo peligroso de este bug** es que no falla: responde `HTTP 200` con datos
plausibles, solo que viejos. Si le hubiera contestado a Connie «no ha entrado
ninguna cotización» me habría creído, y las dos de esa madrugada se habrían
perdido.

**La regla:** cuando un dato de este sitio parezca «congelado» en una fecha,
sospechar del caché **antes** que de la credencial o de que no haya datos.
Contrastar la misma consulta con la URL cambiada (otro `per_page`, o un parámetro
tonto). Si cambian, es caché.

**Ojo con la dirección del rompe-caché**, que es distinta según qué se verifique:

- **Leyendo datos por la API** → siempre fresco, rompe-caché siempre. Es esto.
- **Verificando cómo se ve una página pública** → al revés: la URL limpia es la
  única válida. Ver [[verificar-sin-rompe-cache]].
