---
name: giveaway-yesstyle-vigia
description: Connie pidió que le avise cuando se abra el Glow Up Giveaway de YesStyle; se vigila la página pública, porque por correo no se anuncia nunca.
metadata:
  type: project
---

**16-sep-2026 (msg 1231).** Connie mandó la captura de la app de YesStyle
—«Giveaway YesStyle Glow Up / Próximamente»— y pidió que le avise cuando se abra.

**Cómo se resolvió:** la misma sección existe en la **web pública, sin login**:
`https://www.yesstyle.com/en/glow-up-giveaway.html`. O sea **no hace falta su
cuenta** ni pedirle claves. Montado en `bin/vigia_yesstyle.sh` + cron a las **:50,
de 08:00 a 22:00** de Chile.

**El correo NO es canal, y está verificado:** tiene **200+** correos de YesStyle y
**cero** que digan giveaway, patrocinado, sponsored o sorteo. Los 3 que salen por
«glow up» son el newsletter semanal genérico. No montar nada sobre Gmail para esto.

**Cómo lee el estado el vigía:** la `<section ...__cardView>` dice hoy
`<h3>Coming Soon</h3>`. Cuando abra, ahí van los productos con su botón
**«Claim Now»** (la cadena ya está en el diccionario de la página). El script
avisa cuando el «Coming Soon» **desaparece de ese bloque**, no de todo el HTML.

**Tres guardas, para no gritar en falso:** HTTP 200, más de 100 KB, y que la
página contenga «Glow Up Giveaway». Si falla cualquiera → `SIN-DATO` y silencio.
Un falso positivo la hace correr a una página vacía. Las cuatro ramas (abierto,
repetido, cerrado, roto) se probaron con HTML falso antes de montarlo.

**Why:** el giveaway es **por orden de llegada y stock limitado**, así que un
aviso tarde no sirve de nada.

**Las bases, leídas el 16-sep** (`yesstyle.com/en/help/section.html/hsi.2511`),
porque ella dijo «no creo que sea apta» (msg 1233) y **sí lo es**:

- **No hay que ser influencer ni tener un mínimo de seguidores.** Basta ser
  **miembro** de YesStyle —no comprador invitado—, y ella ya tiene cuenta.
- **Compra mínima de US$ 29** para reclamar el producto gratis. O sea el producto
  es gratis, pero **cuelga de un pedido suyo**: decírselo siempre, no venderlo como
  regalo sin condiciones.
- **Reseña de 60+ caracteres** dentro de los 2 meses del envío. La reseña aprobada
  da un cupón.
- **Uno a la vez**, hasta agotar stock.

**How to apply:**
- Si YesStyle rediseña la página, el vigía cae a `SIN-DATO` y **se calla**: hay que
  mirar el HTML de nuevo, no dar por hecho que no hay giveaways.
- **El programa de influencers quedó descartado**: se le ofreció el 16-sep y contestó
  «no creo que sea apta» (msg 1233). Es **otra cosa** que el Glow Up Giveaway. No
  reofrecérselo salvo que ella lo saque.

Relacionado: [[no-importar-agent-cron]], [[notas-connie]]
