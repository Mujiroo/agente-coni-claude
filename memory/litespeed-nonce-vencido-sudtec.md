---
name: litespeed-nonce-vencido-sudtec
description: DESCARTADA — creí que el nonce vencido en páginas cacheadas rompía el cotizador de sudtec.cl; se probó y YITH lo acepta igual.
metadata:
  type: feedback
---

# ❌ HIPÓTESIS FALSA — se probó y no era

**El 24-ago-2026 le mandé a Connie (msg 328) un diagnóstico equivocado**, con
cifras y todo, y ella me dijo «dale» para actuar sobre él. Lo salvó haber probado
antes de tocar.

## Lo que creí

LiteSpeed sirve páginas de 44-65 h de antigüedad; el botón de YITH lleva un nonce
de WordPress que vive 24 h; **por lo tanto** el visitante hace clic con un token
vencido y el envío falla en silencio.

Todo lo observable era cierto y verificado:

- home cacheada del 21-ago 22:13, `/product-category/epp/botas/` del 22-ago 03:30
- el nonce cacheado (`1d9990fee6`) **difiere** del fresco (`a6396ee230`)
- con `?gclid=` y `?utm_source=` LiteSpeed responde `hit`: **el tráfico de Ads
  recibe la versión vieja**

## Por qué era falso igual

**YITH no valida ese nonce con `wp_verify_nonce` estricto.** Probado contra
producción, mismo producto, los dos tokens:

    POST /?wc-ajax=yith_ywraq_action
    context=frontend&action=yith_ywraq_action&ywraq_action=add_item&product_id=3066&wp_nonce=<X>

| nonce | respuesta |
|---|---|
| vencido `1d9990fee6` | `{"result":"true","message":"Producto agregado a la lista"}` |
| fresco `a6396ee230` | `{"result":"true","message":"Producto agregado a la lista"}` |

**Idénticas.** El nonce viejo funciona.

## La lección, que es la que vale

**Encadené hechos verificados hasta una conclusión que no verifiqué.** Cada
eslabón era real; el salto «por lo tanto falla» era una suposición, y la presenté
con el mismo tono de certeza que las mediciones.

**Regla: antes de mandar un diagnóstico, probar el eslabón final**, el que dice
que la cosa efectivamente se rompe. Acá costaba una llamada `curl` y la hice
**después** de haber avisado, no antes. Ver [[leer-estado-real-antes-de-proponer]].

**Segunda lección:** no leí `clientes/sudtec/cotizaciones-sequia-20ago.md` antes de
diagnosticar, y ahí estaba escrito que el formulario **ya se había verificado sano
el 21-ago** y que **purgar la caché de este sitio provocó errores 500** el 20-ago.
Media hora de investigación y un mensaje equivocado que la carpeta ya respondía.

## Lo que sí quedó probado y sirve

- **El endpoint del cotizador se puede probar desde fuera** con
  `/?wc-ajax=yith_ywraq_action` — la sesión del 20-ago lo intentó por
  `admin-ajax.php` y obtuvo `400/0` para todo, y concluyó que era inverificable.
  **Con `wc-ajax` sí responde de verdad.**
- Agregar un ítem **no crea pedido ni manda correo**: es lista de sesión. Prueba barata.
- La página `/cotizacion-sudtec/` **no se cachea** (`x-litespeed-cache-control: no-cache`),
  está bien configurada.
- Los destinos reales de los anuncios son **`/lista-productos/`** (General e Improfor,
  el grueso del tráfico) y variantes con `?yith_wcan=1&product_cat=…`. Todas dan 200
  con botones, en escritorio y en móvil.

Relacionado: [[litespeed-cachea-la-api-rest]], [[verificar-sin-rompe-cache]],
[[contadores-no-son-envios]].
