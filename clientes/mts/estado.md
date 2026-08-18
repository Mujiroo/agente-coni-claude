# MTS — Red de Ferreterías (www.mts.cl)

*Abierto: 18-ago-2026 (msg 59). Pedido de Connie: **contacto del ejecutivo de
retail media / pauta publicitaria, catálogo de medios y tarifario**.*

## Quién es MTS

**Materiales y Soluciones S.A. — «Red MTS»**. No es una cadena: es la **mayor red
de ferreterías independientes de Chile** (fundada 1994, ~46 marcas asociadas,
~130-140 puntos de venta de Arica a Punta Arenas, share ~13% de un mercado de
~US$7.000 millones). Los socios son **dueños de sus ferreterías**; MTS es la
central de compras y el paraguas de marca.

**Consecuencia para el pedido:** el inventario de medios no es de una cadena
propia, sino de una red federada. Lo que MTS vende a proveedores no se parece a
un retail media de supermercado.

## A quién hay que hablarle

Sacado del **propio sitio de MTS** (`/gobierno-corporativo/`), no de directorios
de terceros:

| Persona | Cargo | Por qué importa |
|---|---|---|
| **Natalia Pérez G.** | **Gerente de Marketing** | 🎯 **es la contraparte del pedido**: marketing, ecommerce y puntos de venta |
| **Alejandra Nuñez R.** | Gerente de Negocios | copia natural si la conversación deriva a acuerdo comercial con proveedor |
| Rodrigo Garriga M. | Gerente de Planificación y Compras | manda en la relación con proveedores |
| Jaime Cases L. | Gerente General | — |

⚠️ **Ojo con el dato viejo que circula:** varias notas de prensa y búsquedas
siguen diciendo que el gerente de marketing es **Felipe Salce**. **Está
desactualizado** — el organigrama vigente del sitio dice Natalia Pérez G., y el
LinkedIn de Salce ya no lo muestra en MTS. Si Connie escribe a Salce, quema el
primer contacto.

## Canales de entrada

⚠️ **Ninguno de estos dos salió del sitio de MTS** — vienen de directorios de
terceros, así que hay que darlos por probables, no por confirmados. Barrí las 73
páginas y las 50 entradas del sitio: **los únicos correos y teléfonos publicados
son los de las ferreterías socias**, no los de la central.

- **Correo general:** `contacto@mts.cl` *(sin verificar)*
- **Teléfono:** **+56 2 2390 5100** (también aparece 2390 5000) *(sin verificar)*
- **Lo más seguro es el formulario del sitio**, que sí es de la central.
- **Dirección:** General Velásquez 7137, Cerrillos, Santiago
- **Formularios:** `mts.cl/contactenos/` y `mts.cl/quiero-ser-proveedor/`
- LinkedIn empresa: `cl.linkedin.com/company/mtschile` (11,2 mil seguidores)

## Catálogo de medios y tarifario: no existe público

Verificado, no supuesto: barrí el contenido completo del sitio (73 páginas + 50
entradas) buscando *retail media*, *tarifario*, *media kit*, *pauta* y
*publicidad*. **Cero coincidencias de las cinco.** MTS no publica media kit ni
tarifario, y ni siquiera nombra el concepto. Tampoco aparece una unidad
de *retail media* formalizada (no está entre los players que sí lo tienen en
Chile: Cencosud Media, Walmart Connect, Sodimac Media, Mercado Ads, Unimedios).

**Lo que sí tienen como vitrina para proveedores:**

- **Ruedas de Negocios** — el evento donde socios y proveedores cierran acuerdos
  (2-3 al año, Espacio Riesco; ~48 socios y ~50 proveedores por versión).
- **RedEncuentros 2026** — **18 al 20 de agosto de 2026, Valdivia**, sobre
  transformación digital y sucesión de los socios. *Es esta misma semana: el
  equipo de marketing probablemente está allá, así que una respuesta puede
  demorar unos días — o ser el mejor gancho para escribir.*
- **Tiendas Digitales MTS** (`/mtsecommerce/`) — su ecommerce por ferretería, que
  es el inventario digital más obvio si quieren vender pauta.
- **Capacitación Marketing Digital MTS** — le hacen marketing a sus socios.

**Conclusión honesta:** el tarifario hay que **pedirlo**, no encontrarlo. Y es
probable que no exista como PDF: que sea una negociación caso a caso con
marketing.

## Nota técnica (para no repetir el tropiezo)

`www.mts.cl` está **detrás de Cloudflare y devuelve 403** a curl y a WebFetch.
Pero su **WordPress deja abierta la API REST**:
`https://www.mts.cl/wp-json/wp/v2/pages?per_page=100` responde 200 y por ahí se
lee el contenido de cualquier página. Así se sacó el organigrama.

## Estado

🟡 **Investigación lista. Falta que Connie apruebe y envíe el correo.** El texto
propuesto está redactado para que lo mande ella — no se envía nada desde acá.
