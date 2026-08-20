---
name: herramientas-keywords-seo
description: Qué hay disponible para datos de keywords SEO (dificultad, orgánico) más allá del Planificador de Google, y qué bloquea cada opción.
metadata:
  type: reference
---

**Connie preguntó el 20-ago-2026 (msg 248)** dónde generar datos de keywords **para
SEO**, explícitamente **sin** el Planificador de Google. Su objeción es correcta:
**el Planificador da métricas de publicidad** (volumen, competencia *de
anunciantes*, CPC) y **no tiene dificultad de keyword ni competencia orgánica**.

Ella paga **Semrush Guru**, y el acceso a la API requiere **Business**.

## Lo que hay

### 1. Semrush — conectado el 20-ago-2026, pero la clave NO funciona

Toolkit `semrush`, cuenta `semrush_expone-lei`, que Composio reporta **«active»**. Herramientas disponibles:

| Tool | Para qué |
|---|---|
| `SEMRUSH_KEYWORD_OVERVIEW_ONE_DATABASE` | volumen (Nq), **dificultad (Kd)**, intención (In), tendencia (Td) |
| `SEMRUSH_KEYWORD_DIFFICULTY` | solo Kd |
| `SEMRUSH_BATCH_KEYWORD_OVERVIEW` | hasta **100 keywords** por llamada |
| `SEMRUSH_PHRASE_QUESTIONS` | keywords de pregunta |
| `SEMRUSH_DOMAIN_ORGANIC_SEARCH_KEYWORDS` | qué rankea un dominio, con posición |
| `SEMRUSH_COMPETITORS_IN_ORGANIC_SEARCH` | competidores orgánicos |
| `SEMRUSH_DOMAIN_VS_DOMAIN` | keyword gap entre hasta 5 dominios |

Bases regionales incluyen **`co` (Colombia)**, **`cl` (Chile)**, `mx`, `pe`, `ec`,
`gt` — o sea, **los seis mercados de Connie**.

⚠️ **Estado real al 20-ago-2026 15:10: NO funciona.** Connie conectó una clave
(msg 253) y Composio la da por activa, pero **Semrush rechaza toda llamada**:

    ERROR 122 :: WRONG FORMAT OR EMPTY KEY

Probado con `SEMRUSH_KEYWORD_OVERVIEW_ONE_DATABASE` y `SEMRUSH_KEYWORD_DIFFICULTY`:
**mismo error en las dos**, así que es la credencial y no un endpoint.

**Pista importante:** el valor que el conector envía a Semrush **no tiene forma de
clave de Semrush** (que es una cadena larga alfanumérica, sin prefijos) sino de
token generado por el propio conector. Sospecha: **la clave no quedó guardada**.

**Que «active» en Composio NO significa que la credencial sirva** — solo que se
guardó algo. La única prueba válida es una llamada real.

### ❌ Diagnóstico EQUIVOCADO (se corrigió, queda por la lección)

Connie cargó **dos claves distintas** (msgs 253 y 255). En las dos, el valor que
Composio envía a Semrush en el parámetro `key=`:

- **cambió** entre un intento y otro, y
- **mantuvo el prefijo `semrtkn-pat-`**, que es formato de **token de Composio**,
  no de clave de Semrush.

**Se concluyó —mal— que el conector generaba un token propio y no pasaba la clave.**

**Era falso.** Connie mandó una captura de su pantalla de API Keys (msg 257) y el
**final de su clave coincide con el final del valor que el conector envía**. La
clave SÍ llegaba.

**El prefijo `semrtkn-pat-` es el formato de las claves v4 de Semrush**, no un
token de Composio.

No hay **una** sola conexión duplicada (verificado con `action: "list"`: una sola
cuenta activa), así que tampoco es que use la vieja.

### 🔑 La causa real: choque de versiones de API

Su captura muestra la clave creada con **Version: v4**, permisos *Read-only*.

Las herramientas de Semrush en Composio llaman al **API clásico**
(`https://api.semrush.com/?type=phrase_this&key=...`), que espera una clave
**de formato antiguo**: cadena alfanumérica larga, **sin prefijos ni guiones**.

Una clave **v4** en ese endpoint da `ERROR 122 :: WRONG FORMAT OR EMPTY KEY`. La
clave es válida; es **del tipo equivocado para esa API**.

**Dónde está la clave clásica:** Semrush → **Info de suscripción** (no «API Keys»)
→ sección **API units**. Si esa sección no existe o marca 0 unidades, ahí sí el
bloqueo es el plan Guru.

### ⚠️ La lección de método

**Dos claves fallando con el mismo prefijo parecía prueba suficiente de que el
conector inventaba el token. No lo era.** Faltaba el dato que solo se veía en la
pantalla de ella: que el prefijo es el formato v4 de Semrush.

**Antes de declarar causa raíz y mandar a escalar, pedir la captura de la pantalla
del otro lado.** Un patrón consistente puede tener una explicación completamente
distinta a la que uno infiere desde su lado del cable.

### ✅ La salida que NO depende de arreglar nada

**Su cuenta Semrush Guru funciona perfecto en el navegador** — lo que no funciona
es la API. Entonces: **ella exporta desde el Keyword Magic Tool** (base Colombia) y
**yo proceso el CSV**: limpieza, agrupación por intención, cruce con competidores y
armado de la planilla.

**Regla general:** cuando una integración está rota pero el usuario tiene la
herramienta en su navegador, **el export manual + procesamiento de mi lado
desbloquea el entregable el mismo día.** No dejarla esperando a que se arregle la
credencial.

**Detalle técnico:** las respuestas de Semrush son **CSV, no JSON**. Hay que
parsear cabeceras y filas. `ERROR 50 :: NOTHING FOUND` significa cero resultados,
no fallo de transporte.

### 2. DataForSEO — elegido por Connie el 20-ago-2026 (msg 259)

Toolkit `dataforseo` en Composio. Da dificultad, volumen, intención de búsqueda,
SERP y keywords que rankea un dominio.

**Precios verificados en su web el 20-ago-2026:**

| Concepto | Costo |
|---|---|
| Por consulta (task) | **US$0,012** |
| Por keyword devuelta (item) | **US$0,00012** |
| Depósito mínimo | **US$50** (saldo, no mensualidad) |

**En su caso:** un estudio de **1.000 keywords con métricas ≈ US$0,13**. Con US$50
alcanza para cientos de estudios.

**Autenticación:** usuario (correo) + **contraseña de API**, distinta de la del
sitio. Va en el conector, **nunca por el chat**.

### ⚠️ Precaución acordada: probar antes de pagar

Después del episodio de Semrush —conector que falla con credencial válida— se le
propuso hacerlo en **dos pasos**:

1. Crear la cuenta (gratis) y conectar
2. **Llamada de prueba de mi lado.** Solo si responde, ella recarga los US$50

**Regla general: nunca pedirle que pague por una integración que todavía no se
probó de punta a punta.**

### Lo que se correría para el caso Colombia / NIVEA body

- Ideas de keywords de la categoría, con volumen
- **Dificultad** (lo que el Planificador no da)
- **Intención de búsqueda** — separa lo que va a Search de lo que va a contenido
- **Qué rankea Lubriderm orgánicamente y dónde NIVEA no aparece** ← el keyword gap,
  que es exactamente lo que pidió Alex y no se arma con datos de publicidad

### 3. Google Search Console — gratis y la mejor fuente para sitios propios

Consultas reales con impresiones, clics, posición y CTR. **No estimaciones.**
Limitación: solo sitios que ella administre. **Hoy NO está conectado** (no está
entre las 8 apps de Maton). Queda por averiguar si se puede sumar.

### 4. Lo que se puede hacer hoy sin pagar nada

`WebFetch` sobre SERPs y páginas: quién rankea, estructura de contenido (H2/H3),
preguntas frecuentes. Sirve para **intención y panorama competitivo**.

⚠️ **Dos límites que hay que declarar y no maquillar:**
- **No da volumen ni dificultad.**
- `WebSearch` devuelve **resultados de EE.UU.**, así que para Colombia o Chile
  sirve a medias. `WebFetch` sobre una URL concreta sí funciona igual.

## Regla

Cuando pregunte por una herramienta que no está conectada: decir en una línea que
no está, **qué credencial haría falta**, y **ofrecer la alternativa concreta** —
no dejarla solo con el «no». Y recordar que **las claves nunca van por el chat**:
se guardan con `/env`.

Relacionado: [[cuota-google-ads]], [[composio-respaldo-google-ads]]
