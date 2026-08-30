#!/usr/bin/env python3
"""Editor de fotos del agente.

Pillow no viene en la imagen del contenedor y aca no hay root ni pip, asi que la
rueda vive desempaquetada en vendor/ (ver memory/editar-fotos.md). Por eso el
sys.path de abajo: sin el, el import falla aunque el paquete este bajado.

  python3 bin/editar_foto.py entrada.jpg salida.jpg --preset guofeng
  python3 bin/editar_foto.py e.jpg s.jpg --contraste 1.2 --saturacion 1.15 --negros 12
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "vendor"))

from PIL import Image, ImageEnhance  # noqa: E402


def lut_niveles(negros=0, blancos=255, gamma=1.0):
    """Curva de niveles clasica: recorta el punto negro/blanco y aplica gamma.

    Subir `negros` es lo que saca el velo lechoso de los filtros tipo 'film':
    esos dejan el negro mas oscuro en 20-30 en vez de 0, y la foto se ve lavada.
    """
    tabla = []
    rango = max(1, blancos - negros)
    for i in range(256):
        v = (i - negros) / rango
        v = min(1.0, max(0.0, v))
        v = v ** (1.0 / gamma) if gamma != 1.0 else v
        tabla.append(int(round(v * 255)))
    return tabla


def aplicar_por_canal(im, lr, lg, lb):
    r, g, b = im.split()
    return Image.merge("RGB", (r.point(lr), g.point(lg), b.point(lb)))


PRESETS = {
    # Lo que hace que una foto se lea "china" no es un filtro sobre la piel:
    # es el FONDO. El verde mineral oscuro de la pintura sobre seda, con la
    # figura clara brillando encima. Por eso el preset hunde negros y satura,
    # en vez de suavizar.
    "guofeng": dict(negros=14, gamma=0.97, contraste=1.18, saturacion=1.22,
                    nitidez=1.15, verde=1.04, rojo_sombras=0.94),
    # Al reves: aclara y suaviza, para una foto con sol duro o contraluz.
    "suave": dict(negros=0, gamma=1.12, contraste=0.95, saturacion=1.05,
                  nitidez=1.0, verde=1.0, rojo_sombras=1.0),
}


def editar(entrada, salida, negros=0, blancos=255, gamma=1.0, contraste=1.0,
           saturacion=1.0, brillo=1.0, nitidez=1.0, verde=1.0, rojo_sombras=1.0,
           ancho=None, calidad=95):
    im = Image.open(entrada)
    im = im.convert("RGB")

    base = lut_niveles(negros, blancos, gamma)
    # El verde se empuja aparte del resto: subir la saturacion global tambien
    # satura la piel, y eso la deja naranja. Tocar el canal verde mueve el
    # follaje sin arrastrar la cara.
    lut_g = [min(255, int(round(v * verde))) for v in base]
    # Bajar el rojo SOLO en las sombras es lo que quita el tinte beige del
    # fondo sin enfriar la piel, que vive en los medios y altos.
    lut_r = [int(round(v * (rojo_sombras + (1 - rojo_sombras) * (i / 255.0))))
             for i, v in enumerate(base)]
    im = aplicar_por_canal(im, lut_r, lut_g, base)

    for clase, factor in ((ImageEnhance.Brightness, brillo),
                          (ImageEnhance.Contrast, contraste),
                          (ImageEnhance.Color, saturacion),
                          (ImageEnhance.Sharpness, nitidez)):
        if factor != 1.0:
            im = clase(im).enhance(factor)

    if ancho and im.width > ancho:
        alto = round(im.height * ancho / im.width)
        im = im.resize((ancho, alto), Image.LANCZOS)

    im.save(salida, "JPEG", quality=calidad, subsampling=0, optimize=True)
    return salida, im.size


def main():
    p = argparse.ArgumentParser(description="Edita una foto (niveles, color, nitidez).")
    p.add_argument("entrada")
    p.add_argument("salida")
    p.add_argument("--preset", choices=sorted(PRESETS))
    for nombre, defecto in (("negros", 0), ("blancos", 255)):
        p.add_argument("--" + nombre, type=int, default=defecto)
    for nombre in ("gamma", "contraste", "saturacion", "brillo", "nitidez",
                   "verde", "rojo-sombras"):
        p.add_argument("--" + nombre, type=float, default=1.0)
    p.add_argument("--ancho", type=int)
    p.add_argument("--calidad", type=int, default=95)
    a = p.parse_args()

    kw = dict(negros=a.negros, blancos=a.blancos, gamma=a.gamma,
              contraste=a.contraste, saturacion=a.saturacion, brillo=a.brillo,
              nitidez=a.nitidez, verde=a.verde, rojo_sombras=a.rojo_sombras)
    if a.preset:
        # El preset es la base; cualquier flag que el usuario haya movido a mano
        # manda por sobre el.
        base = dict(PRESETS[a.preset])
        for k, v in kw.items():
            if v not in (1.0, 0, 255):
                base[k] = v
        kw = base
    kw.update(ancho=a.ancho, calidad=a.calidad)

    ruta, tam = editar(a.entrada, a.salida, **kw)
    print(f"OK {ruta} {tam[0]}x{tam[1]} {os.path.getsize(ruta)} bytes")


if __name__ == "__main__":
    main()
