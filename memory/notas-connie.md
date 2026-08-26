# Notas personales de Connie

Acá va lo que ella me cuenta al pasar y que no debe perderse: compromisos,
fechas, decisiones, recordatorios, preferencias de trabajo.

Formato: una entrada por línea o bloque, **con fecha absoluta** (nunca «mañana»
ni «la próxima semana» — eso deja de significar algo al día siguiente).

---

*(sin entradas todavía — 17-ago-2026)*

**18-ago-2026** — Pidió auditoría de políticas de Meta y Google Ads para SUDTEC.
Le llega información de políticas desde su trabajo y me la reenvía en bloque para
que la aplique. Vale la pena guardarla: ver `clientes/sudtec/politicas-2026.md`.

**18-ago-2026** — Queda claro que **no hay integración de Meta Ads**. Cada vez que
pida algo de Meta hay que decírselo en la primera línea, no al final: de Meta solo
tenemos Instagram por Composio (publicar y DMs), que no toca el administrador de
anuncios. Conectarlo depende de Nicolás.

**18-ago-2026** — Su **trabajo principal**: es **SEO de Nivea y Eucerin LATAM en
Cheil** (agencia), a cargo de **Colombia, México, Chile, Ecuador, Guatemala y
Perú**. Traduce, localiza y optimiza contenido que le llega en inglés, con una
versión distinta por país para evitar duplicado, y relocalizando los enlaces
internos a cada sitio local. Todo el detalle en
`clientes/cheil-nivea-eucerin/estado.md`. Pidió guardarlo porque «eventualmente»
me pedirá ayuda: cuando eso pase, **leer esa carpeta antes de responder**.

**19-ago-2026** — **Viaja el 21-ago a China** y pidió que yo le avise sus tareas
con fecha, porque no va a revisar el calendario. Quedaron tres avisos montados
(4, 11 y 14 de septiembre). El detalle que importa: **China va 12 horas adelante
de Chile**, así que los crons disparan el día anterior a las 21:00 de Chile.
Todo el razonamiento está en `memory/recordatorios-viaje-connie.md`.
**Regresa el 18-sep-2026 a las 00:00.**

**24-ago-2026** — Está en **Chongqing** (China) y preguntó dónde comprar sin
«precio turista». Le mandé los barrios locales (Guanyinqiao, Chaotianmen
mayorista en Chayuan, Sanxia Guangchang en Shapingba, Nanping/Yangjiaping), qué
evitar (Jiefangbei, Hongya Dong, Ciqikou) y cómo regatear. **Aprendizaje para
próximos pedidos del viaje: mandarle los nombres en caracteres chinos**, así se
los muestra al taxi o los pega en el mapa — sin eso el dato no le sirve en
terreno. Vuelve el **18-sep-2026**; ver [[recordatorios-viaje-connie]].

**24-ago-2026** — No sabía qué era **RMB** (le apareció en una etiqueta de Miniso).
**Para lo que queda del viaje: cuando le mencione un precio chino, convertirlo a
CLP en la misma línea**, no dejarle la conversión a ella. Regla al paso que le di:
**RMB × 1,4 leído en miles** (el 24-ago el cambio real era 1 RMB = 137 CLP).


**25-ago-2026** — Pidió ayuda para comprar por **Taobao** estando en China. Su
traba: puso la moneda en USD y solo le ofrecía Australia. **La causa no era la
moneda sino la región**: la cuenta estaba en modo internacional (淘宝海外), que
amarra la moneda al país de despacho. Le di los pasos para dejarla en 中国大陆 +
人民币, y los dos requisitos que sí frenan a un extranjero: **teléfono +86** (sin
él el repartidor no puede entregar) y **Alipay 支付宝 con tarjeta extranjera**
verificada con pasaporte.
**Queda abierto**: le ofrecí mandarle los **términos de búsqueda en caracteres
chinos** de lo que quiera comprar, porque buscar en español en Taobao no devuelve
nada. Si vuelve con una lista, eso es lo que espera. Precios siempre en ¥ y CLP en
la misma línea (ver la nota del 24-ago).

**26-ago-2026** — Pidió el estado de cotizaciones y campañas de Sudtec. Quedó
**una decisión abierta suya**: agregar 3 keywords negativas a *Campaña Sudtec*
—«cotona ignífuga», «traje encapsulado» y «epp»—, que en la semana del 24-ago
gastaron **$3.143 sin una sola conversión**, y cuyos dos primeros términos **no
tienen ningún producto en el catálogo** (verificado con `sudtec_wp.py productos`).
Le dije que puede esperar a que vuelva (18-sep) porque los cambios están
congelados; **si contesta que sí, hacerlo; si no contesta, recordárselo al
regreso**. Ver [[congelar-cambios-viaje-china]] y el detalle en
`memory/estado/negativos_pendientes.json`.
