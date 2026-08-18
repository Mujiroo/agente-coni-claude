---
name: instagram-sin-reacciones
description: Por API no se puede reaccionar (corazón) a un mensaje de Instagram; solo texto, imagen y marcar visto.
metadata:
  type: reference
---

**No se puede poner un corazón ni ninguna reacción a un DM de Instagram desde la
API.** Las reacciones sobre la burbuja del mensaje son de **solo lectura** (llegan
por webhook); ponerlas es exclusivo de la app.

Lo único que la integración permite **escribir** en DMs:

- `INSTAGRAM_SEND_TEXT_MESSAGE` — enviar texto (admite `reply_to_message_id`
  para que quede citando un mensaje)
- `INSTAGRAM_SEND_IMAGE` — enviar imagen
- `INSTAGRAM_MARK_SEEN` — marcar como visto

Verificado el 18-ago-2026 con `COMPOSIO_SEARCH_TOOLS` buscando explícitamente
«react with a heart or like emoji»: devolvió esas tres y ninguna de reacción.

**Cuando Connie lo pida, la respuesta es:** no se puede reaccionar, pero sí
responder con ❤️ como mensaje, marcar visto, o **armarle la lista para que ella lo
haga desde el teléfono**. El 18-ago prefirió **no hacer nada**.

## Tropiezos al leer DMs

- Las conversaciones vienen **doblemente anidadas** en `data.data`. Mirar solo
  `data` parece una bandeja vacía.
- Algunos `conversation_id` **fallan con HTTP 400 (code 100, subcode 33)** aunque
  vengan del propio listado. Hay que saltarlos, no reintentar.
- Los mensajes que comparten un reel llegan con `message: ""` — **el texto vacío
  no significa mensaje vacío**, significa adjunto.

Relacionado: [[contadores-no-son-envios]]
