---
name: verificar-sin-rompe-cache
description: Un cambio de front no está verificado hasta verlo en la URL limpia; el rompe-caché prueba que el código corre, no lo que ve el visitante.
metadata:
  type: feedback
---

**20-ago-2026, Sudtec.** Apliqué dos cambios de front (estilos de grilla y bloque
de navegación), los verifiqué con `?cb=<random>` para saltar la caché de LiteSpeed,
y le dije a Connie que estaban listos. **No los veía nadie.** Ella lo detectó:
*«no se ve en el mobile y en botas tampoco»*.

**El error:** el rompe-caché fuerza un MISS y regenera la página. Eso prueba que el
código **corre**, pero deja intacta la copia cacheada de la **URL limpia**, que es
la que reciben los visitantes. Verifiqué la versión que nadie mira.

**La regla:**

1. Se usa `?cb=` **para diagnosticar** (ver si el código produce lo esperado).
2. **La verificación de verdad es la URL limpia**, sin parámetros, mirando
   `x-litespeed-cache`. Si dice `hit` y no trae el cambio, **no está entregado**.
3. Y hay que verlo en **PC y en móvil por separado**: LiteSpeed guarda copias
   distintas por tipo de dispositivo.

**Síntoma que delata esto:** unas páginas muestran el cambio y otras no, sin patrón
lógico. No es el código — es la **antigüedad de la copia cacheada** de cada URL.

## Cómo purgar la caché en Sudtec

La API REST de LiteSpeed (`litespeed/v1`, `litespeed/v3`) **no expone purga**: sus
rutas son callbacks de su servicio en la nube.

Lo que **no funcionó** desde un snippet de Code Snippets (`single-use`):

- `do_action( 'litespeed_purge_url', $url )` por cada categoría
- `do_action( 'litespeed_purge_all' )`

Lo que **sí funcionó**:

```php
if ( class_exists( '\LiteSpeed\Purge' ) && method_exists( '\LiteSpeed\Purge', 'purge_all' ) ) {
	\LiteSpeed\Purge::purge_all( 'motivo' );
}
if ( ! headers_sent() ) {
	@header( 'X-LiteSpeed-Purge: *' );
}
```

En un snippet con scope `single-use`: se ejecuta una vez y queda inactivo solo.

**Ojo con el borrado de snippets:** `POST .../snippets/<id>?_method=DELETE` devuelve
**204 pero no borra**, y actualizar el campo `name` tampoco surtió efecto. Sí
funciona actualizar `code`. Los snippets gastados hay que borrarlos a mano desde el
panel.

Relacionado: [[bloqueo-bots-htaccess-sudtec]], [[ads-403-robot-vs-navegador]]
