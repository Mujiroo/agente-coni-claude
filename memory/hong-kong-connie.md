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
