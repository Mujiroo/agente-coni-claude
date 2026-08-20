# Cheil — Traspaso de SEO por las vacaciones de Connie

*Pedido el 20-ago-2026 (msg 234). Le llegó un correo del equipo pidiendo un
traspaso completo antes de irse. Ella lo reenvió y pidió «ordenarlo para que se
entienda bien».*

## Qué se entregó

Documento publicado:
https://claude.ai/code/artifact/188484e3-6d0e-470b-bb01-570c1f13d499

Armado sobre **los nueve puntos que pidió el equipo, en el mismo orden**, para que
la entrega se lea como respuesta punto por punto.

## Lo que se pudo pre-llenar (de las rondas de QA del 18-ago)

- **Chile · NIVEA — BB & CC Cream:** 12 celdas aplicadas y verificadas
- **Guatemala · NIVEA — Sun Allergy:** 8 celdas + referencias de 20 homepages a 10
  enlaces directos comprobados
- **México · NIVEA — Sudoración excesiva:** 13 celdas + claims ajustados
- Los **pendientes de decisión** de cada uno, que son reales y estaban registrados

Y en SEO/Technical, lo detectado y no resuelto: el `<title>` equivocado de la PDP
de Tono Natural en NIVEA México, el desajuste de `I59`, las `Local URL not found`
de Guatemala y Chile.

## Dos secciones agregadas que no pidieron

1. **«Cómo se trabaja la hoja»** — mapa de columnas A–K y qué exige cada control
   (B3, B4, B5, y que **B6 está mal en la plantilla**: va sin comodines, así que
   nadie debe maquillar el H1 para que pase).
2. **«La regla dura del encargo»** — que cada país se traduce distinto a propósito
   (anti-canibalización) y que los enlaces internos **se relocalizan, no se
   copian**.

**Por qué:** sin esas dos, quien la cubra puede romper seis meses de trabajo sin
darse cuenta. Un traspaso que solo lista pendientes no sirve si el reemplazo no
sabe cómo se trabaja.

## Lo que quedó en blanco A PROPÓSITO

Colombia, Ecuador, Perú, **todo Eucerin**, H2 Content Plans, Uploads/JIRA,
reporting, stakeholders y links. **No hay datos de eso en ninguna parte y no se
inventó nada** — van marcados para que los complete ella.

## Ambigüedad que quedó planteada, no adivinada

Su mensaje decía *«ayúdame a redactar un correo que me enviaron… tú lo ordenas»*.
Se interpretó como **ordenar lo que le piden** y se entregó el documento, pero se
le preguntó explícitamente si además quiere **la respuesta al correo redactada**.
También se le ofreció dejarlo como **Google Doc editable** en su Drive.

## Estado

🟡 Entregado el borrador. Esperando: (a) si quiere la respuesta al correo, (b) si
lo quiere como Google Doc, (c) que ella complete los campos en blanco.

Relacionado: `estado.md`, `chile-nivea-bb-cc-cream.md`,
`guatemala-nivea-sun-allergy.md`, `mexico-nivea-sudoracion.md`


---

## 20-ago 11:46 — Connie hizo su propio doc y pidió mejorarlo

Ella armó **«Estado SEO»** en Google Docs
(`1QMFAzWbsZQvN2-9S_iIpvmPQoq0JfWhvHoTGfOoreT8`) y pidió *«mejóralo para que
entiendan mejor»*. Se editó **su documento**, no una copia.

**Respaldo del original:** `backup-traspaso-doc-20ago.json` (mismo criterio que los
backups de las hojas).

### Lo que se hizo

Su contenido estaba bien pero venía en **dos párrafos larguísimos** donde se
mezclaban el circuito de JIRA, la revisión de Nidia, el SharePoint y Trello.
Se reordenó en 4 secciones con encabezado H1/H2, sin quitar información:

1. **Contenidos** — circuito de publicación numerado + los «not ready»
2. **Auditorías y cambios técnicos** — Paso 1/2/3 alrededor de sus capturas
3. **Estado actual del SEO**
4. **Si hacen falta contenidos antes de mi vuelta**

Añadido: bloque **Personas clave** (Pato, Nidia, IRIS), negrita en el punto de
Trello y en «Pato está copiado», y el SharePoint convertido en enlace clicable.

### ⚠️ Lo delicado: las 3 imágenes

El doc tenía **3 capturas incrustadas** que su texto referencia («en esta parte»,
«luego clic a esta otra»). **Reescribir el cuerpo entero las habría borrado.**

Solución: se mapearon los índices exactos y se editó **por rangos, de mayor a
menor índice** (para no descuadrar los índices de las ediciones siguientes),
borrando solo el texto y **nunca el rango que contiene la imagen**. Verificado
leyendo de vuelta: **3 imágenes antes, 3 después**.

**Receta para editar un Google Doc sin romperlo:**

- Leer y mapear `startIndex`/`endIndex` de cada párrafo antes de tocar nada.
- Para reemplazar el texto de un párrafo `[s,e)` **borrar `[s, e-1)`**, así se
  conserva el salto de párrafo.
- Si el párrafo contiene una imagen, el `inlineObjectElement` ocupa **un índice**:
  borrar solo hasta ahí.
- Aplicar las ediciones **de mayor a menor índice**.
- Los estilos (`updateParagraphStyle`, `updateTextStyle`) **no mueven índices**:
  se pueden hacer todos juntos en una segunda pasada.

### Datos operativos que ella aportó y conviene no perder

- **JIRA demora 2–3 semanas** en subir un artículo; responde el ticket con la URL.
- Al revisar esa URL: links, botones e imágenes.
- **Pato** está copiado en todos los tickets. **Nidia** revisa y aprueba MX y GT.
- **JIRA saca el artículo final desde Trello**, no del SharePoint: un cambio que
  no llegue a la tarjeta de Trello **no se publica**.
- **NIVEA está parado**; la única auditoría posible hoy es la de **Eucerin**.
- **Ya no se necesita la aprobación de IRIS**: se manda directo a JIRA, y por eso
  ella puede hacer hasta 5 artículos aun estando fuera.

### Pendiente

Su doc cubre Contenidos, JIRA, auditorías y estado. De los nueve puntos pedidos
faltan **H2 Content Plans**, **reporting/rankings**, **stakeholders por país** y el
resto de **links** (Trello, JIRA, dashboards). Ofrecido agregarlos con lo que ella
dicte.
