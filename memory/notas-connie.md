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

**29-ago-2026, 09:30** — La vigilancia de cambios dio **HAY-QUE-AVISAR** por 7ª
corrida seguida. Antes de reenviarle el texto del script, se desglosó día por día.

**Dos cosas que hay que saber de ese script, para no leerlo mal:**
1. `malos_seguidos: 7` **no son 7 días malos distintos** — son **7 corridas** en que
   la ventana móvil de 7 días quedó bajo el umbral. Los mismos días malos se
   recuentan cada día.
2. `LAST_7_DAYS` de Google Ads **excluye hoy**, así que la ventana era **22-28 ago**.
   Verificado cuadrando las cifras: 22 conversiones y 73.742 CLP dan exactamente el
   3,14 conv/día y el CPA 3.352 que imprimió. **El día parcial de hoy no contamina.**

**El desglose diario (20-29 ago), que es lo que el agregado escondía:**
20:2 · 21:4 · 22:3 · 23:3 · **24:7** · 25:4 · 26:3 · **27:1** · **28:1** · 29:0 (en curso)

**Lo que eso cambia:** los dos peores días de la racha son **27 y 28**, justo los de
**después** del revert. O sea el revert **no levantó** — pero hay **un solo día
completo** post-revert y el rango diario va de 1 a 7, así que concluir ahora sería
falso. Se lo dije con ese matiz explícito.

**Dato que nadie había mirado:** el gasto está **clavado en ~10.500 CLP/día todos los
días**. El presupuesto se gasta entero siempre; lo que varía es la conversión. **El
problema no es la inversión, es la tasa de conversión.**

**No se tocó nada.** Propuesta: esperar el veredicto ya agendado del **31-ago**.

**29-ago-2026 (19:20 Chile = 30-ago 07:20 en China)** — Pidió anotar en el calendario
que el **1-sep es el cumpleaños de Felipe** y que **debe llamarlo**.

Se hicieron **las dos cosas**, según la regla del 20-ago:
· **Evento** en su Google Calendar, todo el día del 1-sep, **sin invitados** (id
  `68iathf5k0f1vn40s6vcupqn44`). Sin invitados a propósito: así no le llega aviso a
  ningún tercero.
· **Cron** de Telegram a las **10:05 de Chile = 22:05 en China** (1-sep, Chile todavía
  en UTC-4; el horario de verano parte el 6-sep). Verificado con `zoneinfo`.

**Por qué 10:05 y no 10:00:** a las 10:00 del 1-sep ya corre el recordatorio del cobro
de Google Workspace. Separarlos 5 minutos evita que le lleguen dos mensajes pegados
sobre temas distintos.

**No consta quién es este Felipe.** El único Felipe en los archivos es *Felipe Salce*,
gerente de marketing de MTS, y casi seguro **no** es él: el pedido es personal. No se
lo pregunté porque no cambiaba nada del trabajo.

**30-ago-2026 (07:23 en China)** — Llega a **芙蓉镇 (Furong Zhen)** y tiene **solo ese
día**. Pidió qué hacer.

**Lo que se puso primero, porque es lo que le arruina el día:** la entrada son
**108 ¥** ≈ **$14.800** y se reserva por **mini-programa de WeChat**, con cupo que en
temporada **se agota**. Si no la trae comprada, a la boletería temprano por los cupos
liberados (<code>今天还有余票吗？</code>). Horario **07:30-23:00**.

**Dato que cambia cómo arma el día:** la entrada **incluye los shows de día y de
noche**, sin pago aparte — o sea conviene quedarse hasta la noche.

**Lo imperdible:** el **米豆腐** (tofu de arroz) en un <code>刘晓庆米豆腐</code> junto
al **牌坊** — el pueblo se llamaba 王村 y se renombró por la película de 1986, de ahí
la fama del local. Más el mirador de la cascada (**60 × 40 m**, dos saltos),
**五里长街** y el **土司行宫**.

**La advertencia que importaba de verdad:** el pueblo está construido **sobre la roca,
encima de la cascada** — escaleras y losa **mojada** por la humedad del salto. A las
20 semanas eso pesa más que el precio. Le recomendé pagar el **carro eléctrico + bote,
68 ¥** ≈ **$9.300**, que normalmente uno se salta: en su caso son piernas ahorradas.

**Lo que NO afirmé:** no pude confirmar que haya ascensor. En vez de suponerlo (como
casi pasó en Tianmen), le di la frase para preguntarlo:
<code>有没有电梯？我怀孕了，不能爬很多台阶</code>

**Preguntó qué era ese carro + bote (msg 555), y al verificarlo apareció el dato
bueno:** los **68 ¥** son el **transporte del recinto**, no un paseo extra. Se vende
como <code>车进船出</code> (*entras en carro, sales en bote*): **环保车** desde la
entrada hasta **荷花池广场**, recorrido a pie por el pueblo **pasando por detrás de la
gran cascada** (穿过大瀑布), y salida en **bote** por el lago del **酉水**.

**El argumento real para ella no es el paseo, es que el bote ES la salida** — sin eso
hay que devolverse a pie por donde se subió. Ese tramo de vuelta era el problema.
Frase: <code>我要环保车加游船的票，车进船出</code>

**Y el paso detrás de la cascada tiene el suelo mojado siempre** — ahí es donde hay
que cuidar el piso, no en la calle de losas.

**Y después dijo dónde se aloja (msg 557), que cambió el plan:**
<code>土王行宫·八部堂</code> (*Tuwang Palace · Eight Halls*), **dentro del 土王行宫** —
o sea **duerme adentro de una de las atracciones** que le había listado. Teléfono
**0743-5854999**.

· **26 habitaciones** colgadas del acantilado sobre los dos saltos, mirando al 酉水.
· Cada pieza con **balcón propio para ver la cascada**; las de **270°** son únicas.
· **Ve la cascada iluminada desde su balcón**, sin caminar, y el paisaje nocturno
  **no cobra entrada aparte**.
· **Hace traslado a sus huéspedes**, a 6 min del terminal de buses — eso resolvía el
  problema real, que era llegar con la maleta.

**Le corregí lo del bote**: el argumento de «el bote es la salida» **ya no aplica**
si duerme adentro del pueblo. Pasa a ser paseo opcional, y el carro solo sirve si el
hotel no la va a buscar. Cambiaba una decisión de plata, así que se dijo explícito.

**Mensaje que le pasé para el hotel** (traslado + ascensor + comprar la entrada ahí,
que sale algo más barata que en línea). Y una sola advertencia: **pieza con vista a la
cascada es pieza con ruido de cascada** — tapones, <code>请给我耳塞</code>.

**Lección que se repite:** el dato de dónde se aloja reordenó medio consejo. Cuando
hay un viaje en curso, **preguntar o esperar el alojamiento antes de armar el día**.

**30-ago-2026 (11:28 en China)** — Foto de un dulce morado con láminas de almendra:
*«¿qué son estos dulces de China?»*. Es **雪花酥** (*xuěhuā sū*, «crocante de nieve»),
de origen **taiwanés**, viral en China hace unos años.

**Composición:** marshmallow derretido + mantequilla + leche en polvo, mezclado con
**galletas de soda saladas** y frutos secos, prensado y cortado. El contraste
dulce-salado es la gracia. El **morado** es **紫薯** (camote morado) o **香芋** (taro)
en polvo, que reemplaza parte de la leche en polvo — frase para preguntar cuál:
<code>这是紫薯还是香芋味的？</code>

**Lo relevante para ella:** **no tiene huevo crudo** (el marshmallow es gelatina y
azúcar), la leche es en polvo y las galletas van horneadas. Todo cocido, nada que
cuidar.

**Criterio de tono:** el aviso del azúcar ya se lo había dado esa misma mañana con el
té con leche. Repetirlo habría sido machacar, así que fue una línea liviana y en
broma. **Una advertencia se da una vez.**

**30-ago-2026 (13:43 en China)** — Mandó el cartel de programación de shows de
芙蓉镇 y pidió **qué show ver y la rutina completa** del día.

**El dato que ordenaba todo y no estaba en su pregunta: hoy es DOMINGO.** El cartel
tiene filas condicionadas por día (周五 / 周六 / 周日至周四). El grande,
**花开芙蓉·锦绣未央** (21:30, en las **跳岩**), **solo va sábado y domingo** — o sea
justo hoy y mañana ya no. Eso definió la recomendación.

**Lo que aparece leyendo el TÍTULO del festival:** es el **13º 摸泥狂欢季**, la
«temporada del carnaval de **tocar barro**». Verificado: la gente se embarra con
**barro de tres colores**, hay **guerras de pistolas de agua** y bailes en montón
hasta las 24:00. Le dije que evite <code>芙蓉狂欢·情满泥水</code> y los **巡游**
(pasacalles): barro + agua + multitud = piso resbaloso, y va en la semana 21. Los
shows de escenario, todos; los de meterse al montón, no.

**La rutina se armó alrededor de un bloque de descanso de 18:00 a 19:45 en el hotel**,
aprovechando que duerme adentro del pueblo, y encadenando los shows con los lugares
que ya iba a visitar (el 16:30 es en el **铜柱园**, que es donde está el **溪州铜柱**
de su propio texto: show y visita en el mismo punto, cero caminata extra).

**Se le dio permiso explícito de saltarse cosas:** «prefiero que veas uno bien a que
llegues arrastrando a los dos». Con ella conviene decirlo, si no intenta hacer todo.

**Lo que NO afirmé:** las dos últimas filas del cartel se contradicen en los días
(21:30 vs 21:10). Le pasé la frase para confirmar en recepción en vez de elegir yo
una hora.

**Rareza del puente, anotada por si se repite:** el aviso de mensaje largo del msg 565
salió encabezado como *«Sebastian mando un mensaje LARGO»*, pero el archivo
`msgs/565.txt` decía **Constanza**. Se verificó en el archivo antes de responder. No
era un chat ajeno, así que no correspondía `[TG-ALERT]`.

**Cierre del día de Furong:** confirmó que **se va a las 10:00** del lunes 31-ago. Con
eso el show grande de las **21:30** entraba sin apretar (termina ~22:30, ~9 h de
sueño), así que se le dio luz verde y quedó la noche cerrada: **18:40** 巫傩绝技 ·
**19:30** la cascada iluminada desde su balcón · **20:00** fogata · **21:30**
锦绣未央 en las 跳岩. Se le marcó **cuál es la que se salta** si anda cansada (la
fogata), en vez de dejarla decidir con todo el cansancio encima.

**Traslado:** terminal a 6 min, salir 9:30. Check-out en China suele ser 12:00, así que
eso no la apura.

**Le OFRECÍ un aviso a las 9:00 de mañana y no lo dejé puesto.** Ella no lo pidió;
montar un cron no pedido es ruido. **Ofrecer y esperar el sí** — queda como criterio.


**30-ago-2026 (05:38 Chile / 17:38 en China)** — Mandó **la misma foto con dos
ediciones** (sesión de 汉服 en 芙蓉镇, con 帷帽 —el sombrero de velo— rosa y blanco)
y preguntó **cuál se veía más «estilo chino»**, más una descripción para abajo.

**El criterio que resolvió la comparación:** la diferencia no estaba en ella sino en
el **fondo**. La edición 1 tenía negros levantados y el verde lavado hacia el beige —
el filtro «film» de Instagram, que se lee **europeo**. La edición 2 dejaba el follaje
**verde profundo y oscuro**: eso es lo que construye el look 古风, porque replica el
**verde mineral** (石绿) de la pintura sobre seda con la figura clara brillando encima.
Se eligió la **segunda**.

Argumentos concretos que se le dieron, en vez de «se ve mejor»: con más contraste el
**rosa bordado se separa del blanco** (si no, todo se funde en un beige), **brillan
las cuentas** del 帷帽, y su cara queda como el punto más luminoso. *«La primera te
deja bonita pero plana; la segunda te deja dentro de la escena.»*

**Descripción propuesta:** «Salí a caminar por 芙蓉镇 y volví de otra dinastía» +
<code>一袭轻纱，半日千年</code> («un velo de gasa; medio día, mil años»), que es una
frase de registro 古风 y se lee bien para ojo chino. Se le dieron **dos alternativas
de tono** en vez de una sola opción, y los hashtags <code>#汉服 #古风 #芙蓉镇</code>
con el porqué: la encuentra gente de allá, no solo sus contactos de Chile.

**Lo que quedó como criterio:** cuando pida elegir entre dos ediciones, **nombrar la
variable técnica que las diferencia** (contraste, saturación del fondo, temperatura)
y no solo el veredicto. Así puede repetir el ajuste sola en la próxima foto.

**Mismo día, 05:40** — Eligió el caption «Salí a caminar…» y pidió **publicarlo en su
Instagram**. Quedó arriba: <code>instagram.com/p/DcqN6UmlXK_/</code>, con la segunda
edición, las dos líneas y los tres hashtags. La ruta técnica (Instagram no acepta
archivos locales: hay que pasar por una URL pública) quedó documentada en
[[instagram-publicar-ruta-drive]].

**Cómo se resolvió el margen del pedido:** ella aprobó el texto pero no dijo nada de los
hashtags, que yo había recomendado en el mensaje anterior. Se **publicaron incluidos** y
se le informó **textualmente qué quedó**, avisándole que se editan desde la app si los
quiere fuera. El criterio: los hashtags no son voz suya —no dicen nada en su nombre—,
son ruteo; y hacerla repetir un pedido por eso habría costado más que el ajuste.

**2-sep-2026 (19:58)** — Mandó la **cartola de su Visa Signature** en PDF y preguntó
*«por qué debí tanto si ya he abonado»*. La respuesta era simple una vez cuadrada:
**sí abonó 97 USD** (49 el 26-ago + 48 el 28-ago), pero **cargó 387,42** — 313,03 en
compras y **74,39 en un AVANCE EN EFECTIVO** en Chongqing el 26-ago. Saldo **290,42
USD**, con 2.712,56 de cupo libre.

**Lo que valía la pena decirle y no preguntó:** ese avance es **el movimiento más
grande de toda la cartola** y el **19%** de lo cargado, y a diferencia de una compra
**paga interés desde el día uno más comisión fija**. Además se le avisó que la cartola
dice **«no facturado»**: cuando llegue la factura vendrá **más alta**, porque ahí recién
se suman ese interés y esa comisión.

**Cómo se leyó el PDF:** no había con qué; se escribió `bin/pdf_texto.py`. Ver
[[leer-pdf-sin-herramientas]] — incluye la regla de **cuadrar el parseo contra los
totales impresos** antes de darle cifras.

