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

**Cómo lo verifica ella:** Semrush → foto de perfil → *Subscription info* →
sección **API units**. Si dice **0 unidades** o no existe la sección, el bloqueo es
el **plan Guru** (no incluye API). Si hay unidades, ahí está la clave real.

**Detalle técnico:** las respuestas de Semrush son **CSV, no JSON**. Hay que
parsear cabeceras y filas. `ERROR 50 :: NOTHING FOUND` significa cero resultados,
no fallo de transporte.

### 2. DataForSEO — la alternativa recomendada

Toolkit `dataforseo` en Composio, **sin conexión activa**. Da dificultad, volumen,
SERP y keywords que rankea un dominio.

**Modelo de precio verificado en su web el 20-ago-2026:** *pay-as-you-go*, **sin
suscripción mensual**, **depósito mínimo US$50** que se consume por uso.

**Es la opción recomendada** por costo y porque cubre justo lo que Guru no permite
por API.

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
