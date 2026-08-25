---
name: gmail-sin-scope-filtros
description: Ni Maton ni Composio pueden crear filtros de Gmail — les falta el scope gmail.settings.basic. Sí pueden modificar mensajes, así que la barrida propia hace el mismo trabajo.
metadata:
  type: reference
---

**25-ago-2026.** Connie pidió (msg 387) que los correos de AliExpress no le
llegaran más. El camino obvio era crear un **filtro nativo de Gmail**. No se puede
desde acá, y conviene no volver a descubrirlo:

- `POST google-mail/gmail/v1/users/me/settings/filters` por **Maton** → `403
  ACCESS_TOKEN_SCOPE_INSUFFICIENT`.
- `GMAIL_CREATE_FILTER` por **Composio** → **el mismo 403**, contra la misma ruta.

O sea **no es la credencial ni el proxy**: las dos conexiones se autorizaron sin
`gmail.settings.basic`. Arreglarlo es re-autorizar OAuth pidiendo ese scope, y eso
solo puede hacerlo Connie (o Nicolás en el panel). No vale la pena pedirlo solo por
esto.

**Lo que sí funciona:** modificar mensajes.
`POST .../messages/batchModify` con `addLabelIds:["TRASH"]` responde **204**, hasta
900 ids por llamada. Con eso se arma el mismo efecto por fuera.

**Cómo quedó montado:** `bin/limpieza_remitentes.py` lee los dominios de
`memory/estado/remitentes_bloqueados.json` y manda a papelera lo que llegue de
ellos; corre por cron cada hora al **:20**, en silencio salvo error. Para bloquear
otro remitente **se agrega el dominio a ese JSON y listo** — no hay que tocar el
script ni el cron.

**Papelera, no borrado definitivo**: Gmail la guarda 30 días. Si alguna vez cae
algo por error, se recupera. No usar `batchDelete`, que sí es irreversible.

**El punto ciego a recordar:** el filtro barre *todo* el dominio. Si Connie compra
en AliExpress, la confirmación del pedido también se va a la papelera. Se lo dije
al entregar. Si algún día compra, la salida es acotar la barrida con
`negatedQuery` (pedido/envío/factura), no desarmarla.

Ver [[verificar-sin-rompe-cache]] y [[leer-estado-real-antes-de-proponer]].
