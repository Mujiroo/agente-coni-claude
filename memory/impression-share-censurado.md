# El impression share de Google Ads viene CENSURADO

Cuando `metrics.search_impression_share` vale exactamente **0.1** y
`metrics.search_budget_lost_impression_share` vale exactamente **0.9**, eso **no es una
medición**: es el tope del reporte. Google publica esos valores como «< 10%» y «> 90%»
y la API los devuelve como 0.1 y 0.9 planos.

**La señal para detectarlo:** el número se clava en un redondo exacto muchos días
seguidos. Una métrica real fluctúa. En la cuenta de Sudtec, del 10 al 18-ago el IS
variaba natural (12,4 · 14,8 · 26,3 · 17,7 · 19,5 · 22,0 · 20,3 · 15,0) y desde el
19-ago quedó clavado en 10,0 / 90,0 durante trece días.

**El error que costó:** el 1-sep-2026 leí ese 90% como exacto y construí encima una
«contradicción» (pierde el 90% por presupuesto pero no lo gasta) que sostenía una
hipótesis equivocada — que la puja automática se había apagado sola. Se la propuse a
Connie como acción. Al pedirme ella el fundamento («¿en qué te basas?») y bajar a
mirar las keywords, la causa real resultó ser otra: una sola amplia genérica
(`equipo de protección personal`) se llevaba el 49% del gasto con CPA de 14.489 CLP
contra 1.675 de base.

**La regla:** ante una caída de rendimiento, la keyword y el CPC son datos duros; el
impression share puede estar censurado. **Baja a `keyword_view` con costo, clics y
conversiones antes de teorizar.** El gasto por keyword no miente.

Ver también [[leer-estado-real-antes-de-proponer]] y [[verificar-estado-antes-de-ejecutar-lo-aprobado]].
