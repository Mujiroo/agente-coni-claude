# Cómo se comunica Connie conmigo

*17-ago-2026.*

## Audios

**Connie manda audios.** Los recibo y transcribo con `bash bin/tg_audio.sh <file_id>`.

⚠️ **Hoy la transcripción es con whisper local (modelo `base`)** — no hay
`OPENAI_API_KEY` ni `GEMINI_API_KEY` en el `.env`. Funciona, pero:

- se le escapan **nombres propios y términos técnicos**
- en audios largos o con ruido baja bastante

**Cómo lo manejo:** si transcribo algo que no calza con el contexto, **no adivino
ni respondo sobre esa base** — le devuelvo lo que entendí y le pido que confirme.
Es preferible a actuar sobre una palabra mal oída.

Si algún día aparece una clave de OpenAI o Gemini en el `.env`, el mismo script
la usa solo y la calidad sube sin tocar nada. Eso lo pone Nicolás o ella con
`/env`; **nunca se pide por chat**.

## Formato

Ella lee todo en el teléfono → **siempre HTML**, párrafos cortos, negritas en
cifras y nombres. Ver [[connie]] para el resto del contexto.

## Idiomas: caracteres chinos SIEMPRE con traducción (27-ago-2026)

**Ella me lo pidió textual** (msg 471): *«No entiendo en chino jaja, porfavor
trata de ponerme entre paréntesis la traducción»*.

El 24-ago yo había aprendido a **mandarle los nombres en caracteres chinos**,
porque sin eso no puede mostrárselos al taxista ni pegarlos en el mapa. Eso
sigue siendo cierto. **Lo que faltaba es la otra mitad:** ella no lee chino, así
que un bloque de caracteres solo es opaco y no sabe qué está mandando ni si es
lo que quiere.

**La regla que queda, y vale para cualquier idioma que ella no lea:**

> Cada término en otro alfabeto va con **cómo se lee** y **qué significa**, entre
> paréntesis, en la misma línea.

Ejemplo de la forma correcta:

```
<b>七十二奇楼</b> (<i>Qishi-er Qilou</i> — «las 72 torres prodigiosas»)
<code>七十二奇楼，武陵山大道1号</code>
(<i>«72 Qilou, Avenida Wulingshan número 1»</i>)
```

**El principio detrás,** que es lo que hay que retener: el chino es para
**mostrar**, no para leer. Si le doy algo que no entiende, no puede decidir con
eso — solo obedecerlo a ciegas. Un dato que ella no puede evaluar no la ayuda,
aunque sea correcto.

Relacionado: [[notas-connie]], [[connie]]

### Corolario: además pide frases chinas listas para mostrar (27-ago-2026)

Msg 476: *«Pone en chino: el show de esta hora donde es?»*. No quería una
traducción para entender — quería **una frase que pueda mostrarle a un chino en
la cara**. Es el mismo principio de la sección anterior visto al revés: el chino
es una **herramienta de salida**, no de lectura.

**Cómo se le entrega una frase así:**

1. En `<code>` (se copia y se ve grande en el teléfono)
2. Con la traducción entre paréntesis, para que sepa **qué está mostrando**
3. Sola, sin párrafos alrededor — la va a leer caminando

**Y enseguida lo afinó (msg 478): «pero ponle la hora y el nombre porfa».**
Yo le había dado la frase *genérica* («¿dónde es el show de esta hora?») y ella
quería la **frase ya rellenada** con los datos concretos. La lección: no le
entregues una plantilla para que la complete ella estando en la calle —
**entrégale el resultado terminado**. Le dejé las 7 frases prellenadas de los
shows que le quedaban esa noche, y el molde `请问，__的《__》在哪里？` **al final
y como extra**, no como respuesta.

### Y el error de verdad, el mismo día (msg 480)

Después de las dos correcciones anteriores todavía me faltaba la principal. Ella
escribió, ya con signos de exclamación: **«En chino! Quiero preguntarle a
alguien!»**.

Yo *sí* le había mandado chino — pero envuelto en un mensaje largo, con títulos,
negritas, viñetas, siete frases y un molde al final. **Con una persona parada al
frente, eso no se puede usar.** Tenía que hacer scroll, encontrar el bloque
correcto y recién ahí mostrarlo.

**La regla, y es la que manda sobre las otras dos:**

> Cuando lo que necesita es **mostrarle algo a alguien**, la frase va **sola, en
> su propio mensaje, sin una palabra alrededor**. La explicación va **después, en
> un mensaje aparte**.

Así levanta el teléfono y ya está. Lo que envié al final fueron dos mensajes:

```
请问，现在这个时间的演出在哪里？
```
```
👆 Muéstrale ese mensaje. Dice: «¿dónde es el show de esta hora?»
```

**El patrón de fondo, que es lo que más me cuesta:** cuando ella está en
movimiento, **más información es peor respuesta**. Yo estaba optimizando por
completitud —dejarla cubierta toda la noche— cuando lo que pedía era una sola
cosa utilizable en ese segundo. Las tres correcciones del 27-ago
(traducción → rellenada → sola) son la misma flecha: **acercarle el dato a la
mano**.

**Corolario práctico:** una frase genérica que sirve toda la noche («el show de
esta hora») vale más que siete prellenadas, porque no la obliga a elegir.

**Pendiente ofrecido:** armarle un **mini-glosario de frases de viaje** en chino
(pedir la cuenta, precio, baño, taxi, alergias, "¿me lo puede escribir?"). No se
lo mandé el 27-ago porque estaba en medio de los shows; ofrecérselo cuando esté
tranquila. Vuelve el **18-sep-2026**, así que hay tres semanas donde le sirve.
