# Sudtec — meta descripciones y alt de productos

*Pedido de Connie el 18-ago-2026 (msg 83). **Auditoría hecha, nada escrito
todavía** — el sitio es producción y espera su OK.*

## El tamaño real del trabajo

Catálogo leído entero por la API de WooCommerce: **307 productos**
(300 publicados, 5 borradores, 1 pendiente, 1 privado).

### Meta descripciones (Rank Math, meta `rank_math_description`)

| | |
|---|---|
| Productos **con** meta description | **127** |
| Productos **sin** meta description | **180** |
| Sin meta **title** (`rank_math_title`) | 258 — *no lo pidió, pero es el mismo trabajo* |

**Con qué material se puede escribir cada uno de los 180:**

- **76** tienen **descripción corta** — es la mejor base, ya está redactada.
- **103** no tienen corta pero **sí descripción larga** con características,
  medidas y normas.
- **1 solo** producto no tiene ningún texto: habría que escribirlo con el nombre
  y la categoría, o preguntarle a Sudtec.

> O sea: **179 de 180 tienen fuente real**. No hay que inventar nada.

### Alt de imágenes (meta `_wp_attachment_image_alt`)

| | |
|---|---|
| Imágenes asociadas a productos | 730 (**658 únicas**) |
| **Imágenes sin alt** | **509 asignaciones · 469 únicas** |
| Productos sin ninguna imagen | 6 |

Los nombres de archivo son **inservibles** para SEO y accesibilidad:
`WhatsApp-Image-2026-02-18-at-17.08.16.jpeg`,
`e494ab29-24b5-4dbe-b0f5-dcc377aaff75-scaled.webp`. Por eso el alt aquí sí
cambia algo real.

## Un dato que apareció de paso

El sitio **tuvo Yoast antes de Rank Math**: quedan 96 `_yoast_wpseo_metadesc` y
otros metas huérfanos. Se revisó si servían para rellenar los que faltan:
**0 productos** sin Rank Math tienen texto de Yoast aprovechable. No hay atajo
por ahí, pero tampoco estorban.

## Cómo se escribirían (criterio propuesto)

**Meta descripciones**
- 140-155 caracteres, con el **nombre del producto** y su **uso real**.
- Sacadas **solo del texto que ya tiene el producto**. **Nada de inventar
  certificaciones, normas ni plazos** — es la misma regla que dejó la auditoría
  de anuncios de agosto, donde aparecieron 3 claims sin respaldo en el sitio.
- La tienda es de **cotización**, no de venta directa: el cierre natural es
  «cotiza», no «compra».

**Alt**
- Describe **lo que se ve**, no una repetición de la keyword.
- Cuando un producto tiene 6 fotos casi iguales, los alt **varían** (producto
  completo, detalle, en uso…). Repetir el mismo texto 6 veces es peor que nada.

## Estado

🟢 **Piloto de 5 productos hecho y verificado el 18-ago.** Ver abajo.

### (histórico) Esperando OK de Connie — Propuesto: piloto de **5 productos** primero, se
los muestro, y recién con su visto bueno va la tanda completa.

**Vía técnica ya verificada de lectura:** `wc/v3/products` (307 leídos sin
problema). La escritura sería `wc/v3/products/<id>` con `meta_data` para la
descripción, y `wp/v2/media/<id>` con `alt_text` para el alt. **Falta probar la
escritura** — se probará en el piloto, no en masa.


---

# Piloto (5 productos, 12 imágenes) — 18-ago-2026

Connie aprobó el piloto (msg 85). **Escrito y verificado en la página pública.**

## Lo que se escribió

| Producto | Meta description | car |
|---|---|---|
| **11206** Set Alzaprima Mighty Strut | Set Mighty Struts de 2 alzaprimas de rescate a batería para estabilizar y elevar cargas en emergencias técnicas, sin hidráulica externa. Cotiza en Sudtec. | 154 |
| **11201** Botas Lytos FR-1406 | Botín Lytos FR-1406 para bomberos, certificado EN 15090 F2A HI3, con puntera de fibra 200J, cierre rápido BOA y suela nitrílica SRC. Cotiza en Sudtec. | 150 |
| **8023** Casco Schuberth F220 | Casco Schuberth F220 fotoluminiscente con visor integrado, norma EN 16471 y aislación eléctrica E2/E3, para incendio estructural, forestal y rescate. | 149 |
| **8027** Guantes Penkert Flash Long | Guantes de bombero Penkert Flash Long en cuero flor ignífugo con aislación térmica Needlona, certificados EN 659 y EN 420. Cotiza en Sudtec. | 140 |
| **8019** Botas Jolly 9016/A | Bota estructural Jolly 9016/A Leather EVO, norma EN 15090 F2A HI3 CI AN SRC, con puntera 200J y suela de nitrilo resistente a 300 °C. Cotiza en Sudtec. | 151 |

Las 5 entre **140 y 155 caracteres**, y **cada dato sale del texto del propio
producto** — ninguna norma ni certificación inventada.

12 alt escritos. **Se descargaron y se MIRARON las 12 imágenes** antes de
redactar: por eso dicen lo que de verdad se ve (un poste caído sobre un auto, una
camioneta encaramada, la suela vista desde abajo) y no una repetición del nombre.

## ⚠️ La trampa de este sitio, confirmada — pero no es Elementor

La API respondió **200** en las 17 escrituras… **y la página pública seguía
mostrando la descripción vieja**. Ojo: **no era Elementor**. La cabecera lo
delató:

```
x-litespeed-cache: hit
```

Era **LiteSpeed Cache** sirviendo una copia guardada. Repitiendo la llamada con
un parámetro que evita la caché (`?nocache=...`) aparece **todo correcto**:

```
<meta name="description" content="Botín Lytos FR-1406 para bomberos, certificado
EN 15090 F2A HI3, con puntera de fibra 200J, cierre rápido BOA y suela nitrílica
SRC. Cotiza en Sudtec.">
alt="Par de botas Lytos FR-1406 negras con cierre rápido BOA y detalles amarillos reflectantes"
alt="Suela nitrílica antideslizante de la bota Lytos FR-1406 vista desde abajo"
```

> **Regla para las próximas tandas:** en Sudtec, verificar la página pública
> **siempre con cache-buster**. Sin eso, un cambio correcto parece fallido y uno
> fallido parece correcto.

**No se puede purgar la caché desde la API:** LiteSpeed expone rutas REST
(`/litespeed/v1/…`) pero **ninguna de purga**. Hay que hacerlo desde el panel de
WordPress, o esperar a que la caché expire sola.

## Vía técnica, ya probada de escritura

- **Meta description:** `PUT wc/v3/products/<id>` con
  `{"meta_data":[{"key":"rank_math_description","value":"…"}]}` → 200 y persiste.
- **Alt:** `POST wp/v2/media/<id>` con `{"alt_text":"…"}` → 200 y persiste.

## Lo que falta y cuánto pesa

- **175 meta descriptions** restantes. Es el tramo rápido: el texto fuente ya
  está en cada producto.
- **457 alt** restantes. **Éste es el tramo lento**, porque hacerlo bien exige
  abrir cada imagen y mirarla. A ojo son varias tandas.

**Detectado de paso:** entre las imágenes que *sí* tienen alt, varias lo tienen
pobre — solo el nombre del producto (`Botas Lytos FR-1401`) o basura de la subida
(`Untitled (500 x 350 px) (1)`). No entra en el conteo de «faltantes», pero
conviene saberlo.


---

# Tanda de 50 — 18-ago-2026, 15:29

Connie pidió (msg 89) **avanzar de a 50 y preguntar antes de seguir**, para no
gastarle la cuota. Queda como preferencia fija en `memory/cuota-y-tandas.md`.

**50 meta descripciones escritas y verificadas.** Todas releídas por API (0
vacías) y dos comprobadas además en la **página pública con cache-buster**.

| | |
|---|---|
| Sin meta al empezar | **180** |
| Piloto | 5 |
| Esta tanda | **50** |
| **Hecho** | **55** |
| **Falta** | **125** |

Los ids exactos, en `seo-productos-hechos.json`.

**Qué cubrió:** linternas ATEX, la familia completa de botas Lytos FR-1401 a
1406, los parches VETTER Magnaseal, toda la línea AWG de espuma, pitones y
accesorios, y los equipos CAFS (MFU, VARIO, HiCAFS, HiGUARD).

**Dónde hubo que estirar el texto:** los productos CAFS traen como única fuente
una frase de una línea («Extintor de Alta Presión Robusto y Versátil – Ideal para
Brigadas Profesionales»). Con eso no se llega a 140 caracteres sin inventar, así
que se completó con el encuadre de la tienda («Cotízalo en Sudtec, especialistas
en equipos de emergencia»), **sin agregar ni una especificación que no estuviera
en la ficha**.

## 🔎 Productos duplicados detectados de paso

- **AWG Accesorio de espuma Turbo Strike** existe **tres veces**: ids `10433`,
  `10365` y `10363`, con el mismo texto y distintas categorías.
- **AWG Turbo-Spritze 2750** aparece dos veces, en Storz B (`10346`) y Storz C
  (`10343`) — eso sí tiene sentido, son acoples distintos.

Se les escribió meta description **diferenciada** a los tres Turbo Strike para que
no compitan entre ellos, pero **el duplicado de producto sigue ahí** y es decisión
de Sudtec si se unifican.
