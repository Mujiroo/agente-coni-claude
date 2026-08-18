# SUDTEC — reenvío de cotizaciones cg@ → bd@

*Abierto: 17-ago-2026, a pedido de Connie.*

## Lo que ella pidió

Reenviar a `bd@sudtec.cl` los correos que llegan de `cg@sudtec.cl`, porque bd@
«no está recibiendo las cotizaciones». Solo los nuevos, nunca dos veces.

## Lo que encontré al revisar (importante)

**`bd@sudtec.cl` ya viene como destinatario directo en TODOS los correos de
`cg@`**, sin excepción, desde por lo menos el **3 de marzo de 2026**. El `To:` es
siempre el mismo:

```
c.montilla@south-pacific.cl, bd@sudtec.cl, pfeifer.constanza@gmail.com
```

O sea: **cg@ sí le está escribiendo a bd@**. Lo que falla es la entrega o el
filtrado del lado de la casilla `bd@sudtec.cl`. El reenvío es un **parche**, no
el arreglo.

Pista sobre la causa: el original sale por el relay de sudtec (MailChannels +
ImunifyEmail) y trae la cabecera **`X-MC-Relay: Junk`** — algo en el propio
trayecto de sudtec lo está clasificando como basura. A la casilla de Connie
igual le llega a Recibidos; a bd@ puede que lo esté comiendo esa clasificación.
Quien administre el correo de sudtec.cl debería mirar ahí.

## Volumen

- **201** correos de cg@ en total en la casilla de Connie
- **55** en los últimos 30 días · **15** en los últimos 7 → **~2 por día**
- Todos con el asunto `[Solicitud de presupuesto]`, cuerpo HTML, sin adjuntos

## La solución que armé

`bin/reenvio_sudtec.py` — corre por cron, y en cada pasada:

1. Busca en Gmail `from:cg@sudtec.cl newer_than:2d` (la ventana de 2 días da
   margen si estuve caído; no provoca duplicados porque el filtro real es el
   estado).
2. Descarta los id que ya están en `memory/estado/reenvio_sudtec.json`.
3. Reconstruye cada correo **limpio** (descarta las cabeceras del relay de
   sudtec, incluida la `Junk`) conservando el cuerpo HTML intacto, y lo manda a
   `bd@sudtec.cl` con asunto `RV: [Solicitud de presupuesto]` y `Reply-To:
   cg@sudtec.cl`, para que bd@ conteste al cotizador y no a Connie.
4. Guarda el id **apenas envía cada uno**, no al final: si me corto a la mitad,
   no reenvío dos veces.

En la primera corrida real **no manda el historial**: marca lo que ya existe
como visto y desde ahí en adelante solo reenvía lo nuevo.

Modo simulación (`sin --enviar`) para ver qué haría sin mandar nada.

## Estado

- 🟡 **Escrito y probado en simulación. NO está enviando todavía** — falta el OK
  de Connie, porque el primer envío le habla a un tercero.
- Pendiente de definir con ella: si quiere que reenvíe también lo atrasado, y si
  se persigue el arreglo de fondo con quien administra el correo de sudtec.cl.
