---
name: instagram-publicar-ruta-drive
description: Cómo publicar en Instagram una foto que llega por Telegram — el API no acepta archivos locales, hay que pasar por una URL pública de Drive.
metadata:
  type: reference
---

# Publicar en Instagram una foto local (ruta verificada 30-ago-2026)

**El problema:** el API de Instagram **no acepta archivos locales**. Y el campo
`image_file` de `INSTAGRAM_POST_IG_USER_MEDIA` **tampoco sirve** para un archivo del
contenedor: exige un objeto `{name, mimetype, s3key}`, y el `s3key` solo lo devuelve
una descarga previa hecha *dentro* de Composio. Pasarle la ruta local falla con
`Input should be a valid dictionary or instance of FileUploadable`.

**La ruta que sí funciona** — subir a Drive por Maton, hacerlo público, dárselo a
Instagram como `image_url`, y borrarlo:

```bash
# 1. subir (OJO: la ruta lleva /upload/ ANTES de /drive/v3/)
bash bin/maton.sh 'google-drive/upload/drive/v3/files?uploadType=media' \
  -X POST -H 'Content-Type: image/jpeg' --data-binary @incoming/file_55.jpg

# 2. hacerlo visible con enlace
bash bin/maton.sh 'google-drive/drive/v3/files/<ID>/permissions' \
  -X POST -H 'Content-Type: application/json' -d '{"role":"reader","type":"anyone"}'

# 3. la URL directa que Meta sí sabe leer:
#    https://lh3.googleusercontent.com/d/<ID>
# 4. contenedor -> publicar -> y AL FINAL borrar el archivo:
bash bin/maton.sh 'google-drive/drive/v3/files/<ID>' -X DELETE     # da 204
```

**Verificar antes de publicar**, con `curl -o /dev/null -w '%{content_type} %{size_download}'`:
la URL tiene que devolver `image/jpeg` y **el mismo tamaño en bytes** que el archivo
local. `lh3.googleusercontent.com/d/<ID>` sirve el JPEG directo; el clásico
`drive.google.com/uc?export=download` también funcionó, pero el primero es más limpio
porque no redirige.

**Borrar el temporal es seguro:** Instagram se queda con **su propia copia** en
`cdninstagram.com` desde que se crea el contenedor. Se comprobó pidiendo `media_url`
*después* de borrar el archivo de Drive: el post seguía entero. Dejar el archivo público
en el Drive de Connie sería el descuido real.

## Dos cosas del caption

- El schema de Composio dice «usa `%23` para el `#`». **Es falso para este camino y es
  una trampa fea:** si no lo decodifican, en el post público aparece `%23汉服`. Se mandó
  el `#` **crudo** y llegó perfecto, hashtags chinos incluidos. El `#` crudo, si algo
  falla, solo pierde los hashtags; el `%23` deja un error visible bajo su nombre.
- **Siempre releer el post con `INSTAGRAM_GET_IG_MEDIA` (`fields=caption,permalink`)
  después de publicar.** Es la única forma de saber qué quedó de verdad, y de ahí sale
  el enlace para mandárselo.

**Datos fijos de la cuenta:** `connie_pfeifer`, BUSINESS, `ig_user_id`
**27795064996852941**. No hay herramienta para **borrar** un post ni para **comentar**:
si el caption sale mal, se arregla desde la app.

**Se le suma `alt_text`** (máx. 1000 car.) describiendo la foto: es accesibilidad y
además ayuda al alcance. Va en el contenedor, no en el publish.

Relacionado: [[notas-connie]], [[canal-y-formato]]

## La música NO se puede poner desde acá (verificado 30-ago-2026)

Connie reclamó «le faltó música» al post de 芙蓉镇. **No hay forma por API.** Se buscó
con `COMPOSIO_SEARCH_TOOLS` (`search_strategy: tool_search`) por música/audio y por
editar/borrar: **no existe herramienta para ninguna de las tres cosas**. Lo único
audio-adyacente es `audio_name` en Reels, que solo **nombra** el audio original — no
adjunta una canción del catálogo.

O sea: **la música, editar un post y borrarlo son todos «desde la app»**. Conviene
decírselo *antes* de publicar si la foto es de las que ella suele musicalizar.

**Dato que le sirve y no es obvio:** su cuenta es **BUSINESS**, así que Instagram le
muestra solo el **catálogo de uso comercial** — muchas canciones conocidas no aparecen
y parece un error de ella. El truco: **buscar por instrumento, no por canción**
(`guzheng`, `erhu`, `bamboo flute`, `chinese traditional`).
