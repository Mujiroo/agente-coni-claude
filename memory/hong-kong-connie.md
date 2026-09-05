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
