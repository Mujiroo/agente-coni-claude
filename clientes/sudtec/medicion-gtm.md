# SUDTEC — por qué las conversiones no cuadran (y por qué el arreglo se cayó)

*17-ago-2026. Diagnóstico cerrado con evidencia. Nada modificado.*

## Lo que contó Connie (audio, msg 22)

Las conversiones vienen de GTM, ella **sabe que no son 100% correctas**, pero
cuando las corrigió **la campaña se cayó** y llegaron muchas menos solicitudes,
así que **devolvió todo al estado original**.

Confirmado en el propio GTM: la versión en vivo se llama **«RESTAURACIÓN ver.3»**.

## Prueba de que el conteo está inflado

Crucé día a día las conversiones de Ads con los correos `[Solicitud de
presupuesto]` que llegan a la casilla de Connie:

| | 30 días |
|---|---|
| Conversiones en Google Ads | **143** |
| Solicitudes reales (correos de `cg@`) | **55** |
| **Ratio** | **2,60×** |

Días que lo rematan:

| Fecha | Ads | Correos |
|---|---|---|
| 2026-07-26 | 3 | **0** |
| 2026-08-07 | 3 | **0** |
| 2026-08-08 | **9** | **0** |

**El argumento decisivo:** los correos de `cg@` incluyen **todas** las
solicitudes —de Ads, de orgánico y de tráfico directo—. Por lo tanto las
conversiones atribuidas a Ads deberían ser **un subconjunto**, siempre menores.
Son casi el triple. No hay interpretación benigna.

*(Días 27, 28 y 29 de julio: 0 conversiones en Ads y 2-3 correos. Es lo esperable
— solicitudes que no vinieron de Ads.)*

## La causa exacta, en GTM

Contenedor **`GTM-NGQV7WCW`** (`accounts/6239878086/containers/190040740`),
versión en vivo **6 «RESTAURACIÓN ver.3»**.

El tag `awct` **«Seguimiento de conversiones de Google Ads»**
(`conversionId 17032241815`, label `V5w-CKOJ7sMaEJfFzbk_`) dispara con el
trigger **«Envio de formularioo»** *(con tres oes — es un duplicado de «Envío de
formulario»)*:

```
tipo:             formSubmission
filtros:          NINGUNO          <-- cualquier formulario del sitio
checkValidation:  no activado      <-- cuenta envíos fallidos o incompletos
```

**Sin filtros, en un WordPress/WooCommerce**, eso dispara con el buscador de la
tienda, el newsletter, el login, los filtros de producto y el carrito. Ahí está
el 2,6×.

*(Hay además un trigger «Todos los elementos» de tipo `click` sin filtros, y un
«Envío de formulario» duplicado. El contenedor tiene basura acumulada.)*

## Por qué se cayó al arreglarlo — y cómo evitarlo

No se cayó porque medir bien sea peor. Se cayó porque al cambiar la conversión
de golpe, con `MAXIMIZE_CONVERSIONS`:

1. La campaña volvió a **fase de aprendizaje** (1-2 semanas de entrega errática).
2. Perdió el **historial** con el que venía pujando.
3. Pasó de ~5 conversiones/día a ~2 y **pujó más conservador**.

Ella revirtió **en plena fase de aprendizaje**, que es exactamente cuando peor se
ve. El arreglo probablemente iba bien y no alcanzó a estabilizarse.

### El camino propuesto (msg 24, pendiente de su OK)

1. Crear la conversión correcta (solo el formulario de cotización, con
   validación) y dejarla **SECUNDARIA** — mide sin influir en la puja: **cero
   fase de aprendizaje, cero caída**.
2. Correr las dos en paralelo **3-4 semanas**.
3. **Validarla contra los correos de `cg@`**, que ya leo para el reenvío: reporte
   semanal «Ads marcó X / llegaron Y». Comprobada contra la realidad.
4. Cuando peguen, pasarla a principal **en una semana que ella elija**, sabiendo
   de antemano que vienen 1-2 semanas de aprendizaje.

### Advertencia que hay que dar ANTES al cliente

Al medir bien, **las conversiones bajan y el CPA sube en el informe**. No es
deterioro: es dejar de contar cotizaciones que nunca existieron. Si el cliente se
entera después, va a parecer que la campaña se echó a perder.

## Estado

🟡 **Nada tocado.** Es el sitio y el GTM del cliente. Esperando OK de Connie para
preparar el paso 1.
