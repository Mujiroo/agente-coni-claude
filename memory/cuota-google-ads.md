---
name: cuota-google-ads
description: La API de Google Ads tiene tope diario de operaciones y el token es de Maton, no de Connie; el 19-ago lo agoté yo por consultar de más.
metadata:
  type: feedback
---

**El 19-ago-2026 dejé la cuenta de Sudtec sin cuota de API a media tarde**, y con
eso quedaron sin aplicar dos cambios que Connie ya había autorizado. Tuvieron que
irse a un cron de madrugada.

**Cómo funciona.** Google limita las **operaciones diarias** por *developer
token*. **Cada consulta y cada escritura cuentan.** Los niveles: **Explorer**
2.880/día · **Basic** 15.000/día · **Standard** ilimitado. Se sube pidiendo
Standard en el API Center de la cuenta administradora.

**El detalle que importa: el token no es de Connie, es de Maton.** Yo entro por
`api.maton.ai`, así que el tope que topo es de **ellos**, probablemente
compartido. **Ni ella ni yo lo podemos subir**; habría que preguntarle a Nicolás
en qué nivel está, o conseguirle acceso propio a la API.

**Pero la causa de ese día fui yo.** Repetí consultas que ya tenía respondidas:
pedí las keywords, después las keywords con grupo, después las campañas, después
los grupos, y varias de esas llamadas devolvían datos que ya estaban en un
archivo del scratchpad.

**Cómo trabajar la API de Ads de ahora en adelante:**

1. **Una consulta amplia en vez de cinco angostas.** Pedir de una todos los campos
   que se van a necesitar —campaña, grupo, keyword, estado, métricas— y guardar
   el JSON. Después se filtra en local, gratis.
2. **Releer el archivo antes de volver a preguntar.** Si ya está en el scratchpad,
   no se vuelve a pedir.
3. **Escribir al final.** Si el plan incluye cambios, dejarlos para cuando ya no
   queden lecturas pendientes: quedarse sin cuota justo al escribir es lo peor
   que puede pasar.
4. **`validateOnly: true` es gratis en riesgo pero cuesta operación igual.** Usarlo
   cuando el cambio es delicado, no por costumbre.

**Lo que le dije a ella:** que no le pidiera nada a Nicolás todavía, que primero
me ordeno yo. Si vuelve a topar con la cuenta ordenada, ahí sí se pide, con el
dato concreto de cuándo y haciendo qué.

Relacionado: [[vigilancia-ads-429-transitorio]], [[skill-google-ads]]


---

## 20-ago-2026 — Volvió a pasar, y esta vez agoté LAS DOS vías

Se agotó la cuota **dos veces en el mismo día**:

1. **~13:30** — Maton, diagnosticando el anuncio rechazado. Se salió por Composio
   ([[composio-respaldo-google-ads]]), que tiene cuota independiente.
2. **~19:00** — **Maton Y Composio**, revisando por qué el grupo Botas no arranca.
   Sin salida: reintento a las ~06:40 del 21-ago.

**Consecuencia real:** quedó sin hacer el diagnóstico de las keywords del grupo
Botas, justo el día antes de que Connie viajara. Hubo que agendarlo para las 07:00
del día siguiente.

### Lo que aprendí de verdad

**Tener un plan B no es tener cuota infinita.** Saber que Composio existía me hizo
consultar con menos cuidado durante la tarde. El respaldo sirve para no quedar
ciego en una emergencia, **no para gastar al doble**.

**Reglas que se agregan a las de arriba:**

1. **Presupuestar el día, no la consulta.** Antes de una jornada con trabajo de Ads,
   asumir un tope aproximado de llamadas y reservar margen para lo urgente de la
   tarde. Lo que se gasta en diagnosticar en la mañana no está para operar después.
2. **Guardar el JSON de cada consulta amplia en el scratchpad y releerlo.** Varias
   llamadas de hoy pidieron datos que ya estaban en memoria de la conversación.
3. **Cuando el respaldo también sea la única vía, avisar antes de gastarlo.** Si
   Maton ya cayó, cada llamada por Composio es el último cartucho del día.
4. **Dejar la consulta pendiente escrita en el archivo de estado**, con el GAQL
   completo, para que la próxima corrida no tenga que re-derivarla.
   Se hizo en `memory/estado/anuncio_botas.json`, campo `consulta_pendiente`.
