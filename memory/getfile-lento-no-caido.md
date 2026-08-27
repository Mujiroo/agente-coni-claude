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

Relacionado: [[canal-y-formato]], [[hora-de-connie-no-la-mia]]
