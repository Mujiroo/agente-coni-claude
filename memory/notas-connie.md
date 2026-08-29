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

**27-ago-2026, 09:30** — El cron de vigilancia de cambios dio **HAY-QUE-AVISAR**:
la cuenta de Sudtec lleva **5 días seguidos peor** que la base — **3,4 conv/día**
contra 4,7 (**−27%**) y **CPA $3.084** contra $1.675 (**×1,84**). En 7 días:
**$74.012 por 24 conversiones**, cuando a la tasa anterior esa plata compraba ~44.
Grupo Botas: **63 impresiones, 1 conversión**.

**El matiz que casi me como:** la racha mala empieza el **23-ago** y el ruteo de
botas se cambió el **24-ago 20:10**. El deterioro **precede** al ruteo, así que
atribuírselo entero habría sido falso. Se lo dije así.

**Defecto propio que encontré y le confesé:** el cron que dejé para el 29-ago mide
**solo impresiones** con umbral 20, y Botas ya lleva 63 → caería en la rama (B) y
**no revertiría solo**, pese a tener 1 conversión. La regla mide alcance, no
negocio. Está anotado en `memory/estado/alerta_ads_27ago.json`.

**Estado: esperando su OK** (msg 489). No se tocó nada.

**28-ago-2026 (11:46 en China)** — Mandó el mapa de **天门山 (Tianmen Shan)**
preguntando **cuál es la opción para caminar menos**. Va de 20 semanas y el 24-ago
tenía los pies muy hinchados, así que la pregunta es de fondo, no de comodidad.

**El dato que estaba en su propio mapa y había que leer:** el título decía
*«durante la suspensión del tramo alto del teleférico»*. **El teleférico ya no
llega a la cumbre** — en obras desde el 6-nov-2025, ~1 año. Por eso las rutas del
mapa se ven raras. Sin eso, cualquier consejo de «sube en teleférico» era falso.

**Lo que le dije que importa de verdad, más que la línea:**

1. **Pagar los dos ascensores dentro del cerro**: el de **5 niveles** hasta la cueva
   天门洞 (**32 ¥** ≈ $4.400) — que evita los **999 escalones** — y el de **7
   niveles** de la cueva a la cumbre. Con los dos, sube sentada.
   *(El «32» anotado a mano en su mapa era justo ese precio.)*
2. **Saltarse las pasarelas de vidrio**: 西线, 东线 y 鬼谷栈道 son **kilómetros** de
   pasarela colgada. **Ahí está toda la caminata real**, y es opcional.

**Ruta más corta:** la que sube por el **天门洞快线索道** (cable exprés directo a la
cueva) = **línea C**, la única que la suspensión no afectó. Alternativa: **línea A**
(teleférico a estación media + bus por las 99 curvas; el bus también es sentada).

**Detalle que le marqué:** en el mapa había un **16:00** escrito a mano. Le dije que
pregunte si es la hora del **último descenso** — enterarse de eso ya estando arriba
sería un problema serio en su estado.

Frase que le mandé aparte para la boletería:
`我怀孕了，想走路最少。请问哪条线最轻松？我要坐扶梯，不爬999级台阶。最后一班下山几点？`

**Lección:** el dato decisivo estaba **impreso en la foto que ella me mandó**, no en
lo que yo sabía de Tianmen. Leer el material antes de responder desde la memoria.

**29-ago-2026 (07:59 en China)** — Mandó el mapa del **张家界国家森林公园**
(Zhangjiajie National Forest Park, distinto del Tianmen del día anterior)
preguntando **cuánto se camina** y **dónde está el ascensor de las montañas de
Avatar**.

**El dato de la leyenda que resuelve la pregunta sola:** los números impresos
sobre los senderos son **minutos de caminata** (徒步游道/分钟). Con eso ella puede
estimar cualquier tramo sin preguntarme.

**La respuesta corta:** el ascensor es el **百龙天梯 (Bailong Tianti)**, 326 m en
menos de 2 minutos, de pie. Ruta con caminata casi nula: entrar por **武陵源门票站**
(no por la entrada de abajo) → bus verde a la parada **百龙天梯** → ascensor → otro
bus a **袁家界 (Yuanjiajie)**, que es donde están las montañas de Avatar.

**Dónde está la caminata de verdad:** el circuito de miradores de Yuanjiajie, ~2 h
plano y pavimentado. Versión corta ~1 h: solo **天下第一桥** y **哈利路亚山**,
saltándose 后花园 y 迷魂台.

**Lo que le dije que NO intentara el mismo día**, porque cada uno es otro cerro con
su propio teleférico: 金鞭溪 (70 min de caminata), 黄石寨, 天子山, 杨家界.

**Precaución con mecanismo concreto (no acumulé otras):** ir temprano, porque la
fila del ascensor en temporada llega a una hora y **estar parada en la cola cansa
más que caminar** a las 20 semanas.

**Hora impresa en su mapa:** `pm 6:30 [最晚]`, último bus del parque a Wulingyuan.
Le dije que preguntara igual por la última bajada del ascensor, que suele ser antes
— mismo patrón que el 16:00 escrito a mano en el mapa de Tianmen.

**Se repite la lección y ya van dos días seguidos:** el dato que ordena la respuesta
estaba **impreso en la foto que ella mandó** (la leyenda de minutos, la hora del
último bus), no en lo que yo sabía del parque. Leer el material primero.

**Limitación del contenedor que apareció acá:** no hay **PIL, ImageMagick, ffmpeg ni
pip**, así que **no puedo recortar ni ampliar una foto**. La herramienta Read la
muestra completa y nada más. Si un detalle no se lee a resolución completa, hay que
pedirle a ella una foto más cerca en vez de intentar procesarla.

**29-ago-2026 (17:48 en China)** — Preguntó **«¿qué hay en la Plaza Zhongshan?»**
estando en Zhangjiajie.

**Verificado antes de responder: en 永定区 NO existe ninguna 中山广场.** La 中山广场
famosa de China es la de **Dalian**, a 2.000+ km. Responder desde lo que "suena
conocido" habría sido mandarla a un lugar que no está.

**Lo que sí hay y se lee casi igual en español:** **中商广场** (*Zhōngshāng*, no
Zhōngshān), el mall del centro en <code>解放路151号</code>, sábado hasta las **22:00**.
Y la plaza peatonal que la gente sí camina: **人民广场**, 200 m entre 回龙路 y 解放路,
entrada libre. Los dos a ~3 km de su hotel en 南庄坪 (~10 min en taxi).

**Confirmó (msg 541) que era ese**, y preguntó qué hay adentro. Es el mall del
centro: **46.000 m²** desde 2016, cinco sectores, sábado hasta las 22:00. Le
destaqué **屈臣氏 Watsons** (farmacia-perfumería, lo más útil en su estado), los
restaurantes del **F4** (`禾港餐厅`, `赣湘苑`) y el patio de comidas. Le dije la
expectativa real sin adornar: **4,1 con 19 reseñas**, marcas normales de ciudad
chica, sirve para comprar y comer bajo techo, **no es paseo turístico**. Y que lo
puede juntar con **大庸府城** y el paseo **人民广场**, que quedan al lado.

**Lección nueva del viaje:** un nombre chino romanizado puede colisionar con otro
casi idéntico (**山 shān** vs **商 shāng**). Cuando el lugar "no aparece", antes de
decir que no existe conviene buscar el vecino fonético — acá el vecino era el
destino real y probable.

**Trampa de marca que le advertí:** el local de té del F3 dice `茶颜观色` y **no es**
el `茶颜悦色` de Hunan que le había mostrado en el 72奇楼 — es la imitación, condenada
por competencia desleal a pagar **1,7 millones ¥**. Los dos se leen casi igual, igual
que 中山/中商. **Segunda colisión de nombres del mismo día:** en China conviene
comparar el carácter, no el sonido.

**29-ago-2026 (20:02 en China)** — Mandó la foto del cartel de un puesto de comida
preguntando **«¿qué es esto, el 14?»**.

**El de 14 ¥ (≈ $1.900) es 牛肉卤粉** — fideos de **arroz** (米粉) en caldo con carne
de vacuno estofada en 卤水, huevo y cebollín. El cartel lo marcaba <code>必点</code>
(imprescindible) y <code>张家界美食</code>: es **el** plato típico de la ciudad. El
local es **庸城巷子** (庸城 = 大庸, nombre antiguo de Zhangjiajie).

**Lo que agregué y no estaba en la foto:** el plato va **麻辣** (picante + hormigueo
de pimienta de Sichuan), y a 20 semanas eso es reflujo. Le pasé la frase
<code>我要牛肉卤粉，微辣，谢谢</code>.

**Precaución de embarazo, una sola:** el 粉 sale hirviendo y está bien; los **卤味
fríos** del mostrador (orejas, menudencias a temperatura ambiente) mejor no. Regla
corta que le di: **caliente sí, frío del mesón no.**

**Lo que NO afirmé:** el plato de 12 ¥ del lado salía cortado en la foto. Le dije que
empieza con 猪 (cerdo) y que *si* es 猪耳 es oreja — sin darlo por cierto. Mismo
criterio que con la foto ampliada: no hay PIL ni ImageMagick para recortar.

**Mismo momento (41 s después)** — Pidió la frase en chino: *«¿puede no ser picante?
Estoy embarazada»*. Estaba en el mesón, así que fue solo la frase, en bloque
<code> y sin rodeos:
<code>我怀孕了，可以做不辣的吗？不放辣椒和花椒，谢谢！</code>
Más el plan B si el caldo ya viene picante (<code>那请不要另外加辣椒油</code>) y la
de confirmar antes de recibirlo (<code>这个不辣吧？</code>).

**Patrón que ya es regla:** cuando está frente a alguien, quiere **la frase lista
para mostrar en pantalla**, no una explicación. Frase sola, en <code>, con la
traducción en cursiva debajo — y anticipar la respuesta que le van a dar.

**29-ago-2026 (20:06 en China)** — Foto de una bebida en un quiosco: *«¿y eso qué es?»*.
Era <code>统一 阿萨姆原味奶茶</code> — **Uni-President**, té con leche Assam, **500 ml**,
de las bebidas más comunes de China.

**Dato que estaba impreso y se pudo leer (sigue el patrón del viaje):** el código de
la tapa decía fabricación **24-jun-2026** y vencimiento **23-mar-2027**.

**Lo que le marqué como relevante y lo que NO:**
· **Sí importa el azúcar** — 40-50 g por botella (~10 cucharaditas), 250-300 kcal.
  Entre las **24 y 28 semanas** le toca el test de tolerancia a la glucosa.
· **No importa tanto la cafeína** — tiene, por el té negro, pero muy poca frente al
  límite de **200 mg/día** en embarazo. Dije eso en vez de alarmar por todo.
· **Salida concreta:** la misma marca tiene versión **无糖** (sin azúcar), con la
  frase <code>有无糖的吗？</code> para preguntarla.

**Criterio que quiero repetir:** con ella, una sola precaución que de verdad mueva la
aguja, y decir explícitamente qué **no** es problema. Una lista de miedos no sirve.
