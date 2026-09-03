---
name: agrupar-por-id-no-por-nombre
description: En Google Ads los nombres de grupo se repiten; agrupar por nombre fusionó dos grupos distintos y me hizo reportarle a Connie tres grupos vivos cuando solo uno lo estaba.
metadata:
  type: feedback
---

**3-sep-2026, Sudtec.** Le dije a Connie que había **3 grupos de botas dormidos** y le
propuse pausar los tres. Ella aprobó. **Al releer el estado real antes de ejecutar,
solo uno estaba vivo.**

| grupo | estado real |
|---|---|
| `Botas` (`197186444097`, en `Campaña Sudtec`) | **ENABLED** — el único a pausar |
| `Botas de Bomberos` (dos ids distintos) | **REMOVED** desde antes |
| `Grupo de anuncios 1` | ENABLED, pero su campaña `Botas Bomberos` está **REMOVED**: no puede servir |

**De dónde salió el error:** mi script agrupaba por `ad_group.name`. En la cuenta hay
**dos grupos distintos llamados «Botas»** —el viejo en `Campaña Sudtec` y el nuevo que
yo mismo había creado horas antes en `Sudtec · Bomberos`— y el diccionario por nombre
**los fusionó**, mostrando 15 keywords donde el grupo nuevo tenía 6. También había
**dos** `Botas de Bomberos` con ids distintos.

**La regla:** en Google Ads **agrupar y decidir siempre por `id`, nunca por nombre.**
Los nombres se repiten entre campañas y sobreviven a los borrados. Si un recuento sale
raro —más keywords de las que creé, dos filas que deberían ser una—, la primera
sospecha es la colisión de nombres, no la cuenta.

**El segundo filtro que faltaba:** un grupo `ENABLED` dentro de una **campaña
`REMOVED`** no muestra nada. Para saber si algo está de verdad vivo hay que mirar
**el estado del grupo Y el de su campaña**.

**Cómo se resolvió con ella:** se pausó el único que correspondía y **se le contó la
diferencia en el mismo mensaje**, sin esconderla para que la propuesta se viera
prolija — la intención aprobada (dejar de partir los datos de botas) se cumplía igual.
Ver [[verificar-estado-antes-de-ejecutar-lo-aprobado]] y
[[leer-estado-real-antes-de-proponer]].
