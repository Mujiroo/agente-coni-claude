---
name: leads-perdidos-por-correo-mal-escrito
description: El formulario de cotización de Sudtec no valida el dominio del correo; ya van dos leads reales imposibles de responder en una semana.
metadata:
  type: project
---

**El formulario de cotización de sudtec.cl (YITH Request a Quote) acepta correos
con dominios que no existen.** No hay validación de dominio, solo de formato.

**Casos, en una sola semana:**

- **20-ago-2026**: un solicitante con dominio inexistente (visto en la pasada de
  reenvío de ese día).
- **21-ago-2026, 02:10 y 02:18 UTC**: **Primera Compañía Cuerpo de Bomberos de
  Curacautín** mandó **dos** cotizaciones (pedidos **11608** y **11609**) con el
  correo `primeracia.cbcuracautin@gmail.con` — **`.con`**, no `.com`. Cualquier
  respuesta por correo se pierde.

**Por qué importa:** son cotizaciones reales de instituciones reales. La de
Curacautín además traía una pregunta comercial que no está en el catálogo
(cadenas de rescate más largas que las que vienen con los equipos hidráulicos),
o sea una venta potencial además del ítem pedido.

**Lo que salva el caso:** el formulario **sí pide teléfono**, y ese campo venía
bien (`933964206`). Está en `_raq_request.telefono`. **Cuando el correo rebote o
tenga dominio dudoso, buscar el teléfono ahí y pasárselo a Connie** — no se
responde por cuenta propia a un tercero.

**Pendiente propuesto a Connie (21-ago, msg 288):** validar el dominio en el
formulario. Es un cambio en el sitio, así que **no se toca sin su OK**.

Relacionado: [[litespeed-cachea-la-api-rest]] — el mismo día, ese caché casi
esconde estas dos cotizaciones.
