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

**26-ago-2026** (27-ago en China) — Viaja de **Chongqing a Zhangjiajie** en el
tren **G2445**, sale **09:52** de <code>重庆东站</code> (Chongqing **Este**, la
estación nueva del sur-oriente, no la Oeste ni la Norte), puerta **28B**, llega
**11:58** a <code>张家界西站</code>. Localizador `E9W7045790`.
**Lección que casi me cuesta caro:** el puente marcaba 19:44 y el pasaje decía
«jue 27», así que parecía que era al día siguiente — pero para ella eran las 07:44
del jueves y el tren salía **en dos horas**. Ver [[hora-de-connie-no-la-mia]].

**27-ago-2026** — Ya está en **Zhangjiajie** (llegó 11:58, tren G2445 desde
Chongqing). A las 18:25 de allá preguntó qué ver esa noche. Le mandé: **天门狐仙**
(20:00, en 永定区 o sea la ciudad, 238 ¥ ≈ $33.000), el **天门山 iluminado**
(18:00–19:30, gratis), **大庸古城** —reabrió en julio-2026, entrada gratis— con
**南门口美食街** al frente, y **三下锅** en <code>胡师傅三下锅</code> (子午路).
**魅力湘西** (19:30) queda en **武陵源**, a 40 min, así que solo sirve si se alojó allá.
**Contestó (msg 467)**: se aloja en el **Yunmei Bieyuan Hotel**, No. 1, Lane 2,
<code>双拥路</code>, barrio <b>南庄坪</b>, <b>永定区</b> — o sea la **ciudad**, no
武陵源. Con eso 魅力湘西 quedó descartado (está en Wulingyuan) y todo lo demás sirve.
Datos útiles de ese barrio: <code>老七三下锅</code> le queda **a pasos** (frente al
condominio 雅典国际); al 天门狐仙 son 10–20 min en taxi y **los hoteles gestionan una
furgoneta ida y vuelta por 20 ¥** (≈ $2.700); 大庸古城 está en 解放路 152, ~10 min,
gratis y abierto hasta tarde.
**Queda preguntado**: cuántas noches se queda en Zhangjiajie, para adelantarle los
panoramas sin que tenga que pedirlos.

Después mandó una captura de **高德地图** preguntando «¿y esto qué es?»: era el
**七十二奇楼** (<code>武陵山大道1号</code>), la **casa palafito 吊脚楼 más alta del
mundo**, récord Guinness, **109,9 m**, arquitectura **tujia**. Abre **10:00–22:00**,
sesión de noche desde **16:30**, entrada **88 ¥** ≈ **$12.000**, lo bueno después de
las **19:00**, fogata (篝火晚会) hasta **22:45**. **Circula que de noche es gratis y
NO lo es** — se lo advertí por si se lo ofrecen en la puerta.
Le recomendé **este** por sobre el 天门狐仙 para esa noche: un tercio del precio, sin
hora fija, y el 天门狐仙 se da **todas las noches hasta diciembre**, así que no se
pierde. En su propia captura salían <code>灶灶土钵菜·三下锅 (72奇楼店)</code> (el plato
típico, ahí mismo) y <code>茶颜悦色</code>, la marca de té con leche de Hunan.

**Patrón del viaje que ya se repitió tres veces:** manda una foto o una dirección y
espera que YO ubique el lugar, lo verifique y le diga si vale la pena — no que le
describa la foto. Verificar con búsqueda antes de responder, porque dos veces lo que
yo "sabía" estaba desactualizado (大庸古城 quebró en 2024 y reabrió en julio-2026).
Se aplicaron las dos reglas del viaje: nombres en **caracteres chinos** para
mostrarle al taxi, y precios en **¥ y CLP en la misma línea**.
Regresa el **18-sep-2026**.

**27-ago-2026, noche** — Fue al **七十二奇楼**, o sea siguió la recomendación.
Desde adentro mandó la foto del cartel de programación preguntando dónde era el
show de las 19:55. Eran las **19:49** en China: **6 minutos**. Respondí corto y
primero la ubicación: 《奇楼掌灯》 (*Qilou Zhangdeng*, «el encendido de las
linternas de la torre»), en **湘西老街** (*Xiangxi Laojie*, «Calle Antigua de
Xiangxi»), con la frase <code>湘西老街怎么走？</code> para preguntarle a
cualquiera. Después, en un segundo mensaje, le traduje la programación completa.

**Lo que hay que retener del cartel** (sirve si vuelve a un parque chino):
· **必看** = imprescindible · **推荐** = recomendado · **非遗** = patrimonio inmaterial
· El cierre grande es 《篝火盛典》 («gran ceremonia de la fogata»), **21:30**, desfile
  que termina en 篝火广场
· **山歌醉 es local de consumo**: para ver el show de ahí hay que pedir algo

**Lección de forma, no de contenido:** con 6 minutos encima, lo correcto fue
**partir por el dato que ella necesitaba para moverse** y dejar todo lo demás
para un segundo mensaje. La respuesta completa habría llegado tarde aunque
fuera mejor.
