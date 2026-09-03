#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saca el texto de un PDF sin depender de nada externo.

POR QUE EXISTE: el 2-sep-2026 Connie mando la cartola de su Visa en PDF y en el
contenedor NO hay pdftotext, ni poppler, ni pypdf, ni pip, ni root para apt-get.
La herramienta Read tampoco puede: pide pdftoppm para rasterizar. Esto lo resuelve
con la libreria estandar (re + zlib), que siempre esta.

QUE HACE: descomprime los streams FlateDecode y junta el texto de los operadores
Tj / TJ / ' / ", cortando linea en Td/TD/Tm/T*. Suficiente para cartolas, boletas y
facturas, que son PDF de texto.

QUE NO HACE: OCR. Si el PDF es un escaneo (puro imagen), esto devuelve poco o nada
-y ahi la respuesta honesta es pedirle una foto legible o el detalle a mano-.
Tampoco resuelve fuentes con CMap raro; si sale ilegible, revisar eso.

USO:  python3 bin/pdf_texto.py archivo.pdf
      python3 bin/pdf_texto.py archivo.pdf | head -80

OJO: la basura binaria de las imagenes incrustadas aparece al final. Cortar por el
primer bloque ilegible antes de parsear (en la cartola el corte fue "Capa 1Arial").
Ver memory/leer-pdf-sin-herramientas.md
"""
import re, zlib, sys

def streams(data):
    out=[]
    for m in re.finditer(rb'stream\r?\n', data):
        ini=m.end()
        fin=data.find(b'endstream', ini)
        if fin<0: continue
        raw=data[ini:fin]
        # el diccionario del objeto viene justo antes
        head=data[max(0,m.start()-400):m.start()]
        if b'FlateDecode' in head:
            try: raw=zlib.decompress(raw)
            except Exception:
                try: raw=zlib.decompressobj().decompress(raw)
                except Exception: continue
        out.append(raw)
    return out

def unescape(s):
    r=b''; i=0
    while i<len(s):
        c=s[i:i+1]
        if c==b'\\' and i+1<len(s):
            n=s[i+1:i+2]
            mp={b'n':b'\n',b'r':b'\r',b't':b'\t',b'b':b'\b',b'f':b'\f',
                b'(':b'(',b')':b')',b'\\':b'\\'}
            if n in mp: r+=mp[n]; i+=2; continue
            if n.isdigit():
                j=i+1; o=b''
                while j<len(s) and len(o)<3 and s[j:j+1].isdigit(): o+=s[j:j+1]; j+=1
                r+=bytes([int(o,8)&0xFF]); i=j; continue
            r+=n; i+=2; continue
        r+=c; i+=1
    return r

def text(content):
    lines=[]; cur=[]
    # operadores: (str)Tj  [..]TJ  (str)'  Td/TD/T*/Tm mueven linea
    tok=re.compile(rb"\((?:[^()\\]|\\.|\([^()]*\))*\)|<[0-9A-Fa-f\s]+>|"
                   rb"(?:TJ|Tj|T\*|Td|TD|Tm|'|\")", re.S)
    for m in tok.finditer(content):
        t=m.group(0)
        if t.startswith(b'('):
            cur.append(unescape(t[1:-1]).decode('latin-1'))
        elif t.startswith(b'<') and not t.startswith(b'<<'):
            h=re.sub(rb'\s',b'',t[1:-1])
            try:
                b=bytes.fromhex(h.decode())
                # heuristica: UTF-16BE si hay muchos ceros alternados
                if len(b)>=2 and b[0::2].count(0)>len(b)//4:
                    cur.append(b.decode('utf-16-be','replace'))
                else:
                    cur.append(b.decode('latin-1'))
            except Exception: pass
        elif t in (b'Td',b'TD',b'T*',b'Tm',b"'",b'"'):
            if cur: lines.append(''.join(cur)); cur=[]
    if cur: lines.append(''.join(cur))
    return lines

data=open(sys.argv[1],'rb').read()
alll=[]
for st in streams(data):
    if b'Tj' in st or b'TJ' in st:
        alll+=text(st)
print("\n".join(l for l in alll if l.strip()))
