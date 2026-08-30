---
name: editar-fotos
description: Sí puedo editar fotos — Pillow va desempaquetado a mano en vendor/ y el editor es bin/editar_foto.py; qué puedo y qué no.
metadata:
  type: reference
---

# Editar fotos (montado el 30-ago-2026, msg 584)

Connie preguntó «¿puedes editar fotos?». La respuesta salió **sí**, pero no venía
gratis: **el contenedor no trae ninguna librería de imagen**.

## Cómo quedó montado (y cómo rehacerlo si desaparece)

La escalera de intentos, para no repetirla: `PIL`, `numpy`, `cv2` → no están ·
`pip`, `pip3`, `ensurepip` → **no existen** · `convert`/`magick`/`ffmpeg` → tampoco ·
`apt-get` existe pero **soy uid 1000, sin sudo y sin escritura en `/usr/lib`**.

**Lo que sí funcionó:** bajar la rueda de PyPI y **descomprimirla a mano**, que no
necesita permisos porque una `.whl` es un zip con los `.so` adentro:

```bash
curl -sSL -o /tmp/p.whl "<url del wheel cp311 manylinux x86_64 de pillow>"
python3 -c "import zipfile; zipfile.ZipFile('/tmp/p.whl').extractall('/home/agent/workspace/vendor')"
```

La URL sale de `https://pypi.org/pypi/pillow/json`, filtrando por `cp311` +
`manylinux` + `x86_64` (el contenedor es **Python 3.11 / x86_64**; si cambia, cambia
la rueda). Quedó **Pillow 12.3.0** en `vendor/`, que está en `.gitignore` — son
binarios, no van al repo. `bin/editar_foto.py` se agrega solo el `sys.path`, así que
no hace falta exportar `PYTHONPATH`.

**Si un día `import PIL` falla, no es un bug: es que `vendor/` se perdió.** Se rehace
con los dos comandos de arriba en un minuto.

## La herramienta

`bin/editar_foto.py` — niveles (punto negro/blanco, gamma), contraste, saturación,
brillo, nitidez, canal por canal, redimensionar, calidad.

```bash
python3 bin/editar_foto.py entrada.jpg salida.jpg --preset guofeng
python3 bin/editar_foto.py e.jpg s.jpg --contraste 1.2 --saturacion 1.15 --negros 12
```

**Preset `guofeng`** — es el que le gustó a ella, y codifica lo aprendido comparando
sus dos ediciones ([[notas-connie]]): lo que hace que una foto se lea china **no es un
filtro sobre la piel, es el fondo**. Sube el punto negro a 14 (los filtros tipo «film»
dejan el negro en 20-30 y por eso se ven lavados), sube contraste y saturación, empuja
**el canal verde aparte** para no naranjear la piel, y baja el rojo **solo en las
sombras** para sacar el velo beige sin enfriar la cara.

## Mandarle la imagen: `tg.sh` no sabía

Se le agregaron dos subcomandos, y **la diferencia importa**:

- `bash bin/tg.sh foto <archivo> '<caption>'` → `sendPhoto`. Telegram **recomprime**.
- `bash bin/tg.sh archivo <archivo> '<caption>'` → `sendDocument`. Llega el JPEG
  **exacto**. **Este es el que va cuando ella va a resubir la imagen** (Instagram).

## Qué NO puedo, y hay que decirlo sin rodeos

Nada **generativo**: borrar una persona del fondo, agregar lo que no estaba, cambiar
caras o cuerpos, extender el fondo, o un «upscale» con IA. No hay modelo de imagen
conectado. Pillow mueve píxeles existentes, no los inventa.

**Lo que sí vale como diferencia y conviene decirle:** *veo* el resultado. Aplico,
abro la imagen, la juzgo y corrijo. No es mandar números a ciegas.

## Dos cosas del camino

- **El bug del caption vacío, que diagnostiqué mal dos veces.** `tg.sh foto` devolvía
  un JSON vacío y la llamada cruda con `caption=prueba` funcionaba, así que lo di por
  **fallo pasajero de red**. No lo era, y volvió a pasar con `archivo`.

  **La causa real:** en `curl`, un valor de `-F` que empieza con `<` (o `@`) significa
  *«lee el contenido de este archivo»*. Todos mis captions empiezan con `<b>`, así que
  curl buscaba un archivo llamado `b>Texto...`, no lo encontraba y devolvía **vacío**.
  Por eso «prueba» funcionaba y `<b>prueba</b>` no. **La solución es `--form-string`**,
  que nunca interpreta el valor.

  **La lección que vale más que el bug:** la prueba que hice para descartar el script
  —la llamada cruda— usaba un caption **sin tags**, o sea no reproducía el caso que
  fallaba. Una prueba que cambia dos cosas a la vez no descarta nada. Y «fallo
  pasajero» es la explicación más cómoda y la que hay que sospechar primero: si el
  fallo se repite, nunca fue pasajero.
- **Nunca depurar `tg.sh` con `bash -x`:** el trace imprime el **token del bot** en
  claro. Se usa un `echo` puntual del comando, no el trace completo.

Relacionado: [[instagram-publicar-ruta-drive]], [[notas-connie]], [[canal-y-formato]]

## Segundo encargo, mismo día: la foto del 土王行宫 (msg 589)

Mandó una foto suya con 帷帽 frente al templo, de día nublado. **No se le aplicó el
preset `guofeng`**, y ese fue el punto: ese preset hunde los negros, y en luz plana de
nublado eso habría tapado todas las sombras. **El preset se elige por el problema de la
foto, no por el estilo que uno quiere.**

Ajuste usado: `--negros 8 --contraste 1.16 --saturacion 1.24 --nitidez 1.2 --verde 1.02
--rojo-sombras 1.07 --gamma 0.98`. El `rojo-sombras` sobre 1 **calienta la madera y los
faroles sin enrojecerle la cara**, porque el efecto se apaga hacia las luces.

**El cielo estaba quemado a blanco puro y no se recupera** — se le dijo derecho, y
además que en este estilo juega a favor: se lee como papel de arroz.

**Se le agregó recorte al editor** (`--aspecto 4:5 --sesgo 0.3`) y se le mandaron **dos
versiones**: completa y recortada. La 4:5 es la que más pantalla ocupa en el feed de
Instagram; sacándole el suelo vacío de abajo ella queda más grande y las sillas
distraen menos. **Se recomendó una de las dos**, no se le dejó la decisión entera.
