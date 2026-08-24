# SUDTEC — Snippet de textos del cotizador (APLICADO 24-ago-2026, snippet id 15)

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

## ❌ El primer intento falló: NO son traducciones, son opciones

Escribí el snippet con un filtro **`gettext`** dando por hecho que las cadenas
venían del sistema de traducciones. Quedó activo, sin error de PHP… **y no cambió
nada**. Lo delató el AJAX, que **no se cachea** y seguía devolviendo el texto viejo:
si hubiera sido caché, ahí se habría visto el cambio.

**Son opciones del plugin**, encontradas leyendo `wp_options`:

| Opción | Valor original |
|---|---|
| `ywraq_show_browse_list` | `Explorar la lista` |
| `ywraq_show_product_added` | `Producto agregado a la lista` |
| `ywraq_show_already_in_quote` | `Este producto ya está en su lista de solicitud de cotización.` |

**Pista que lo anticipaba y no aproveché:** el botón dice «Agregar a cotizador»,
que no es una traducción por defecto de nada — era señal de que estos textos se
configuran, no se traducen.

## El snippet que SÍ funciona (id 15, scope `front-end`, activo)

```php
add_filter( 'pre_option_ywraq_show_browse_list', function () {
	return 'Enviar cotización →';
} );

add_filter( 'pre_option_ywraq_show_product_added', function () {
	return 'Producto agregado a tu cotización';
} );

add_filter( 'pre_option_ywraq_show_already_in_quote', function () {
	return 'Este producto ya está en tu cotización';
} );
```

`pre_option_*` **no escribe en la base de datos**: los valores originales siguen
intactos y **borrar el snippet revierte todo**. Scope `front-end` a propósito, para
que el panel de YITH siga mostrando los valores reales si alguien va a editarlos.

## Verificado en producción

- HTML fresco: **28** de cada texto nuevo, **0** de los viejos
- AJAX: `true → Producto agregado a tu cotización` · `exists → Este producto ya está en tu cotización`
- `code_error: null`

## ⚠️ Pendiente: la caché tapa el cambio

Un visitante normal recibe `x-litespeed-cache: hit` con páginas de hace días y
**sigue viendo «Explorar la lista»**. El cambio solo se ve forzando render fresco.

Para que llegue hace falta **purgar**, y el 20-ago una purga total dejó el sitio en
**500 varios minutos** ([[verificar-sin-rompe-cache]]). Se le ofrecieron tres
caminos (msg 339) y se recomendó **purgar de madrugada**. **Esperando su decisión.**

## Cabo suelto

El snippet **id 16** («TEMPORAL lector de opciones») quedó **inactivo y con el
código vaciado** — no ejecuta nada y su endpoint da 404. La API devuelve
`rest_cannot_delete` al intentar borrar el registro. Se le pidió a Connie borrarlo
de un clic en el panel.

**Regla que deja:** un snippet de diagnóstico que expone datos por REST **se borra
en el mismo turno en que se usa**, no después.
