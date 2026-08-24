---
name: litespeed-nonce-vencido-sudtec
description: En sudtec.cl LiteSpeed sirve páginas de 40-65h y el nonce del botón de cotizar vence a las 24h, así que las solicitudes fallan en silencio.
metadata:
  type: project
---

**Hallazgo del 24-ago-2026**, buscando por qué se desplomaron las solicitudes de
presupuesto (ver `clientes/sudtec/estado.md`).

**El mecanismo:** LiteSpeed cachea las páginas con un TTL larguísimo y las sigue
sirviendo días después. El botón de YITH «Solicitar presupuesto» lleva incrustado
un **nonce de WordPress, que vive 24 horas**. Cuando la página cacheada supera
esa edad, **el nonce que recibe el visitante ya no es válido** y el envío falla
sin mensaje visible.

**Lo medido el 24-ago 15:00 Chile:**

| página | generada | edad |
|---|---|---|
| home | 21-ago 22:13 | 65 h |
| `/product-category/epp/botas/` <i>(destino de los anuncios)</i> | 22-ago 03:30 | 59 h |
| `/producto/set-alzaprima-mighty-strut/` | 22-ago 19:20 | 44 h |

**La prueba que lo deja claro:** en la página cacheada el nonce era
`e2dd72261d`; forzando un render fresco con un parámetro aleatorio salía
`a69430c315`. **Son distintos**, o sea el cacheado ya no es el vigente.

**Lo peor: el tráfico pagado no escapa.** Probé con `?gclid=...` y con
`?utm_source=...` — **LiteSpeed igual responde `hit`** con la versión vieja. Solo
un parámetro desconocido produce `miss`. Así que **la gente que llega desde Google
Ads recibe justamente la página con el token muerto**.

## Cómo reconocerlo la próxima vez

La firma es siempre la misma y es fácil de confundir con «bajó la demanda»:

- **Los clics y las impresiones se mantienen**, pero las solicitudes se van a cero
- El sitio responde **HTTP 200** y el botón **sí aparece** en el HTML
- No hay páginas editadas ni plugins nuevos
- El contador de conversiones de Google **sigue marcando** ([[contadores-no-son-envios]])

**Cómo comprobarlo, todo de solo lectura:**

```bash
curl -s https://www.sudtec.cl/product-category/epp/botas/ | grep -oE "cached by LiteSpeed Cache [0-9.]+ on [0-9: -]+"
# y comparar el nonce contra un render fresco:
curl -s "https://www.sudtec.cl/product-category/epp/botas/?bust=$(date +%s)" | grep -oE 'nonce":"[a-f0-9]{10}"'
```

Si la página tiene **más de 24 horas**, el nonce está vencido.

## El arreglo

1. **Purgar la caché** — inmediato y reversible, pero dura solo 24 h
2. **Bajar el TTL público a menos de 24 horas** (12 h va sobrado) — este es el de fondo
3. Alternativa mejor: usar **ESI** de LiteSpeed para que el nonce se sirva dinámico

**Estado al 24-ago:** propuesto a Connie (msg 328), **esperando su OK**. No se tocó
nada — rige [[congelar-cambios-viaje-china]]. Relacionado:
[[litespeed-cachea-la-api-rest]], que es el mismo plugin mordiendo por otro lado.
