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
