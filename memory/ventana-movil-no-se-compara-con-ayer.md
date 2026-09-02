---
name: ventana-movil-no-se-compara-con-ayer
description: Una métrica de ventana móvil comparada contra la de ayer mide el calendario, no la cuenta; el 2-sep casi mando una falsa alarma por eso.
metadata:
  type: feedback
---

**El 2-sep-2026 la vigilancia de Sudtec marcó 1,0 conv/día contra 1,4 del día
anterior, y CPA 9.047 contra 6.278.** Leído de frente son un 29% y un 44% peor, y
estuve a punto de mandarle eso a Connie como deterioro nuevo.

**No era deterioro.** La métrica es un promedio de **ventana móvil de 7 días**. Ese
día salió del cálculo el **25-ago (4,3 conversiones)** y entró el **1-sep (1,0)**:

    (1,0 − 4,3) / 7 = −0,47 conv/día        ventana 1,47 → 1,00 = −0,47

El delta se explica **entero** por qué día salió, no por lo que pasó. Los días
individuales llevaban planos en ~1 conversión hacía casi una semana.

**La regla:** una métrica de ventana móvil **solo se compara contra la línea base**,
nunca contra su propio valor de ayer. Si quiero saber si algo empeoró **hoy**, miro
**el día suelto** contra la base. La diferencia entre dos ventanas móviles
consecutivas es aritmética del calendario disfrazada de hallazgo.

**Dónde quedó aplicado:** por esto se descartó poner «avisa de nuevo si empeoró un
25%» en `bin/vigilancia_cambios.py`. Habría disparado ese mismo día sin que pasara
nada. La anti-repetición quedó por **cadencia** (primer día de la racha, y
recordatorio cada 7), no por variación.

**Lo otro que se decidió el mismo día:** con el mismo cuadro ya avisado el 1-sep y el
veredicto prometido para el 3-sep, **no se le escribió**. Persistir no es noticia.
Un agente callado se ve igual que uno caído, pero repetir tres veces la misma foto
también gasta la atención de Connie — y ella pidió expresamente menos ruido.

Va junto con [[impression-share-censurado]] y
[[ventana-corta-condena-keywords-buenas]]: los tres son la misma familia de error
—sacar conclusiones de una ventana que no da para sostenerlas—.
