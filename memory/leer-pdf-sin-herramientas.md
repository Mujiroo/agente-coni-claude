---
name: leer-pdf-sin-herramientas
description: En este contenedor no hay pdftotext ni pip ni root; los PDF se leen con bin/pdf_texto.py, escrito con la librería estándar.
metadata:
  type: reference
---

**El 2-sep-2026 Connie mandó la cartola de su Visa en PDF** y no había con qué
abrirla. Lo que se probó, en orden, y falló todo:

| Intento | Resultado |
|---|---|
| herramienta `Read` sobre el PDF | pide **pdftoppm** para rasterizar — no está |
| `pdftotext`, `pdftoppm`, `mutool`, `gs`, `qpdf` | ninguno instalado |
| `pypdf`, `PyPDF2`, `fitz`, `pdfplumber` | ningún módulo |
| `pip3` / `python3 -m pip` | **no hay pip en la imagen** |
| `apt-get install poppler-utils` | **no soy root** (`dpkg lock: Permission denied`) |

**La salida fue escribir el extractor:** `bin/pdf_texto.py`, con `re` + `zlib` de la
librería estándar. Descomprime los streams `FlateDecode` y arma el texto desde los
operadores `Tj` / `TJ` / `'` / `"`, cortando línea en `Td`/`TD`/`Tm`/`T*`.

    python3 bin/pdf_texto.py incoming/archivo.pdf

**Funcionó a la primera** con la cartola del banco.

## Tres cosas para la próxima

1. **La basura binaria de las imágenes incrustadas sale mezclada al final.** Hay que
   cortar el texto en el primer bloque ilegible antes de parsear — en la cartola el
   corte limpio fue la marca `Capa 1Arial`.
2. **No hace OCR.** Si el PDF es un escaneo, esto devuelve poco o nada. Ahí la
   respuesta honesta es pedirle una foto legible o los datos a mano, no inventar.
3. **La otra vía, si algún día hace falta una librería de verdad:** existe el
   precedente de **desempaquetar un wheel a mano en `vendor/`** (así está Pillow, ver
   [[editar-fotos]]). Es más trabajo; el extractor propio ya cubre cartolas, boletas
   y facturas, que son PDF de texto.

## La regla que vale más que el script

**Cuando el PDF trae plata, cuadrar el parseo contra un total que el propio documento
declare, y decírselo a Connie.** En la cartola los 26 movimientos sumaron **290,42
USD**, y `290,42 − 2,98` (el movimiento del día, aún no aplicado) dio **287,44**, que
es exactamente el «cupo utilizado» impreso; y `3.000 − 287,44 = 2.712,56`, el
disponible impreso. **Dos controles exactos = no se me quedó ninguna fila afuera.**
Sin esa cuadratura, un parser casero que se salta una línea da un número plausible y
equivocado — el mismo peligro de [[contadores-no-son-envios]].

**Nada de esto se commitea:** `incoming/` está en `.gitignore`, y ahí viven las
cartolas, el RUT y todo lo que ella manda. Verificado con `git check-ignore` antes de
commitear.
