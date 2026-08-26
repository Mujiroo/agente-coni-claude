---
name: audios-solo-whisper-local
description: Este contenedor no tiene clave de OpenAI ni de Gemini; los audios de Telegram se transcriben siempre por whisper local.
metadata:
  type: reference
---

**Verificado el 26-ago-2026.** El `.env` de este agente tiene solo:
`TELEGRAM_BOT_TOKEN`, `TG_*`, `COMPOSIO_API_KEY`, `MATON_API_KEY`, `COMPOSIO_MCP_URL`
y las cuatro `WP_SUDTEC_*`. **No hay `OPENAI_API_KEY` ni `GEMINI_API_KEY`.**

`bin/tg_audio.sh` intenta OpenAI → Gemini → **whisper local** (faster-whisper,
modelo `base`). Como las dos primeras no tienen clave, **acá siempre sale por la
tercera**. O sea: la transcripción funciona, pero es la mediocre, y demora más.

Dos consecuencias prácticas:

1. **No perder tiempo llamando a la API de OpenAI a mano** para transcribir un
   `.oga` que ya está en `incoming/`: devuelve *"You didn't provide an API key"*.
   Usar el helper y listo.
2. Si una nota de voz sale confusa, **puede ser el modelo, no ella**. Antes de
   actuar sobre algo ambiguo (una cifra, un nombre propio, una fecha), preguntarle
   por chat en vez de asumir.

Si alguna vez hace falta transcripción buena, eso se pide por la escalera de
soporte: es una clave que pondría Nicolás en el panel — **jamás por el chat**.

Relacionado: [[canal-y-formato]], [[connie]]
