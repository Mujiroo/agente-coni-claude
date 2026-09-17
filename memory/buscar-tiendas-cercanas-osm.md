---
name: buscar-tiendas-cercanas-osm
description: Para «¿dónde hay un X cerca?» en China, la web no sirve; Overpass (OpenStreetMap) sí responde desde el contenedor y da distancias, pero con cobertura incompleta.
metadata:
  type: reference
---

**Probado el 13-sep-2026** (Connie pidió un Lawson cerca del hotel en Pekín, msg 1131).

Buscar en la web «罗森 东单» no devolvió nada útil: los directorios chinos no se dejan
consultar. Lo que **sí funcionó** fue OpenStreetMap:

1. Coordenadas de la calle: `nominatim.openstreetmap.org/search?q=<calle en chino>&format=json`
   (con `User-Agent`). **Geocodificar la calle, no adivinar**: la primera vez centré la búsqueda
   a ojo y quedé ~700 m corrido.
2. Tiendas alrededor: `overpass-api.de/api/interpreter` con
   `node(around:900,LAT,LON)[shop~"convenience|supermarket"]` y `name~"罗森"` en un radio mayor.
   **`overpass.kumi.systems` no respondió** — usar `overpass-api.de`.

**Límite, y hay que decírselo:** en China muchas tiendas en OSM **no tienen nombre** o
**no están cargadas**. Sirve para «hay un FamilyMart en tu calle», no para afirmar que no
existe algo más cerca. Cerrar siempre con: **búscalo en Amap** (ella usa Amap), que ordena
por distancia desde donde está.

**Para mandarle un punto en Amap hay que convertir coordenadas.** OSM está en **WGS84** y
Amap en **GCJ-02**: en Pekín la diferencia es de ~500 m (lon −0,006 / lat −0,0014). Convertir
con la fórmula estándar WGS→GCJ y armar el link
`https://uri.amap.com/marker?position=LON,LAT&name=...&coordinate=gaode`. (Usado el 13-sep
con el FamilyMart de `大纱帽胡同`, msg 1134.)

**En China la tienda suele estar DENTRO de un mall, y eso hay que decirlo.** El
17-sep-2026 le pasé un `小米之家` como si estuviera en `帅府园胡同` y ella preguntó si
no era un mall (msg 1278): **sí lo era**. Quedarse con el nombre de la calle la deja
buscando una puerta que no existe.

**Se resuelve con `is_in`, que es exacto y barato:**

    [out:json];is_in(LAT,LON);out tags;

Devuelve todas las áreas que contienen el punto. Si aparece una con `shop=mall`, la
tienda está adentro: hay que dar **el nombre del mall**, no el de la calle. En ese caso
salió `北京apm`. Un `node(around:150,...)` sirve además para nombrar tiendas vecinas
conocidas (Victoria's Secret, Miniso) y que ella ubique el edificio de lejos.

**Ojo con Overpass:** responde **406 Not Acceptable** sin `User-Agent`, igual que
Nominatim. Costó una llamada perdida.

**Y el reverse geocoding antes de decir «en tu calle»:** dije que el FamilyMart estaba en
`东单三条` y en realidad estaba en el hutong de al lado. Hubo que corregirlo en el mensaje siguiente.

Relacionado: [[pekin-connie]], [[direccion-china-por-pinyin]]
