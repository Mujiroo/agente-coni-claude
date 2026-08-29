---
name: getfile-lento-no-caido
description: getFile de Telegram puede tardar más de 30s y responder bien; el helper se rendía antes de tiempo y me dejaba sin ver las fotos de Connie.
metadata:
  type: reference
---

**27-ago-2026, en plena emergencia.** Connie estaba en la estación de tren de
Chongqing, a 30 minutos de que saliera su tren, y me mandó la foto de un letrero
que no entendía. `bin/tg_file.sh` devolvió **`ERROR-RED`** cinco veces seguidas.

**Pero la API no estaba caída:** `getMe` respondía **200 en 0,58 s**. Lo que
pasaba es que `getFile` tardaba **más de 30 s**, y el helper cortaba justo ahí.
La misma llamada con `--max-time 45` **respondió sin problema**.

**Arreglado el mismo día:** el helper ahora usa **60 s y 3 intentos** con 3 s de
espera entre medio. Verificado: la misma foto que fallaba bajó a la primera.

**La lección, más allá del script:** *lento* y *caído* se ven igual desde afuera,
y confundirlos me hizo decirle a Connie que no podía ver su foto cuando en
realidad sí podía. **Antes de declarar caída una API, probar una ruta barata de
la misma API** (`getMe` acá) para separar «el servicio no está» de «esta llamada
tarda más de lo que yo aguanto».

**Lo que sí estuvo bien:** avisarle de inmediato que no me llegaba la foto, en vez
de quedarme en silencio intentando, y mandarle mientras tanto una frase en chino
para mostrarle a un funcionario. Un agente callado se ve idéntico a uno caído —
y con ella corriendo contra un tren, eso se paga caro.

## 28-ago-2026: volvió a pasar, y el arreglo anterior no bastaba

Connie iba **en el bus dentro del parque de Zhangjiajie** y mandó la foto del
letrero. Los **tres** intentos de 60 s fallaron. Pero `getMe` seguía respondiendo
**200 en 0,57 s**, y una llamada manual hecha enseguida **sí funcionó, en 19 s**.

**Lo que medí, y que cambia el diseño del reintento:**

- Cuando `getFile` falla, **cuelga hasta agotar el timeout completo**: HTTP `000`
  exactamente a los 50 s, 60 s y 90 s. O sea **un techo más alto no ayuda** en una
  llamada colgada — solo quema el presupuesto de tiempo.
- Cuando responde, **responde rápido**: 19 s ese día, y <45 s el 27-ago.

**Conclusión contraintuitiva:** el arreglo del 27-ago (subir el techo) iba en la
dirección equivocada. Lo que sirve es **muchos intentos cortos** para pillar la
ventana buena, y **un par largos al final** por si toca una lenta de verdad.

**El helper quedó en `20/20/45/45/75 s` — 5 oportunidades con el mismo techo total
que las 3 de antes.** Probado con la misma foto que había fallado: bajó en **4,9 s**.

**La lección que se repite y ahora está medida:** *lento* y *caído* se ven igual, y
el desempate es **probar una ruta barata de la misma API** (`getMe`). Eso ya estaba
en esta nota; lo nuevo es que **el patrón de la falla decide la forma del
reintento** — si el fallo cuelga hasta el timeout, hay que acortar el timeout, no
alargarlo.

Relacionado: [[canal-y-formato]], [[hora-de-connie-no-la-mia]], [[notas-connie]]
