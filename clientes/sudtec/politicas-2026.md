# SUDTEC — Auditoría de políticas 2026 (Meta + Google Ads)

*18-ago-2026. Pedido por Connie (msg 40-41), que me pasó el resumen de políticas
que le dieron en la pega. **Todo lo que sigue es lectura: no se modificó nada.***

## Alcance real (importante)

- **Google Ads: auditado de verdad**, cuenta `9907217991`, vía Maton.
- **Meta Ads: NO auditado — no hay integración.** De Meta solo existe Instagram
  por Composio (publicar y DMs), que no toca el administrador de anuncios.
  Auditar Meta requiere que Nicolás conecte Meta Ads. Se le dijo a Connie.

## Lo que está en orden ✅

- **13 anuncios, los 13 `APPROVED` / `REVIEWED`.** Ninguno rechazado ni pendiente.
  Incluye los dos publicados el 17-ago (`821206571976`, `821323439891`).
- Presupuestos sin cambios: 9.100 + 700 = **9.800 CLP/día → 297.920/mes**, bajo
  el tope de 300.000 del cliente.
- Cuenta `ENABLED`, moneda **CLP**, no es de prueba, auto-tagging activo.
- **Ninguna campaña cae en categorías sensibles** (salud, finanzas, política,
  elecciones). Buena parte de lo que endureció Meta simplemente no aplica acá.
- **«Despacho a todo Chile» SÍ está respaldado en el sitio**: la home dice
  *«Despachos a todo Chile por medio de Turbus, Starken, Chilexpress o Pullman
  Bus.»* El claim que agregué el 17-ago está sostenido.

## Hallazgos 🔴

### 1. «Certificación EN y NFPA» sin respaldo en el destino

Aparece en **3 de los 4 anuncios activos** (`749580460058`, `821206571976`,
`821323439891`). Se revisó `sudtec.cl` y `sudtec.cl/lista-productos/`: **la
certificación no se menciona en ninguna parte visible del sitio.**

Probablemente el claim es cierto (las marcas del catálogo suelen estarlo), pero
el punto de la revisión multimodal nueva es la **coherencia anuncio ↔ landing**.
Si el destino no lo evidencia, el anuncio queda expuesto.

**Origen del claim:** venía del anuncio original `749580460058`, no fue inventado
en los anuncios nuevos — pero sí se repitió en ellos.

**Salida recomendada:** publicarlo en el sitio, no borrarlo del anuncio.

### 2. La cuenta se contradice sola: 24h vs 48h

| Dónde | Qué dice |
|---|---|
| Anuncios `749580460058`, `821206571976`, `821323439891` | «Cotiza en 24 Horas» / «Cotización en 24h» |
| Sitelink «Cotiza con Nosotros!» | «Tu cotizacion en menos de **48hrs**» |

Se muestran **en la misma subasta**. Hay que unificar. Ninguno de los dos plazos
aparece en el sitio.

### 3. No hay política de privacidad ni términos

Ni en la home ni en la landing. En Google es tolerable; **en Meta es rechazo
directo si se usa formulario nativo de leads** (la política exige que esté
activa, accesible y que refleje qué datos se recogen).

## Etiqueta de IA (Google, vigente desde el 13-jul-2026)

Aplica a **imagen y video**, no a texto. Los anuncios son RSA (texto), pero hay
**9 assets `AD_IMAGE` activos** entre las dos campañas.

Nombres de los archivos: `Captura de Pantalla 2025-04-25 a la(s) 11.xx.xx.png`
(x4) y `campaña sudtec.png` / `sudtec1.png` / `sudtec2.png`. **Son de abril de
2025 y tienen pinta de captura real, no de imagen generada.**

**La procedencia no se puede verificar por API.** Pendiente que Connie confirme
si alguna se hizo o retocó con IA. Si no, no hay nada que etiquetar.

## Verificación de anunciante

**No hay campo en la API de Google Ads para leerla.** Hay que mirarla en el panel
(*Herramientas → Configuración → Verificación del anunciante*). Si está vencida,
Google puede pausar la cuenta completa. Pedido a Connie.

## Marcas de terceros en sitelinks

Los sitelinks nombran **ADALIT** (linternas) y **FLIR** (cámaras termales), y
ambos tienen categoría propia en el catálogo → uso de revendedor, permitido. Sin
riesgo, se deja anotado por si cambia el catálogo.

## Pendiente de respuesta de Connie (18-ago)

1. ¿La certificación EN/NFPA es real y se puede publicar en el sitio?
2. ¿El plazo de cotización es de 24 o 48 horas?
3. ¿Alguna de las 9 imágenes se hizo o retocó con IA?
4. ¿Qué dice la verificación de anunciante en el panel?

Con 1-3 respondidas, los tres hallazgos se cierran sin tocar el anuncio bueno.
