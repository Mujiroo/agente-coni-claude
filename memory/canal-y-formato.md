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
