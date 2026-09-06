---
name: hong-kong-connie
description: Connie va a Hong Kong al final del viaje (preguntó el 4-sep-2026); las 9 tiendas Casetify y por qué Festival Walk es la que le sirve viniendo de Shenzhen.
metadata:
  type: project
---

**El 4-sep-2026 (msg 752, 20:51 de Hong Kong) preguntó *«dónde está la tienda de
Casetify en Hong Kong»*.** Es el primer indicio de que el viaje sigue a **Hong Kong**
después de Shenzhen ([[shenzhen-connie]]); vuelve a Chile el **18-sep**
([[recordatorios-viaje-connie]]).

## Casetify en Hong Kong

**Casetify es marca de Hong Kong**, así que no hay «la» tienda: hay **9 CASETiFY
STUDiO**. Las que le pasé, ordenadas por dónde esté:

- **Festival Walk** — Shop LG1-21, 80 Tat Chee Ave, **Kowloon Tong** · 11:00-21:00
- **Landmark** — Shop B18, B/F, Landmark Atrium, **Central** · 11:00-20:00
- **Causeway Place** — G/F, 2-10 Great George St, **Causeway Bay** · 11:30-21:30
- **K11 MUSEA** — Shop B122, 18 Salisbury Rd, **Tsim Sha Tsui** · 11:00-21:00
- **MOKO** — Shop M22, piso MTR, **Mong Kok**
- **apm** — C-31, 418 Kwun Tong Rd, **Kwun Tong**

**Lo que convirtió una lista en una respuesta útil:** viniendo de Shenzhen, el paso
fronterizo de **Lo Wu / Lok Ma Chau** deja en la **East Rail Line**, que para en
**Kowloon Tong** — y Festival Walk está conectado a esa estación. Es la única de las
nueve que no le cuesta un desvío. **Regla: cuando pregunta «dónde queda X» estando de
viaje, la respuesta se ordena por su ruta, no por la fama del local.**

**El dato que justifica ir a tienda** en vez de comprar online: en las STUDiO **imprimen
la carcasa personalizada en el local**.

**Hora:** preguntó **20:51 de Hong Kong** y casi todas cierran **21:00**, así que se le
advirtió que para ese día no alcanzaba. Hong Kong está en **UTC+8, igual que China**, así
que la regla de [[hora-de-connie-no-la-mia]] (Chile +12) sigue valiendo igual.

Fuentes: `casetify.com/visit-us/hk/*`.

## Precios (msg 754, «¿a cuánto están?»)

Rango oficial en HK: **HK$279 a HK$789** según modelo y diseño (**36-100 lucas**).
Por tipo: **Impact Case HK$500-550** · **Bounce HK$620** · **Ultra Bounce HK$780**;
las colaboraciones (Sanrio, Disney) van arriba del rango.

**El sitio no se deja leer:** `casetify.com` devuelve **402** a WebFetch y por `curl` la
página llega renderizada por JavaScript y **geolocalizada en USD** — las cookies de país
no la cambian. Las cifras salieron de la **lista en USD** (Impact desde US$65, Bounce
US$80, Ultra Bounce US$100) convertidas al **peg HK$7,8 por dólar**, y cuadran con el
techo de HK$789 reportado por prensa de Hong Kong. **No perder tiempo scrapeando ese
sitio la próxima vez.**

**Lo que le dije, más allá del número:** en tienda **cuesta lo mismo que online**, así
que lo que compra yendo es la **impresión personalizada en el local** y los **diseños
exclusivos de Hong Kong**. En HK **no hay IVA**: la etiqueta es el precio final.

**Y una línea de perspectiva**, porque venía de regatear relojes a ¥130-160: una carcasa
le sale **más que tres** de esos relojes. No es un reproche —es su plata— pero el dato le
sirve para decidir en el momento. Ver [[lewear-ht30-relojes]].

## Se va 2 días a Hong Kong y pidió plan (msg 758, 4-sep-2026)

Confirmado: **sábado 5 y domingo 6 de septiembre**. Preguntó *«me voy por 2 días a Hong
Kong, ¿qué puedo hacer allá?»* a las **09:55 de Hong Kong** del sábado.

**El plan se armó alrededor del embarazo y del calor, no alrededor de los panoramas.**
Va de **~22 semanas** ([[embarazo-connie]]) y el 24-ago tenía los pies muy hinchados;
el pronóstico daba **27-32°C con humedad alta**. Por eso todo lo elegido es **sentado,
corto o con aire acondicionado**, y el metro es la columna del recorrido.

**El dato más práctico de todos, y el que nadie avisa:** en Hong Kong el enchufe es el
**británico de 3 patas planas**, distinto al de China continental — **su cargador chino
no entra**. Se le dijo que pidiera adaptador en el hotel al llegar.

**Lo recomendado:** Octopus (八達通) · Star Ferry HK$6 · Peak Tram *con la advertencia de
la fila al sol* · Tai Kwun · Symphony of Lights 20:00 · para el domingo lluvioso **M+**,
K11 MUSEA y Harbour City · farmacias **Mannings/Watsons** (de cadena, no las 藥房 de calle)
· dim sum sí, sashimi y mariscos crudos no.

**Lo desaconsejado explícitamente:** Buda Grande de Lantau (medio día + 268 escalones),
Dragon's Back y cerros; y no intentar isla + Kowloon + Lantau en 2 días.

**Cómo se verificó el clima, que sirve para cualquier consulta futura de Hong Kong:** la
API abierta del **Observatorio de Hong Kong**, sin clave —
`data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en` para el
pronóstico de 9 días y `dataType=warnsum` para los avisos vigentes (devuelve `{}` cuando
no hay ninguno, que fue el caso: **sin señal de tifón**). La página `hko.gov.hk/textonly`
NO sirve: llega llena de CSS y no se puede leer.

Quedó ofrecido reordenarle el plan por cercanía si dice dónde se aloja.

### Repreguntó por los escalones del Buda (msg 760) — y tenía razón en repreguntar

*«¿pero para el Buda hay que subir todos esos escalones?»*. **Mi advertencia estaba mal
enfocada y se lo dije:** los **268 escalones** suben al **pódium**, pero el Buda mide
**34 m** y se ve completo desde la explanada y el monasterio — **para verlo no hay que
subir ninguno**. Además vienen **por tramos con descansos**, y a las 22 semanas subir
escaleras no está prohibido: lo pesado es hacerlo al sol con 32° y humedad.

**Dato verificado:** existe un camino de vehículos hasta un estacionamiento bajo el
pódium, con rampa, **pero solo para vehículos autorizados — los taxis no entran**. No es
una opción contratable, así que no sirve como plan B.

**Lo que sí sostenía mi reparo, y es lo que le dije:** el problema no eran los escalones
sino **el día completo** — metro a Tung Chung + teleférico de 25 min por lado + fila +
vuelta. Con 2 días, el Buda **es uno de los dos días**.

**Cómo se cerró, sin quitarle la decisión:** si le tinca igual, que vaya el **domingo**
(que llueve y el plan de ciudad se cae), **reservando el teleférico online** por la fila
de fin de semana, temprano, y que suba los escalones solo si el cuerpo se lo pide.

**Lección para mí:** al desaconsejar algo, **decir cuál es el costo real**. Yo colgué la
advertencia de los escalones, que era lo llamativo pero lo menos cierto, y el argumento
de verdad —medio día de los dos que tiene— quedó en segundo plano. Ella repreguntó
justamente por el pedazo débil.

## Dónde se aloja: Royal Plaza Hotel, Mong Kok (msg 768, 5-sep-2026)

**Royal Plaza Hotel, 193 Prince Edward Road West, Mong Kok.** Preguntó si estaban
«arriba o al lado de un mall».

**Arriba, y de dos cosas a la vez:** el hotel está **encima de MOKO** (+200 tiendas) y
**encima de la estación Mong Kok East**, con acceso techado a ambos. Es de Sun Hung Kai,
abrió en 1997.

**El hallazgo que valía el mensaje:** la tienda **Casetify** que le pasé el 4-sep como
«MOKO, Shop M22, piso MTR» **está en el mall de su propio hotel** — la dirección de esa
tienda es literalmente **193 Prince Edward Rd W**, la misma del hotel. Le dije que se
olvidara de Festival Walk. *Salió porque relacioné la dirección que ella mandó con la
lista que yo mismo había armado el día anterior; si no releo mi propia respuesta, se
pasa.*

**Lo demás que se sigue de la ubicación:**
- Su estación es de la **East Rail**, la misma línea del borde con Shenzhen, y
  **Kowloon Tong está a una parada**.
- **Mercado de las Flores** y **Jardín de los Pájaros** a ~8 min a pie, por Prince Edward
  Road West, **sin escaleras**. **Ladies Market** a ~10 min. Tsim Sha Tsui a ~15 min en
  metro.
- **Piscina temperada de 40 m al aire libre en el piso 8** — se lo destaqué por encima
  del resto: con los pies hinchados ([[embarazo-connie]]) flotar al final del día es lo
  que mejor le va a hacer. **Buscar siempre el dato del hotel que sirva a su estado, no
  el que luce.**

Quedó ofrecido reordenarle los dos días saliendo desde el hotel.

### Ferias baratas en Mong Kok (msg 770)

Todo a pie desde el hotel: **Ladies Market** (Tung Choi St, 10 min, hasta 23:30) ·
**Fa Yuen Street**, la de al lado y **más barata porque es la de los locales** ·
**Sneaker Street** · **Temple Street**, nocturno, parte 18:00, dos paradas de metro.
Regateo: **ofrecer el 40%**, efectivo, y caminar si dicen que no.

**Lo que hacía falta decir, y es lo que da valor a la respuesta:** viene llegando de
**Huaqiangbei**, así que estas ferias le venden **la misma mercadería china que acaba de
ver, pero más cara** — allá estaba en la fábrica, aquí en la reventa. **En Hong Kong lo
barato es lo opuesto al mercado callejero:** sin IVA, lo que conviene son las **marcas
reales** (cosméticos en Sasa/Bonjour, farmacia en Mannings, electrónica original).

Es la misma regla del caso Shokz de [[comprar-electronica-huaqiangbei]] leída al revés, y
conviene tenerla a mano: **el lugar barato para un genérico no es el lugar barato para una
marca**.

Se le sugirió ir cerca de las **18:00**: baja el calor y ya están todos los puestos.

### Quería ropa de réplica (msg 772)

**Hong Kong no es el lugar y se lo dije derecho:** en el Ladies Market hay algo, de mala
calidad y caro, porque HK persigue la falsificación.

**El lugar está en su camino de vuelta: 罗湖商业城 (Luohu Commercial City)** — 5 pisos de
réplicas (ropa, carteras, relojes, zapatillas) **pegado al control de inmigración de
Lo Wu**, del lado de Shenzhen. Lleva 30 años y es donde compra la propia gente de Hong
Kong. Tiene **sastres que copian una prenda a medida**, y **hablan inglés**, así que ahí
no necesita tarjetas en chino.

**El detalle que hace que el dato sirva:** tiene que **volver cruzando por Lo Wu (罗湖)**,
no por Futián ni Lok Ma Chau — el mall está pegado a ese paso y no a los otros. Un dato
de compras sin la condición de ruta no habría servido de nada.

**Regateo ahí: partir en el 20%**, bastante más agresivo que en HK.

**Sobre Aduana:** solo **una línea** al final, sin repetir el argumento completo que ya se
le dio el 3-sep por los relojes. Misma política de no acumular precauciones de
[[lewear-ht30-relojes]].

### Dónde queda exactamente Luohu Commercial City (msg 774)

**Dirección:** `深圳市罗湖区和平路 罗湖商业城` — Heping Road, Luohu, **pegado al 罗湖口岸
(paso de Lo Wu) y a la Estación de Tren de Shenzhen**. Se sale de inmigración y está al
frente. Abre **10:00-22:00**; el paso fronterizo, hasta medianoche.

**Lo que convirtió esto en una respuesta buena:** la estación que tiene **debajo del
hotel**, Mong Kok East, es de la **East Rail Line**, y esa línea **termina en Lo Wu** —
**~40 minutos directos, sin transbordos**, desde su propia puerta.

**La advertencia que evita el error:** en **Sheung Shui la línea se divide**. Hay que
tomar el tren que dice **Lo Wu (羅湖)**, no el de **Lok Ma Chau**, que deja en el otro paso
y lejos del mall.

Y como es su ruta de vuelta a Shenzhen igual, **no le cuesta ningún día de Hong Kong**.

### ¿Hong Kong o Shanghái para réplicas? (msg 776)

**Respuesta: Shanghái le gana a Hong Kong, pero ninguna le gana a Luohu.** El ranking que
le di, con el motivo y no solo el orden:

1. **Shenzhen (Luohu)** — **Guangdong es donde se fabrica**: compra en el origen.
2. **Shanghái, AP Plaza** — bajo el metro de *Science & Technology Museum*,
   `世纪大道2002号`, 10:00-20:00. Sigue siendo el más grande, **pero está de capa caída**:
   lo bueno ya no está, quedó calidad más baja y los vendedores andan cautos por las
   fiscalizaciones (verificado, dato de 2026 — no repetir la fama vieja del lugar).
3. **Hong Kong** — poco y caro.

**El dato que sirve en las tres y que ella no iba a saber:** *lo que está a la vista es lo
malo*. La calidad buena está en otro piso o en una pieza atrás y **hay que pedirla**; no
la ofrecen.

**Regateo:** Shanghái abrir en **10%** y cerrar entre **25-40%**; Luohu, **20%**.

**Quedó preguntado si va a pasar por Shanghái** — si va, le preparo dirección y frases.
No lo sé y no lo supuse.

### Volvió a pedir el plan, ya con hotel conocido (msg 778, 16:06 de HK del sábado)

Descartó Shanghái y pidió *«dime mejor qué hacer aquí»*. **No se le repitió el plan del
msg 759:** ya eran las 16:06 del sábado y el plan genérico de dos días había dejado de
servir. Se rehízo **con horas** y anclado en el hotel:

- **Hoy sábado:** 18:00 metro a Tsim Sha Tsui · 19:00 **Star Ferry** al atardecer (HK$6) ·
  20:00 **Symphony of Lights** · cena.
- **Domingo:** temprano **Mercado de las Flores** y **Jardín de los Pájaros** a 8 min a pie
  · si arrecia la lluvia, **M+** · tarde **Ladies Market** y **MOKO** bajo el hotel.
- **Cerrar cada día en la piscina del piso 8**, por las piernas.

**El criterio que ordenó el plan fue el pronóstico, no el gusto:** hoy despejado y mañana
con chubascos, así que **lo de afuera va hoy** y lo bajo techo queda para el domingo.
Decírselo con esa razón explícita vale más que la lista.

**Regla:** un plan de viaje se arma sobre **la hora que es allá y lo que queda del día**,
no sobre los días nominales. A las 16:06 el «día 1» ya no existe.

Quedó ofrecido comprimirlo todo a esta noche si se va el domingo temprano.

### Se va el martes, no el domingo (msg 780) — y eso reabrió el Buda

Dijo «me voy 2 días» pero en realidad tiene **hoy sábado, domingo, lunes y la mañana del
martes**. **Preguntar la fecha de salida antes de planificar, no después:** dos mensajes
de plan se armaron sobre un supuesto equivocado.

**Consecuencia principal, y se le dijo como corrección explícita:** mi reparo al **Buda
Grande** era que se comía uno de sus dos días. **Con el lunes libre ese reparo se cae**, y
el Buda entra. Calza doble porque **el M+ cierra los lunes** (verificado: abre martes a
domingo, 10:00-18:00), así que el lunes no servía para museo de todos modos.

**El plan final:**
- **Sábado:** Star Ferry al atardecer + Symphony of Lights. *Su noche más despejada.*
- **Domingo (lluvia):** Mercado de las Flores temprano · **M+** a mediodía · Ladies Market.
- **Lunes:** **Ngong Ping y el Buda**, día completo, teleférico reservado la noche antes.
- **Martes:** el **Peak**, porque es el **único día despejado que le queda** y esa vista sin
  cielo limpio no vale nada.

**El criterio que ordenó los cuatro días fue el pronóstico cruzado con los días de cierre
de cada lugar**, no el interés de los panoramas. Quedó preguntada **la hora de salida del
martes** para saber si el Peak alcanza.

### Confundió el Star Ferry con un crucero turístico (msg 784, foto)

Mandó la ficha de un **crucero Wing On** por la bahía, **US$15 (~14 lucas)**, preguntando
si era ese. **No lo era:** el Star Ferry es el ferry verde y blanco de línea, **HK$6,5**
(~$800), que cruza ahí hace más de 100 años.

**Pero no se descartó el crucero, y esa fue la parte útil de la respuesta.** Si su salida
es la de las **20:00**, ve el **Symphony of Lights desde el medio de la bahía y sentada**,
en vez de parada y apretada en el malecón. Con sus piernas hinchadas
([[embarazo-connie]]) eso **justifica las 14 lucas**. Se le dijo que hiciera **las dos
cosas**.

**Las tres verificaciones que se le pidieron antes de reservar:** que la salida sea la de
las 20:00 y no un paseo diurno · de qué muelle sale · y que lo reserve para **hoy**, que
está despejado, porque la ficha dice **«no se admiten cancelaciones»** y mañana llueve.

**Y una resta honesta:** el «consumo ilimitado de bebidas» que la oferta destaca **vale
poco para ella**, porque la gracia de eso suele ser el alcohol. Al valorar una oferta,
descontar los beneficios que en su caso no aplican.

### Alipay le falla en Hong Kong (msg 786)

**No era su cuenta: Hong Kong es otro circuito de pagos.** El Alipay del continente solo
funciona en los comercios adheridos al esquema transfronterizo —cadenas grandes y poco
más—, y **AlipayHK es una app aparte** que exige teléfono e identidad de Hong Kong. Además
**Hong Kong no vive del pago con teléfono** como el continente.

**Lo que sí sirve, y es lo que le mandé:**
- **Octopus (八達通)** — metro, buses, Star Ferry, 7-Eleven, supermercados y muchos
  restoranes. Se compra en el **mostrador de atención del metro**, que tiene **abajo de su
  hotel** en Mong Kok East. **HK$150 = $50 de depósito reembolsable + $100 de saldo**; se
  recarga en efectivo.
- **Efectivo en HKD** para el Ladies Market, los puestos y muchos taxis, que son **solo
  efectivo**. Visa/Mastercard para malls y restoranes.

**Se le dijo que la sacara HOY antes de salir**, porque la necesitaba esa misma noche para
el metro y el Star Ferry. **Una respuesta de pagos sin el «cuándo» habría llegado tarde.**

**Regla general:** cuando algo que le funcionaba en el continente falla en Hong Kong, la
causa por defecto es **que son dos sistemas distintos** (pagos, enchufes, moneda, SIM), no
que su cuenta o su aparato estén malos. Ver el enchufe británico más arriba.

### Cajero Hang Seng (msg 788, foto)

Mandó la foto de un cajero de **恒生銀行 Hang Seng** en un mall preguntando si servía para
sacar plata. **Sí:** Hang Seng es de los bancos grandes de Hong Kong, del grupo **HSBC**, y
acepta tarjetas extranjeras. Ese entrega **HKD y RMB** — se le dijo que eligiera **HKD**.

**Lo que se puso como titular, porque es donde de verdad pierde plata:** cuando el cajero
ofrece **cobrar en pesos chilenos** o «conversión con tasa garantizada» (**DCC**), hay que
decir **NO** y elegir **cobrar en HKD / sin conversión**. Aceptarla cuesta **3-8% extra**;
que el banco de ella haga el cambio siempre sale más barato. **Esto vale para cualquier
cajero en cualquier país** — no es un dato de Hong Kong.

**Las otras dos:**
- **Sacar harto de una vez:** su banco chileno cobra **cargo fijo por giro** (~US$5-7), así
  que tres giros chicos cuestan el triple que uno grande. Los cajeros de Hong Kong no
  suelen agregar comisión propia.
- **Pedir un monto quebrado** (HK$1.500 en vez de HK$1.000) para no recibir todo en
  billetes de $500 y $1.000, que en el Ladies Market son un problema.

### La reserva del crucero, y una corrección mía (msgs 792-794)

Ya lo tenía **reservado**: crucero **Wing On**, **sábado 5-sep**, **3 adultos, US$45**,
**salida 20:10**, **Muelle Público N°3/4 de Tsim Sha Tsui**, no reembolsable. *Pidió la
captura antes de inventar el muelle — de la primera foto no se veía, y había tres
posibles.*

**La corrección que valía el mensaje:** yo le había dicho que si zarpaba a las 20:00 vería
el show **desde el agua**. **El show es 20:00-20:10** (verificado) y el barco sale
**20:10**: no lo ve desde el agua. Se lo dije derecho, y con la parte buena — estará
parada en el **mejor punto de tierra** justo mientras espera embarcar, y después navega
con la bahía iluminada. **Corregir el supuesto propio antes de que lo descubra ella.**

**El itinerario con horas que le mandé:** 18:30 salir · Mong Kok East → Hung Hom → East
Tsim Sha Tsui · salir por letreros «Star Ferry», referencia la **Torre del Reloj** · 19:00
Star Ferry ida y vuelta (HK$6,5) · 19:45 en el muelle · 20:00 el show · 20:10 a bordo.

**Metro sin Octopus:** se le confirmó que el MTR acepta **tarjeta contactless directo en
el torniquete** (misma tarjeta al entrar y salir) y **boleto con efectivo** en máquina.

**Dato con fecha de vencimiento:** hay reportes de que el *Symphony of Lights* **se
reemplaza durante 2026** por otros shows. Si alguien pregunta más adelante, **verificar
antes de darlo por vigente**.

### El enchufe «shavers only» del baño (msg 798, foto)

**Mandó la foto de un enchufe del baño del hotel que dice «shavers only / 115V», con su
cargador puesto, preguntando si había una razón.** La hay, y es de seguridad: es un
**enchufe de afeitadora con transformador aislado** — lo que sale no está referido a
tierra, así que si el aparato cae al agua o se toca con las manos mojadas **el circuito no
se cierra por el cuerpo**. Es el **único** enchufe que la norma británica (heredada en
Hong Kong) permite dentro de un baño; por eso ahí no hay otro. Mismo origen que el enchufe
británico de 3 patas de más arriba.

**Lo que se puso como advertencia, porque es donde la gente rompe algo:** el límite real
son ~**20 W**. Afeitadora, cepillo eléctrico y cargador de teléfono, sí. **Secador de
pelo (1.500 W), alisador o hervidor, no** — no es que anden mal, es que **le queman el
fusible interno al enchufe y queda muerto**, y hay hoteles que lo cobran.

**Su cargador estaba bien:** el «115V» del cartel es porque el enchufe entrega dos
voltajes, y los cargadores modernos son `Input 100-240V`. La salvedad útil: **si es
cargador rápido, ahí no da toda su potencia** — para cargar de noche, el enchufe normal
de la pieza.

**Regla:** cuando fotografía algo del hotel y pregunta «¿por qué dice esto?», la respuesta
completa incluye **qué NO hay que enchufar/hacer ahí**, no solo la explicación del cartel.

### La noche del crucero, en vivo por el chat (msgs 800-811, 5-sep)

**Fue una conversación de navegación en terreno, no de planificación**, y eso cambia el
tipo de respuesta: mensajes cortos, la respuesta primero, y siempre una **referencia que
ella pueda verificar sin mí**.

Lo que preguntó, en orden, y lo que resultó útil:

- **«¿Es aquí donde sale el crucero?»** con el mapa del **Star Ferry Terminal**. No era:
  el crucero sale del **Muelle Público 3/4**, pegado al del Star Ferry. **Lo que sirvió
  fue el truco de los números:** los muelles están numerados seguidos en el mismo paseo
  —**1 y 2 = Star Ferry, 3 y 4 = público**—, así que «sigue los números» funciona sin
  depender de mi sentido de orientación. Se le dio además la referencia de sobrepaso: si
  llega al Centro Cultural, se pasó.
- **«Estoy dentro de Mong Kok East, dónde está Hung Hom»** → 1 parada al sur. **El dato
  que evitaba el error caro: tomar el andén de Admiralty (金鐘), NO el de Lo Wu / Lok Ma
  Chau, que la devuelve hacia Shenzhen.** Después trasbordo a Tuen Ma Line dirección Tuen
  Mun hasta East Tsim Sha Tsui.
- **«En la L, ¿cuál? Hay de la 2 a la 6»** → **L6** (Star Ferry / Torre del Reloj), con
  L5 como respaldo. **Y lo que de verdad la dejó tranquila: de la L4 a la L6 salen todas
  al mismo sector, no hay forma de quedar lejos.** Cuando está apurada, decirle que el
  error no le va a costar caro vale tanto como la respuesta exacta.
- **«¿A qué hora cierra el metro?»** → ~**01:00**, últimos trenes 00:00-00:30, y el
  letrero **«Last train»** del andén como fuente que no soy yo. Taxi como plan B.
- **«Quiero volver al hotel ahora»** (21:02) → **se le recomendó taxi, no metro**: 22
  semanas, todo el día de pie, HK$50-70. Se le pasó el nombre del hotel en chino para
  mostrarle al chofer: `帝京酒店，太子道西193號` (*Royal Plaza Hotel, «dai ging jau dim»*).
  El metro quedó como alternativa, con el detalle que más pesa de noche: llega **dentro
  de la estación** y sube al hotel sin salir a la calle.

**La corrección de ella, y la lección:** después de darle salida y ruta le dije «desde
ahí el Star Ferry te queda al frente» y respondió **«no quiero Star Ferry, quiero el
crucero»**. El Star Ferry era MI plan, de la noche anterior; ella ya lo había soltado.
**Cuando está ejecutando, contestar exactamente lo que preguntó y no arrastrar el plan
que yo armé antes.** Se corrigió sin insistir ni justificar.

**Regla operativa que quedó:** en consultas de ruta en vivo, dar (1) la respuesta en la
primera línea, (2) una seña física verificable —número de muelle, letrero, nombre en
chino—, y (3) el margen de tiempo, para que sepa si puede caminar tranquila o apurarse.

### Compras del domingo: me equivoqué de tipo de panorama (msgs 823-825, 6-sep)

Pidió *«comprar cosas más baratas y que sean de Hong Kong, no reventa de tecnología»*.
**Le armé un plan de Mercado de las Flores, Jardín de los Pájaros, Calle de los Peces y
Sham Shui Po (telas, cintas y botones)** — todo barato y todo genuinamente local. Y me
respondió lo que correspondía: **«no voy a ir a comprar plantas po Kai, tampoco cintas ni
botones ni telas»**.

**El error:** traduje «barato + de Hong Kong» a **color local**, y le entregué un paseo
antropológico en vez de un lugar donde comprar. Ella quería **accesorios y productos**
—cosas que se meten en la maleta y se usan— no la experiencia del barrio.

**Regla: cuando dice «comprar», el filtro es qué se lleva puesto o de regalo, no qué tan
auténtico es el barrio.** Un mercado de flores es local y barato y no sirve para nada de
lo que ella pidió.

**Lo que sí correspondía, y quedó verificado el 6-sep:**

- **Mercado de Jade** <code>玉器市場</code>, Kansu St, Yau Ma Tei — ~**400 puestos** de jade,
  perlas, pulseras y aros. **Techado** (sirve con lluvia), a 1 parada de su hotel. **Muchos
  puestos cierran 15:30-16:00**, así que es panorama de mañana. Advertencia dada: mucho
  jade teñido o falso — **comprar como bisutería y pagar precio de bisutería**, ofreciendo
  un tercio.
- **Las Lanes de Central** <code>利源東街 / 利源西街</code> — dos callejones con toldos:
  carteras, mochilas, cinturones, accesorios de pelo, pañuelos, bisutería, fundas.
- **G.O.D.** <code>住好啲</code>, 6 D'Aguilar St, Central, 10:00-20:00 — **la marca de
  diseño de Hong Kong**. Tienda, no feria, y más cara que un puesto, pero es lo más
  «producto de Hong Kong» que existe.
- **Jardine's Crescent** <code>渣甸坊</code>, Causeway Bay — el Ladies Market de los
  locales: más barato y sin recargo turístico.

**Lo que sí acerté y conviene repetir:** decirle que **el Ladies Market es reventa del
continente**, la misma mercadería de Shenzhen más cara. Y el hallazgo de reusar lo ya
sabido: **Casetify es marca de Hong Kong y su tienda está en MOKO, el mall de su propio
hotel** — accesorio de acá, a cero desplazamiento.

**El clima ordenó el día otra vez:** 26-31°, claros en la mañana y **tormentas eléctricas
en la tarde**, sin avisos vigentes (API del Observatorio, `dataType=fnd` y `warnsum`).
Por eso lo techado va después de mediodía.

### El itinerario que ELLA eligió para el domingo 6-sep (msg 831)

Después de descartar mis dos propuestas, lo armó ella y pidió anotarlo:
**Ladies Market · G.O.D. · Temple Street de noche.**

**Eligió el Ladies Market aunque yo le había dicho que es reventa del continente.** Es su
decisión y no se volvió a discutir: se le dieron las direcciones completas y, en vez del
reparo repetido, lo útil para ese lugar —**efectivo, partir ofreciendo la mitad, y que si
no le bajan el precio camine, porque el mismo puesto está tres veces en la calle**.

**Lo único que sí se corrigió fue el orden, y por un dato duro:** el **Ladies Market abre
al mediodía**, así que hacerlo primero no era posible. Quedó: **G.O.D. en la mañana**
(cruzar la bahía temprano, antes de las tormentas de la tarde, y Central es todo techado)
· **Ladies Market en la tarde** · **Temple Street desde las 18:30**.

**Las direcciones, para no rehacerlas:**
- **G.O.D.** — 6 D'Aguilar St, Central, 10:00-20:00. Mong Kok East → East Rail dirección
  **Admiralty** (3 paradas) → línea **roja** dirección **Central** (1 parada) → salida
  **D2** → Queen's Road Central → D'Aguilar sube a la derecha. ~30 min, **HK$14**.
  Las **Lanes** están a 2 min de esa salida y son planas: van antes de subir el cerro.
- **Ladies Market** — Tung Choi St <code>通菜街</code>, Mong Kok. **A pie desde el hotel,
  10-12 min**, plano: Prince Edward Rd West hacia el oeste hasta Tung Choi, doblar a la
  izquierda; el mercado parte en Argyle St. **Seña de que va bien: si ve peceras, está en
  la parte norte de la misma calle y tiene que seguir bajando.**
- **Temple Street** — Jordan salida **A** (el arco) o Yau Ma Tei salida **C**. 2 paradas
  desde Mong Kok, o 15 min a pie desde el final del Ladies Market, o taxi HK$40-50.
  **Se prende 18:00-19:00.**

**Nota mía:** en dos mensajes seguidos ella rehízo el plan que yo había armado. **No es
que los datos estuvieran malos: es que yo elegía por criterio de autenticidad y ella
elige por lo que quiere hacer.** Dar los datos y dejar que arme, en vez de armar y
defender.

**Agregó Pottinger Street** <code>砵典乍街</code> al itinerario (msg 837). Encaja sin
costo porque **las tres cosas de Central están sobre Queen's Road Central**, de oeste a
este: **Lanes → Pottinger → D'Aguilar (G.O.D.)**, 3 minutos entre cada una y sin
devolverse. Los puestos de linternas están en la **parte baja** de Pottinger, así que no
hay que subir los escalones; se le advirtió que **las losas de piedra resbalan con
lluvia**.

**El itinerario final quedó con horas** —formato que ella sigue bien, igual que la noche
del crucero—: 10:45 salir · 11:15 Lanes · 11:45 Pottinger · 12:15 G.O.D. · 13:00 almuerzo
· 15:00 Ladies Market · **17:30 al hotel a descansar** · 18:45 Temple Street.
**El descanso va escrito a propósito**: 22 semanas y piernas hinchadas
([[embarazo-connie]]), y el hotel le queda al lado del Ladies Market.

**Criterio de fondo: cruzar la bahía una sola vez y en la mañana**, antes de las tormentas
de la tarde; todo el resto del día cae en su propio barrio.

**Sobre la Lantern Street de Yuen Long** (msg 835): es un callejón del mercado **Tai Kiu**
donde la tienda **冠香行** cuelga +1.000 linternas a mano, **08:00-20:00**, mejor después
de las 19:00, desde ~HK$30. **Se descartó por distancia**: ~50 min por lado, 2 horas de
viaje que le botaban medio itinerario. Y el dato que evitaba una decepción: **las
linternas famosas son todas después de que se va** — Victoria Park 19-27 sep, Centro
Cultural de TST desde el 17, Dragón de Fuego de Tai Hang 24-26; **Medio Otoño 2026 es el
25 de septiembre**.

**«Lung Fung Mall» no es un mall** (msgs 839-841). Es <code>龍豐</code>, una **cadena de
farmacia y belleza** de ~28 locales — cosméticos, skincare, remedios y suplementos. Si
alguna vez lo vuelve a nombrar, ese es el dato que corrige la expectativa.

**La sucursal útil cayó sola en el plan:** **Gala Place, 56 Dundas Street**, Mong Kok
(salida E2 de la estación Mong Kok) — y **Dundas Street es donde termina el Ladies
Market**, así que sale del mercado y está ahí. Se le advirtió que **no compre remedios,
hierbas ni suplementos chinos** sin preguntarle al doctor, por el embarazo; cosméticos sin
problema.

**ITINERARIO FINAL DEL DOMINGO 6-SEP, como quedó:** 10:45 salir · 11:15 Lanes · 11:45
Pottinger · 12:15 G.O.D. · 13:00 almuerzo en Central · 15:00 Ladies Market · 16:30 Lung
Fung · 17:15 hotel a descansar · 18:45 Temple Street.

**Lo que hizo que funcionara: encadenar por geografía, no por interés.** Central es una
sola calle de oeste a este (Lanes → Pottinger → D'Aguilar); Ladies Market y Lung Fung son
la misma calle de norte a sur (Tung Choi → Dundas); Temple Street queda a 2 paradas. **Una
sola cruzada de bahía, en la mañana.**

**Corrección de terreno (msg 852): Pottinger Street está al OESTE de las Lanes, no al
este.** Yo le había dado el orden «Lanes → Pottinger → D'Aguilar, 3 min al este cada
una». El orden real sobre Queen's Road Central, de **oeste a este**, es: **Mercado Central
<code>中环街市</code> · Pottinger <code>砵典乍街</code> · Li Yuen West · Li Yuen East (las
Lanes) · Pedder · Ice House · D'Aguilar (G.O.D.)**. Se lo dije apenas lo vi en la foto de
su mapa, antes de que caminara de más: le costaba ~5 minutos extra, no más.

**Cómo se detectó:** mandó una captura de Amap con su punto azul y ahí aparecían **中环街市
arriba a la izquierda** y **中环利源东街25号铺** al lado suyo — o sea el Mercado Central,
que está junto a Pottinger, quedaba al **oeste** de ella. **Su propia captura sirvió para
corregirme; conviene mirarlas como fuente y no solo para ubicarla a ella.**

**Buscar en Amap va en chino:** «The Lanes» es apodo de turista y no existe en el mapa; lo
que funciona es pegar <code>利源東街</code>.

**Lung Fung también está en MOKO, el mall de su hotel** (msg 864): **Local 162, Nivel 1,
193 Prince Edward Road West** — la misma dirección del Royal Plaza. La grande del grupo es
la de **Gala Place, 56 Dundas St**, que es su tienda insignia y queda al final del Ladies
Market: esa se elige solo si quiere variedad, porque los precios son de la misma cadena.

**Van tres cosas que terminaron estando en MOKO: Casetify, Lung Fung y su propio hotel.**
Regla que ya se repitió: **antes de mandarla a cruzar la ciudad, revisar si eso existe en
Mong Kok o en su propio mall.**

**Mannings vs Lung Fung** (msg 862), que preguntó estando en la calle: se le partió por
categoría en vez de dar un ganador. **Cosméticos, skincare y maquillaje → Lung Fung**, que
compite por precio. **Cualquier cosa que se tome → Mannings** <code>萬寧</code>, que tiene
farmacéutico y producto claro — y con el recordatorio de que los remedios y suplementos
los vea **con su doctor a la vuelta**, no allá. Método que se le dio para decidir sola:
elegir 2-3 productos concretos y comparar el precio de góndola, porque **la diferencia
cambia según el producto, no según la tienda**.

### Del hotel a Temple Street (msg 868, domingo 6-sep, 17:37 de HK)

Preguntó **«cómo voy y a qué hora me conviene»** estando ya en el hotel, justo en el
descanso de las 17:15 del itinerario. Respuesta que se le dio:

- **Taxi**, ~10 min, **HK$40-50**, mostrando <code>廟街，佐敦道</code> (*Temple Street con
  Jordan Road, «miu gaai, jo dun dou»*).
- **El argumento que decidió el medio:** su estación de abajo (**Mong Kok East**) es East
  Rail, y Temple Street está en la **línea roja** — o sea que en metro igual tiene que
  caminar 8-10 min hasta **Mong Kok** (Nathan Rd) antes de subirse. El taxi no le ahorra
  plata, le ahorra **esa caminata**, que a las 22 semanas y después de todo el día es el
  costo real ([[embarazo-connie]]).
- Metro como alternativa: Mong Kok → roja dirección Central → **2 paradas** → **Jordan
  salida A**, que sale al arco. HK$5.
- **Hora:** se prende **18:00-19:00**, encendida del todo a las **19:00**; salir **18:30**
  para llegar 18:45 y verla prenderse. Puestos hasta las **23:00**.
- **Recorrido:** partir en el **arco de Jordan** y caminar hacia el **norte**, así queda de
  corrido y termina cerca de Yau Ma Tei sin devolverse.
- Clima verificado en el momento (API del Observatorio, `warnsum` vacío y `rhrread`):
  **30°, sin lluvia, sin avisos**. La tormenta de la tarde pronosticada **no llegó**.

**Lo que se repitió a propósito:** respuesta en la primera línea, seña física verificable
(el arco), margen de tiempo, y el nombre en chino para el chofer. Y no se le arrastró nada
del plan anterior: preguntó ruta y hora, se le dio ruta y hora.

**Volvió a preguntar la MISMA ruta 1h33 después** (msg 878, 19:10 de HK): *«para ir al
temple street cómo lo hago desde el hotel»*. La respuesta ya se la había dado a las 17:37
(msg 869) — pero entremedio pasaron **cinco mensajes de góndola** (Curél, YesStyle, la
segunda tienda, Acnes) que la enterraron.

**La lección, y no es que la respuesta estuviera mala:** una instrucción operativa dada
**con anticipación se pierde** si el chat sigue moviéndose. Dos correcciones:
(1) **re-enviarla en el momento de actuar** sin hacerla sentir que ya se la dije, y
(2) cuando la vuelve a pedir, mandarla **más corta y en pasos numerados** —está de pie,
en la puerta, no leyendo. La segunda versión fue 1-2-3 con el chino para el chofer y nada
más.

**Nunca decirle «te lo mandé antes».** Vuelve a preguntar porque necesita el dato ahora, y
eso es información sobre mi formato, no sobre su atención.
