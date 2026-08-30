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

- El primer `tg.sh foto` **falló con un JSON vacío** (curl no devolvió nada). No era
  el script: la llamada cruda idéntica funcionó al tiro. **Fue un fallo pasajero de
  red.** Antes de reescribir un script que parece roto, repetir la llamada.
- **Nunca depurar `tg.sh` con `bash -x`:** el trace imprime el **token del bot** en
  claro. Se usa un `echo` puntual del comando, no el trace completo.

Relacionado: [[instagram-publicar-ruta-drive]], [[notas-connie]], [[canal-y-formato]]
