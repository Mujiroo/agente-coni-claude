# BORRADOR — Freno a bots en URLs de filtro YITH (NO instalado, esperando OK de Connie, msg 1195)

## Snippet (Code Snippets, scope global, prioridad 1)

```php
<?php
// KAI · Freno a bots en URLs de filtro (15-sep-2026) — BORRAR ESTE PARA REVERTIR
add_action( 'init', function () {
	if ( is_admin() || wp_doing_ajax() || wp_doing_cron() || ( defined( 'REST_REQUEST' ) && REST_REQUEST ) ) return;
	if ( 'GET' !== ( $_SERVER['REQUEST_METHOD'] ?? '' ) ) return;
	if ( isset( $_GET['wc-ajax'] ) ) return;
	if ( is_user_logged_in() ) return;

	$claves = array_keys( $_GET );
	$filtros = array_filter( $claves, function ( $k ) {
		return $k === 'yith_wcan' || $k === 'product_cat' || $k === 'min_price' || $k === 'max_price'
			|| strpos( $k, 'filter_' ) === 0 || strpos( $k, 'query_type_' ) === 0;
	} );
	if ( ! $filtros ) return;

	$ref       = $_SERVER['HTTP_REFERER'] ?? '';
	$interno   = (bool) preg_match( '#^https?://(www\.)?sudtec\.cl/#i', $ref );
	$reales    = array_diff( $filtros, array( 'yith_wcan' ) );
	$demasiado = count( $reales ) > 2;

	if ( $interno && ! $demasiado ) {
		add_filter( 'rank_math/frontend/robots', function ( $r ) { $r['index'] = 'noindex'; $r['follow'] = 'nofollow'; return $r; } );
		return;
	}
	nocache_headers();
	header( 'X-Robots-Tag: noindex, nofollow', true );
	$limpia = strtok( $_SERVER['REQUEST_URI'] ?? '/', '?' );
	wp_safe_redirect( home_url( $limpia ), 302 );
	exit;
}, 0 );
```

Notas:
- `init` prio 0: WP y plugins ya cargaron, pero **antes** de la consulta principal de WooCommerce/Elementor (lo caro).
- Filtro por AJAX (`wc-ajax=yith_wcan_render_filter`) no se toca → la tienda sigue filtrando para humanos.
- Antes de instalar: probar con `validate`/snippet inactivo, activar, y verificar: (1) home y categoría 200; (2) URL de filtro sin referer → 302; (3) con referer interno → 200 + noindex; (4) filtrar desde el navegador sigue funcionando.
- LiteSpeed puede cachear el 302 por URL: `nocache_headers()` lo evita.

## .htaccess (lo pega Connie, ANTES del bloque de WordPress)

```apache
# KAI · freno a bots en filtros (15-sep-2026)
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{QUERY_STRING} (^|&)(yith_wcan|product_cat|filter_[a-z0-9_-]+|min_price|max_price)= [NC]
RewriteCond %{QUERY_STRING} !(^|&)wc-ajax= [NC]
RewriteCond %{HTTP_COOKIE} !wordpress_logged_in_ [NC]
RewriteCond %{HTTP_REFERER} !^https?://(www\.)?sudtec\.cl/ [NC]
RewriteRule ^(.*)$ /$1? [R=302,L]
</IfModule>
```

(Falta la regla de «más de 2 filtros» en htaccess; se puede agregar con un `RewriteCond` que cuente 3 `filter_`.)
