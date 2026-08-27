---
name: google-fotos-liberar-espacio
description: Connie casi libera 109 GB de fotos con una cuenta Google de 15 GB casi vacía; el número no cuadraba y había que frenarla.
metadata:
  type: project
---

**27-ago-2026 (21:51 en China).** Connie mandó la pantalla de **«Liberar espacio»**
de Google Fotos —teléfono al **96%**, botón **«Liberar 109 GB»**— preguntando si lo
que se borra del celular queda arriba. Textual: *«No quiero perder nada»*.

## Lo que la pantalla dice, y por qué no bastaba

La pantalla afirma que **«estos elementos ya tienen copia de seguridad»** y que
podrá seguir viéndolos. En teoría es correcto: esa función borra **solo** copias
locales de material ya respaldado.

**Pero el número no cuadraba.** Consulté su cuota real por Maton
(`google-drive/drive/v3/about?fields=storageQuota`):

| Dato | Valor |
|---|---|
| Límite | **15 GB** (16.106.127.360 B) |
| Usado | **1,5 GB** (1.622.005.970 B) |
| De eso, Drive | 0,30 GB |
| Libre | **13,5 GB** |

**109 GB no caben en una cuenta de 15 GB**, y menos en una que está usada al 10%.
Si ese material estuviera realmente respaldado ahí, la cuenta estaría llena.

**Hipótesis más probable:** el teléfono respalda en **otra cuenta de Google**
(distinta de `pfeifer.constanza@gmail.com`, que es la que yo veo por Maton), quizá
una con almacenamiento pagado. Le pedí la pantalla de perfil de Google Fotos para
confirmarlo antes de que apriete nada.

## Las dos advertencias que un «sí, es seguro» se habría comido

1. **Está en China y Google está bloqueado.** Aunque el respaldo esté perfecto, si
   libera ahora **no puede ver esas fotos** hasta volver, o con VPN. Las del viaje
   se quedan en el teléfono.
2. **La calidad del respaldo.** Con «**Ahorro de espacio**» las copias de arriba
   quedan **comprimidas** y el borrado se lleva los originales. Solo con
   «**Original**» quedan intactas.

Alternativa sin riesgo que le di: vaciar caché de **WeChat y WhatsApp**, que en un
viaje junta varios GB y no es material suyo.

## La lección, que es la que se repite

**Cuando la pregunta es «¿es seguro?», la respuesta genérica correcta puede ser la
respuesta equivocada para esta persona.** El manual dice que liberar espacio es
seguro, y lo es — pero solo si el supuesto de fondo (que está respaldado) se
cumple. **Tenía cómo verificar ese supuesto y verificarlo cambió la respuesta.**

Regla: ante un botón irreversible, **comprobar el supuesto contra los datos
reales** antes de dar el visto bueno. Si los números no cierran, frenar y pedir el
dato que falta — aunque la pantalla afirme lo contrario.

## Resuelto el mismo día (msg 494)

**Ella confirmó: «tengo mi Google Fotos con otro correo».** La hipótesis era
correcta — yo estaba mirando `pfeifer.constanza@gmail.com`, que es la cuenta
conectada a Maton, y su Google Fotos vive en otra. Los 109 GB están en esa otra
cuenta y el descuadre desaparece.

**Lo que esto deja como dato permanente, y es lo que hay que recordar:**

> Su **Google Fotos NO es la cuenta que yo veo**. `pfeifer.constanza@gmail.com` es
> su correo/Drive/Calendar, pero las fotos están en otro correo que **no tengo
> conectado**. Cualquier pregunta sobre sus fotos **no la puedo verificar yo**:
> hay que pedirle a ella la pantalla, o conectar esa cuenta (OAuth, solo lo puede
> hacer ella).

Le dejé igual las dos advertencias que **siguen valiendo** aunque el respaldo esté
sano: que confirme que dice «copia de seguridad completada», y que **en China no va
a poder ver lo que libere** porque Google está bloqueado — así que lo antiguo sí,
pero las fotos **de este viaje** que se queden en el teléfono hasta el 18-sep.

**Cerrado.** No perdió nada y no la frené de más: la alerta duró 4 minutos.

Relacionado: [[notas-connie]], [[connie]], [[leer-estado-real-antes-de-proponer]]
