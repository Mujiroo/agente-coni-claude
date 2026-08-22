# SUDTEC — Línea base de cotizaciones (300 pedidos, 10-mar a 21-ago-2026)

*Construida el 22-ago-2026 porque Connie preguntó (msg 303): «no han llegado
conversiones y el miércoles llegaron muchas, eso me hizo ruido».*

**Sirve para no volver a diagnosticar de memoria.** Antes de decirle a Connie que
un día en cero es normal —o que no lo es— se contrasta contra esta tabla.

## Los números

- **300 cotizaciones en 165 días** → media **1,8 por día**
- **33 días cerraron en cero = 20%.** Uno de cada cinco días no entra ninguna.

## Por día de la semana

| Día | Media | Días en cero |
|---|---|---|
| lunes | 2,2 | 4% |
| martes | 2,6 | 4% |
| **miércoles** | **1,7** | 21% |
| **jueves** | **2,8** | **0%** ← el mejor, nunca uno en cero |
| **viernes** | **1,5** | **25%** |
| **sábado** | **0,8** | **57%** ← más de la mitad en cero |
| domingo | 1,2 | 30% |

## Rachas de días en cero

| Largo | Veces |
|---|---|
| 1 día | 20 |
| 2 días | 5 |
| 3 días | 1 |

**La racha más larga en cinco meses fue de 3 días** (19-jun, arrancando un viernes).

**Viernes en cero seguido de sábado en cero: 4 de 24 viernes (17%).** Ocurrió el
**7-8 de agosto**, dos semanas antes de que Connie preguntara, sin que nada
estuviera roto.

## Lo que respondía a su duda

**El miércoles 19-ago (6 cotizaciones) fue el dato atípico, no el cero del viernes.**
Los miércoles promedian 1,7. Ella ancló la expectativa en un día excepcional y
contra esa referencia todo lo posterior parecía derrumbe.

Viernes 21 en cero → pasa el 25% de los viernes.
Sábado 22 en cero → pasa el 57% de los sábados.

## Cómo se reproduce

    for p in 1 2 3; do
      python3 bin/sudtec_wp.py api \
        "wc/v3/orders?per_page=100&page=$p&_fields=id,number,date_created&orderby=date&order=desc" \
        --limite 900000
    done

⚠️ **`bin/sudtec_wp.py` trunca la salida en 6.000 caracteres por defecto.** Sin
`--limite` el JSON llega cortado y los conteos salen mal —o el `json.load` revienta
con «Invalid control character». **Subir `--limite` siempre que se pidan listados
largos.**

Y recordar: **`date_created` viene en UTC**, hay que restar 4 h.
Ver [[ads-hora-chile-woo-utc]].
