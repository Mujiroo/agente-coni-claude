# PENDIENTE — Criterios de decisión de Google Ads con Connie

*Acordado el 18-ago-2026 (msg 122). **Aplazado a la vuelta de su viaje a China.***

## Qué se acordó hacer

Connie preguntó cómo «perfeccionarme» en Google Ads y ofreció clases, PPT y
videos. Se le explicó que **eso no sirve**: no retengo nada entre sesiones, y de
Ads en general ya sé; lo que falta es **su contexto**.

Pero en su audio corrigió algo clave: **ella es experta en SEO, no en Ads.** Con
eso, pedirle «sus criterios» era pedirle lo que todavía no tiene. **Se invirtió
el trabajo:**

1. **Yo propongo los criterios, ella decide.** Los umbrales salen de **sus
   propias cuentas**, no de benchmarks genéricos de internet: el CPL bueno de
   Sudtec es el que muestran sus números.
2. **Cada recomendación con el porqué** en lenguaje simple, para que en unos meses
   el criterio sea suyo y no mío.
3. **Separar siempre lo que sé de lo que supongo.** Marcarle cuándo no estoy
   seguro.

## El entregable comprometido

Una **auditoría de la cuenta de Sudtec** y, a partir de ella, un documento de
**criterios de decisión** con:

- qué CPL es bueno y cuál es alarma
- qué CTR es normal **para este rubro**
- cuándo pausar y cuándo aguantar
- **el número real que justifica cada umbral**

Ella lo revisa, discute lo que no le cuadre, y queda como regla común.

## El freno que se dejó explícito

Se le dijo de frente que **yo también me equivoco** — ese mismo día le reporté 7
reenvíos cuando eran 2, y lo cazó ella. Por eso, aunque me dé poder de decisión,
**el dinero no se mueve sin su OK**. Antecedente de la casa: un agente confundió
la moneda y sobregastó ~100×.

## Cuándo

🟡 **A la vuelta de China.** Viaja el **viernes 21-ago-2026**; **la fecha de
regreso está pedida y aún no la sé**. Cuando la dé, conviene dejar un cron que me
lo recuerde para que esto no se pierda.

## Nota aparte, ya avisada

Faltan `OPENAI_API_KEY` y `GEMINI_API_KEY` en el `.env`, así que sus audios caen
al **whisper local**, el peor de los tres motores. Por eso «SEO» se transcribió
como «deseo». Se le pidió cargar una con `/env`.
