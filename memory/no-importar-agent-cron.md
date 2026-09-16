---
name: no-importar-agent-cron
description: Importar bin/agent_cron.py levanta un SEGUNDO scheduler que dispara todos los crons por duplicado; para probar field_match hay que copiar la función, no importarla.
metadata:
  type: feedback
---

**16-sep-2026.** Quise verificar que un cron nuevo hiciera match y corrí
`from agent_cron import field_match`. El módulo **arranca su loop al importarse**:
quedó un **segundo scheduler** (pid 1876) corriendo en paralelo al legítimo, y
alcanzó a disparar el cron del vigía de Sudtec (`fired #206`) — me llegó la misma
invocación **dos veces**. Se mató con `kill -9` y quedó solo el original.

**Why:** dos schedulers significan **todos los crons duplicados**: doble reenvío de
cotizaciones a Sudtec, doble recordatorio médico, doble aviso a Connie. Esta vez
no pasó a mayores porque el anti-duplicado del reenvío vive en el script, pero es
suerte, no diseño. Además el comando se colgó 120 s y se fue a background.

**How to apply:**
- **Nunca importar `bin/agent_cron.py`.** Para probar la lógica, **copiar** la
  función en el `python3 -c`:
  ```python
  def field_match(field, value):
      if field == '*': return True
      return any(p.isdigit() and int(p) == value for p in field.split(','))
  ```
- Si algo se comporta raro con los crons, **mirar primero `ps -ef | grep agent_cron`**:
  debe haber **exactamente uno**.
- **Los campos NO aceptan rangos.** `field_match` usa `isdigit()`, así que `8-22`
  da `False` siempre: un cron con rango queda **mudo para siempre** y nadie se
  entera. Van en lista: `8,9,10,...,22`. Mismo tipo de defecto que
  [[vigia-mide-la-metrica-rota]].

Relacionado: [[puente-activo-verificar-el-pid]]
