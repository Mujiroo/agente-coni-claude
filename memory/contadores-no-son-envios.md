---
name: contadores-no-son-envios
description: Reporté 7 reenvíos a Connie cuando habían sido 2; el 7 era el anti-duplicado, no los envíos.
metadata:
  type: feedback
---

**El 18-ago-2026 le dije a Connie que se habían reenviado «7 cotizaciones» a
`bd@sudtec.cl`. Eran 2.** Ella lo cazó al toque: *«7 reenviadas? que hablas? solo
han llegado dos cotizaciones»*. Tenía razón.

**Qué pasó:** leí `len(reenviados)` del archivo de estado y lo reporté como si
fuera un contador de envíos. **No lo es**: esa lista es el **anti-duplicado**, e
incluye los **5 correos del historial que la primera corrida marcó como vistos
sin enviarlos**, justamente para no inundar a bd@ con el pasado.

**Por qué importa:** un número inventado en un reporte operativo es peor que no
dar el número. Ella toma decisiones con eso y, además, si no lo hubiera cazado,
habría quedado creyendo que a bd@ le llegaron cinco correos que nunca existieron.

**Cómo se corrigió:** `bin/reenvio_sudtec.py` ahora guarda una bitácora aparte,
`enviados`, con los envíos **reales**, y tiene
`python3 bin/reenvio_sudtec.py --resumen` que muestra los dos números separados y
sin mezclarlos.

**La regla, que vale más allá de este script:** antes de darle una cifra, **hay
que preguntarse qué cuenta exactamente esa variable**. Si el dato tiene una fuente
externa verificable —la bandeja de enviados, la página pública, la ficha del
producto—, esa fuente manda por sobre mi archivo de estado.

Relacionado: [[cuota-y-tandas]]
