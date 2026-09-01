# Siete días no alcanzan para condenar una keyword

El 1-sep-2026 le propuse a Connie pausar dos keywords amplias de Sudtec porque en una
ventana de **7 días** (25 al 31-ago) se llevaban el 63% del gasto con 2 conversiones.
Ella preguntó: *«¿pero esas cómo se han comportado los meses anteriores?»*. El histórico
mensual dio vuelta el veredicto.

**`equipos de bomberos` (amplia)** — es de las mejores de la cuenta:

| mes | conversiones | CPA |
|---|---|---|
| mar | 31,6 | 1.663 |
| abr | 45,5 | 1.044 |
| may | 54,0 | 1.291 |
| jun | 13,2 | 3.386 |
| jul | **60,0** | 1.601 |
| ago | 43,5 | 1.975 |

En los 7 días que yo miré trajo 0 conversiones. **En agosto completo trajo 43,5.**
Pausarla habría apagado el motor de la cuenta.

**`equipo de protección personal` (amplia)** sí muestra deterioro real y sostenido:
CPA de ~1.400 (mar-abr) a **4.006** en agosto, y agosto fue su mes de mayor gasto
(84.142) con 21 conversiones, cuando en mayo con 69.127 trajo 37,8. Aun así, 21
conversiones no justifican pausarla en medio de un colapso general de la cuenta.

**El error de fondo:** la ventana de 7 días cayó justo en el peor momento de *toda* la
cuenta. Le atribuí a dos keywords un deterioro que era general. Con ~4 conversiones/día
de base, 7 días son ~30 conversiones repartidas entre 20 keywords: ruido, no señal.

**La regla:** antes de pausar una keyword, **mirar como mínimo 3-6 meses por mes**
(`segments.month` en `keyword_view`). Compararla contra sí misma en el tiempo, no contra
el resto de la cuenta en una ventana corta. Y si el período reciente es anómalo para toda
la cuenta, ninguna comparación dentro de ese período sirve.

Va junto con [[impression-share-censurado]]: los dos errores del mismo día salieron de
teorizar sobre datos insuficientes en vez de bajar al histórico.
