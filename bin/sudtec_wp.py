#!/usr/bin/env python3
"""
WordPress + WooCommerce de Sudtec (www.sudtec.cl) — via de acceso desde aqui.

COMO ENTRA: app password sobre Basic auth. Probado el 18/08/2026 con la prueba de
las tres llamadas (clave buena / clave mala / sin clave): las tres respuestas fueron
DISTINTAS (200 / incorrect_password / rest_not_logged_in), o sea este hosting SI le
pasa la cabecera Authorization a PHP. Por eso aqui NO hace falta navegador.

Si algun dia la app password empieza a dar 401, corre `sudtec_wp.py diagnostico`
antes de sospechar de la clave: si las tres llamadas dan lo MISMO, el hosting dejo
de pasar la cabecera y el problema no es la credencial (le paso al sitio de otro
cliente de la casa). Eso se arregla del lado del hosting, o entrando con navegador
y usando cookie + nonce; las dos cosas hay que pedirlas, no improvisarlas.

El usuario es administrator, y la MISMA clave sirve para la API de WooCommerce
(wc/v3): productos, pedidos e informes.

Uso:
  sudtec_wp.py estado                     que hay y si el acceso funciona
  sudtec_wp.py diagnostico                la prueba de las 3 llamadas
  sudtec_wp.py api <ruta>                 GET a cualquier ruta REST
  sudtec_wp.py paginas [--tipo pages]     lista paginas/entradas/productos con id
  sudtec_wp.py ver <id>                   muestra una pagina, entrada o producto
  sudtec_wp.py productos [--buscar texto]
  sudtec_wp.py cotizaciones               los pedidos (la tienda trabaja con YITH)
  sudtec_wp.py escribir <ruta> --datos <archivo.json> --confirmar

Ejemplos:
  sudtec_wp.py api 'wp/v2/posts?per_page=3&_fields=id,title'
  sudtec_wp.py productos --buscar botas
  sudtec_wp.py ver 11201
"""
import argparse
import base64, time
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

VARS = ("WP_SUDTEC_URL_LOGIN", "WP_SUDTEC_USER_LOGIN", "WP_SUDTEC_APP_PASS")


def _cred():
    faltan = [v for v in VARS if not os.environ.get(v)]
    if faltan:
        sys.exit("ERROR: faltan variables en el entorno: " + ", ".join(faltan) +
                 "\n       Las administra Nicolas; no las pidas por chat.")
    login = os.environ["WP_SUDTEC_URL_LOGIN"]
    p = urllib.parse.urlparse(login)
    base = p.scheme + "://" + p.netloc
    return base, os.environ["WP_SUDTEC_USER_LOGIN"], os.environ["WP_SUDTEC_APP_PASS"]


def llamar(ruta, metodo="GET", datos=None, usuario=None, clave=None):
    """Devuelve (status, json_o_texto). ruta sin /wp-json/ al principio."""
    base, u, c = _cred()
    if usuario is not None:
        u = usuario
    if clave is not None:
        c = clave
    url = base + "/wp-json/" + ruta.lstrip("/")
    # LiteSpeed cachea las respuestas REST por URL exacta. El 21-ago-2026 esto hizo
    # que `cotizaciones` (que siempre pide per_page=20) mostrara datos VIEJOS: se
    # comio las 3 cotizaciones mas nuevas, entre ellas dos de esa madrugada.
    # Probado: per_page=20 devolvia la #11602 y per_page=19 la #11609, la real.
    # En las LECTURAS agregamos un parametro unico para forzar respuesta fresca.
    # (Ojo: esto es para leer DATOS por la API. Para verificar como se ve una PAGINA
    # publica sirve lo contrario -> ver memory/verificar-sin-rompe-cache.md)
    if metodo == "GET":
        url += ("&" if "?" in url else "?") + "_nc=%d" % int(time.time() * 1000)
    cuerpo = json.dumps(datos).encode() if datos is not None else None
    req = urllib.request.Request(url, data=cuerpo, method=metodo)
    tok = base64.b64encode((u + ":" + c).encode()).decode()
    req.add_header("Authorization", "Basic " + tok)
    req.add_header("User-Agent", "kai-agente/1.0")
    if cuerpo:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            txt = r.read().decode("utf-8", "replace")
            try:
                return r.status, json.loads(txt)
            except ValueError:
                return r.status, txt[:1500]
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(txt)
        except ValueError:
            return e.code, txt[:1500]
    except urllib.error.URLError as e:
        return 0, "no pude conectar: " + str(e.reason)


def _sin_credencial(ruta):
    base, _, _ = _cred()
    req = urllib.request.Request(base + "/wp-json/" + ruta.lstrip("/"))
    req.add_header("User-Agent", "kai-agente/1.0")
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8", "replace"))
        except ValueError:
            return e.code, None
    except urllib.error.URLError as e:
        return 0, str(e.reason)


def cmd_estado(a):
    base, u, _ = _cred()
    print("Sitio   :", base)
    print("Usuario :", u)
    st, d = llamar("wp/v2/users/me?context=edit")
    if st != 200:
        codigo = d.get("code") if isinstance(d, dict) else d
        print("Acceso  : FALLA (HTTP %s, %s)" % (st, codigo))
        print("          Corre 'diagnostico' antes de dudar de la clave.")
        sys.exit(1)
    caps = d.get("capabilities") or {}
    interesantes = ("manage_options", "edit_posts", "edit_pages", "publish_pages",
                    "upload_files", "activate_plugins", "manage_woocommerce")
    print("Acceso  : OK —", d.get("name"), "(" + ", ".join(d.get("roles") or []) + ")")
    print("Permisos:", ", ".join(k for k in interesantes if caps.get(k)))
    st, info = llamar("")
    if st == 200 and isinstance(info, dict):
        print("Nombre  :", info.get("name"), "|", info.get("description"))


def cmd_diagnostico(a):
    ruta = "wp/v2/users/me"
    print("Prueba de las 3 llamadas a /" + ruta + " — mira si las respuestas DIFIEREN.\n")
    st1, d1 = llamar(ruta)
    st2, d2 = llamar(ruta, clave="xxxx xxxx xxxx xxxx xxxx xxxx")
    st3, d3 = _sin_credencial(ruta)

    def cod(st, d):
        if isinstance(d, dict):
            return str(st) + " " + str(d.get("code") or "(sin code, autenticado)")
        return str(st)

    print("  (a) clave buena :", cod(st1, d1))
    print("  (b) clave mala  :", cod(st2, d2))
    print("  (c) sin clave   :", cod(st3, d3))
    c2 = d2.get("code") if isinstance(d2, dict) else None
    c3 = d3.get("code") if isinstance(d3, dict) else None
    print()
    if st1 == 200:
        print("VEREDICTO: acceso normal por app password. Todo bien.")
    elif c2 == c3:
        print("VEREDICTO: las tres iguales -> el hosting NO pasa la cabecera Authorization.")
        print("           NO es la credencial. No reintentes variantes: avisale a Nicolas.")
    else:
        print("VEREDICTO: la cabecera llega pero la credencial no sirve -> hay que renovar")
        print("           la app password. Avisale a Nicolas.")


def cmd_api(a):
    st, d = llamar(a.ruta)
    print("HTTP", st)
    print(json.dumps(d, ensure_ascii=False, indent=2)[:a.limite])


def cmd_paginas(a):
    tipos = [a.tipo] if a.tipo else ["pages", "posts"]
    for t in tipos:
        st, d = llamar(t + "?per_page=%d&status=any&_fields=id,title,status,link" % a.cuantos
                       if t.startswith("wp/") else
                       "wp/v2/%s?per_page=%d&status=any&_fields=id,title,status,link" % (t, a.cuantos))
        print("\n=== %s (HTTP %s) ===" % (t, st))
        if st != 200 or not isinstance(d, list):
            print("  ", d if not isinstance(d, dict) else d.get("code"))
            continue
        for i in d:
            titulo = (i.get("title") or {}).get("rendered") or ""
            print("  %7s [%-8s] %s" % (i.get("id"), (i.get("status") or "")[:8], titulo[:56]))


def cmd_ver(a):
    for t in ("pages", "posts", "product"):
        st, d = llamar("wp/v2/%s/%s?context=edit" % (t, a.id))
        if st != 200:
            continue
        print("tipo   :", t)
        print("titulo :", (d.get("title") or {}).get("raw", ""))
        print("estado :", d.get("status"), "| enlace:", d.get("link"))
        meta = d.get("meta") or {}
        elementor = any(k.startswith("_elementor") for k in meta)
        if elementor:
            print("\nAVISO: esta pagina esta hecha con ELEMENTOR (_elementor_data en meta).")
            print("       Su contenido real NO es el campo 'content': editar 'content'")
            print("       devuelve 200 y la pagina publica NO cambia. Para cambiarla de")
            print("       verdad hay que usar el editor visual de Elementor.")
        cont = (d.get("content") or {}).get("raw", "")
        print("\n--- content.raw (%d caracteres) ---" % len(cont))
        print(cont[:a.limite] if cont.strip() else "(vacio)")
        return
    print("no encontre nada con id", a.id)


def cmd_productos(a):
    q = "wc/v3/products?per_page=%d&_fields=id,name,sku,price,stock_status,status,permalink" % a.cuantos
    if a.buscar:
        q += "&search=" + urllib.parse.quote(a.buscar)
    st, d = llamar(q)
    print("HTTP", st)
    if st != 200 or not isinstance(d, list):
        print(json.dumps(d, ensure_ascii=False)[:600]); return
    print("%d productos" % len(d))
    for p in d:
        print("  %7s [%-7s] %-46s sku=%-14s %s" % (
            p.get("id"), (p.get("status") or "")[:7], (p.get("name") or "")[:46],
            (p.get("sku") or "")[:14], p.get("price") or "sin precio"))


def cmd_cotizaciones(a):
    st, d = llamar("wc/v3/orders?per_page=%d" % a.cuantos)
    print("HTTP", st)
    if st != 200 or not isinstance(d, list):
        print(json.dumps(d, ensure_ascii=False)[:600])
        return
    print("%d cotizaciones. La tienda usa YITH Request a Quote:" % len(d))
    print("  'billing' viene VACIO y el total es 0 -> eso es NORMAL, no un error.")
    print("  Quien pide vive en meta_data (ywraq_customer_name / ywraq_customer_email),")
    print("  y el formulario completo en _raq_request (incluye rut y telefono).\n")
    for o in d:
        meta = {}
        for m in (o.get("meta_data") or []):
            meta[m.get("key")] = m.get("value")
        quien = meta.get("ywraq_customer_name") or "(sin nombre)"
        correo = meta.get("ywraq_customer_email") or ""
        estado = meta.get("ywraq_raq_status") or o.get("status")
        items = [(li.get("name") or "")[:34] for li in (o.get("line_items") or [])[:3]]
        print("  %7s #%-7s [%-9s] %s" % (o.get("id"), o.get("number"),
                                         str(estado)[:9], str(quien)[:42]))
        if correo:
            print("          %s   %s" % (correo, (o.get("date_created") or "")[:10]))
        if items:
            print("          pide: %s" % ", ".join(items))


def cmd_escribir(a):
    datos = json.loads(open(a.datos, encoding="utf-8").read())
    print("Vas a mandar %s a /%s" % (a.metodo, a.ruta.lstrip("/")))
    print("Cuerpo:", json.dumps(datos, ensure_ascii=False)[:600])
    if not a.confirmar:
        print("\n(no se mando nada: falta --confirmar)")
        print("Recuerda: escribir en el sitio de Constanza se confirma CON ELLA antes.")
        return
    st, d = llamar(a.ruta, a.metodo, datos)
    print("\nHTTP", st)
    print(json.dumps(d, ensure_ascii=False, indent=2)[:1500])
    if st in (200, 201):
        print("\nOK. Revisa la pagina publica antes de avisar que quedo listo:")
        print("una respuesta 200 en Elementor NO garantiza que se vea el cambio.")


def main():
    ap = argparse.ArgumentParser(description="WordPress + WooCommerce de Sudtec")
    comunes = argparse.ArgumentParser(add_help=False)
    comunes.add_argument("--limite", type=int, default=6000)
    comunes.add_argument("--cuantos", type=int, default=20)

    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("estado")
    sub.add_parser("diagnostico")
    x = sub.add_parser("api", parents=[comunes]); x.add_argument("ruta")
    x = sub.add_parser("paginas", parents=[comunes]); x.add_argument("--tipo")
    x = sub.add_parser("ver", parents=[comunes]); x.add_argument("id")
    x = sub.add_parser("productos", parents=[comunes]); x.add_argument("--buscar")
    x = sub.add_parser("cotizaciones", parents=[comunes])
    x = sub.add_parser("escribir", parents=[comunes])
    x.add_argument("ruta"); x.add_argument("--datos", required=True)
    x.add_argument("--metodo", default="POST"); x.add_argument("--confirmar", action="store_true")

    a = ap.parse_args()
    {"estado": cmd_estado, "diagnostico": cmd_diagnostico, "api": cmd_api,
     "paginas": cmd_paginas, "ver": cmd_ver, "productos": cmd_productos,
     "cotizaciones": cmd_cotizaciones, "escribir": cmd_escribir}[a.cmd](a)


if __name__ == "__main__":
    main()
