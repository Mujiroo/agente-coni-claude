# SUDTEC — Snippet de textos del cotizador (PREPARADO, NO APLICADO)

**Pedido por Connie el 24-ago-2026** (msgs 332-333): el aviso que sale al agregar
un producto dice **«Explorar la lista»**, y ella quiere algo tipo *«Producto
agregado. Enviar cotización»*. Dijo **«para todo»**, o sea en todo el sitio.

**Por qué vale la pena más allá del gusto:** «Explorar la lista» invita a *mirar*,
no a *pedir*. Es el paso final del embudo y no tiene llamada a la acción.

## Las tres cadenas reales (verificadas en producción)

Salen del plugin YITH, renderizadas en el HTML y también en la respuesta AJAX:

| Cuándo | Hoy dice | Propuesto |
|---|---|---|
| Al agregar (`result:"true"`) | `Producto agregado a la lista` | **Producto agregado a tu cotización** |
| Si ya estaba (`result:"exists"`) | `Este producto ya está en su lista de solicitud de cotización.` | **Este producto ya está en tu cotización** |
| El enlace | `Explorar la lista` | **Enviar cotización →** |

Comprobado con:

    curl -s -d "context=frontend&action=yith_ywraq_action&ywraq_action=add_item&product_id=3066&wp_nonce=<n>&yith-add-to-cart=3066&quantity=1" \
      "https://www.sudtec.cl/?wc-ajax=yith_ywraq_action"

En el HTML viven en `.yith_ywraq_add_item_response_message` y
`.yith_ywraq_add_item_browse_message`, ocultos con `display:none` (28 de cada uno
en `/lista-productos/`, uno por producto).

## El snippet

Scope **front-end**. Solo intercambia textos: no toca plugin, plantillas ni base de
datos. **Borrarlo revierte todo.**

```php
add_filter( 'gettext', 'kai_textos_cotizador', 20, 3 );

function kai_textos_cotizador( $traducido, $original, $dominio ) {
	static $mapa = array(
		'Explorar la lista'                                            => 'Enviar cotización →',
		'Producto agregado a la lista'                                 => 'Producto agregado a tu cotización',
		'Este producto ya está en su lista de solicitud de cotización.' => 'Este producto ya está en tu cotización',
	);
	return isset( $mapa[ $traducido ] ) ? $mapa[ $traducido ] : $traducido;
}
```

**Por qué filtra sobre `$traducido` y no sobre `$original`:** el sitio está en
español y no se conocen con certeza los *msgid* en inglés del plugin premium.
Comparar contra la cadena que efectivamente se muestra es lo que se verificó.

**Riesgo de colateral:** bajo — son tres cadenas exactas y largas. Aun así, tras
aplicarlo hay que **revisar la página pública**, no solo el código de respuesta.

## Estado

**Propuesto a Connie en msg 336, esperando su OK sobre las palabras.** No aplicado.
