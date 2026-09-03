---
name: romper-el-tag-apaga-la-entrega
description: Con puja automática por conversiones, romper el tag no arruina el reporte: apaga la entrega. En Sudtec costó el 66% del tráfico durante tres semanas.
metadata:
  type: project
---

**3-sep-2026 (msg 688) Connie contó** que cuando cambió la medición en GTM *«dejaron de
llegar cotizaciones, como que las campañas cagaron un tiempo»*. **Tenía razón y yo le
había dicho lo contrario.**

## Lo que muestran los datos

| semana | clics | gasto | cotizaciones reales |
|---|---|---|---|
| 4-10 may | 272 | 63.081 | 16 |
| 11-17 may | 249 | 61.952 | 11 |
| 18-24 may | 259 | 70.371 | 11 |
| 25-31 may | 266 | 70.920 | 19 |
| **1-7 jun** | **95** | **18.715** | 12 |
| **8-14 jun** | **77** | **18.353** | 10 |
| **15-21 jun** | **88** | **27.207** | 10 |
| 22-28 jun *(revertido)* | **317** | 120.579 | 11 |

- **Entrega: −66%.** Impresiones, clics y gasto se derrumbaron juntos. Google **dejó de
  mostrar los anuncios**; no fue un problema de reporte.
- **Cotizaciones reales: 14,2/semana → 10,7/semana, −25%.** Menor que la caída de
  entrega (otros canales amortiguaron), pero **real**.

## El mecanismo

La cuenta usa **MAXIMIZE_CONVERSIONS**. Google decide cuánto pujar **mirando las
conversiones que recibe**. Si el tag se rompe, no ve conversiones, concluye que nada
funciona y **deja de pujar**.

> No se rompió el termómetro: se apagó la caldera.

## El error mío que se corrigió ante ella

Le dije **«tu negocio nunca se cayó»**. **Falso para junio.** Miré agosto —donde las
cotizaciones sí se mantuvieron— y **estiré esa conclusión hacia atrás sin comprobarla**.
Son dos problemas distintos y los mezclé:

- **Junio:** el tag se rompió → la entrega se apagó → cayeron las cotizaciones de verdad.
- **Agosto:** el tag sobrecuenta **2,6x** → las conversiones reportadas están infladas.

## La consecuencia para el plan

**Se retiró la propuesta de arreglar la medición mientras ella viaja.** Si el tag se
rompe, no se pierde un reporte: se pierden **dos tercios del tráfico** hasta que alguien
lo note. No se hace con ella en China.

**El procedimiento seguro, para cuando vuelva el 18-sep:**

1. Montar el tag nuevo **sin apagar el que funciona**; los dos conviviendo.
2. Verificar que el nuevo **registre de verdad**.
3. **Recién entonces** cambiar la acción principal.
4. Vigilar los **clics diarios**, no las conversiones: los clics avisan en 24 h, las
   conversiones tardan por la ventana de atribución.

**Nunca dejar un momento con Google a ciegas.** Eso es exactamente lo que pasó en junio.

## La lección de método

**Mirar los clics, no solo las conversiones.** Un desplome de entrega se ve en clics e
impresiones de inmediato; en conversiones se confunde con «no convirtió». Si me hubiera
quedado en las conversiones, habría seguido creyendo que en junio solo falló el conteo.

Va con [[cotizaciones-del-sitio-son-el-termometro]] y [[gasto-cero-con-impresiones]].
