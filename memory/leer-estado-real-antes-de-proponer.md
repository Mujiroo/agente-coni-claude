---
name: leer-estado-real-antes-de-proponer
description: El 21-ago le propuse a Connie agregar una keyword que llevaba semanas en el grupo; construí toda una explicación encima de un dato que nunca verifiqué.
metadata:
  type: feedback
---

**El 21-ago-2026 le propuse a Connie agregar `botas de bomberos` al grupo Botas.
Ya estaba ahí**, en frase, activa y elegible. Ella aprobó el cambio (msg 276) y al
ir a aplicarlo descubrí que la propuesta 1 era un **no-op**.

**Lo grave no fue el no-op, fue lo que colgué encima.** Con esa columna mal llenada
concluí que «el grupo no arranca porque sus keywords tienen volumen cero», lo
escribí como hallazgo en `clientes/sudtec/botas-volumen-keywords.md` y se lo mandé
como diagnóstico. Las dos keywords más buscadas del grupo (390 y 260/mes) estaban
dentro todo el tiempo.

**De dónde salió el error:** medí el volumen con el Planificador —eso sí fue real—
pero la columna «¿está en el grupo?» la llené **de memoria**, de lo que recordaba
haber armado el 19-ago. Nunca consulté `ad_group_criterion`. Una sola consulta lo
habría desmentido.

**La regla:** antes de proponer agregar, pausar o cambiar algo en una cuenta,
**leer el estado real de eso mismo en la misma tanda de consultas** en que leo los
datos de apoyo. Si voy a decir «no está», tengo que haber mirado. Nunca describir
la configuración de una cuenta de memoria ni desde lo que yo mismo dejé armado
días atrás: la cuenta cambia, y mi recuerdo de lo que hice no es evidencia.

**Vale doble cuando el dato es la premisa de un diagnóstico.** Un dato de apoyo
equivocado da una recomendación floja; una premisa equivocada da una explicación
entera equivocada, y esa se la llevo a Connie como si fuera la respuesta.

Cuando lo descubra, **corregirlo antes de que ella actúe**, aunque ya haya
aprobado — y decir con todas las letras qué parte de lo anterior queda sin efecto.

Relacionado: [[cuota-google-ads]] — agrupar consultas no es excusa para saltarse la
que verifica la premisa; esa es justamente la que hay que incluir en el grupo.
