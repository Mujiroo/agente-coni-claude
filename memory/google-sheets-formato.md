# Google Sheets por Maton — escribir SIN romper el formato

*18-ago-2026. Aprendido a los golpes en `Chile - NIVEA` (Cheil), ronda 1 vs ronda 2.*

## El error que cometí

Escribí una celda con `values.update` / `values:batchUpdate`. **Eso borra los
`textFormatRuns` de la celda**: el texto queda bien, pero se pierde la negrita y
el color de las palabras. En el trabajo de Cheil eso **borró un texto ancla**
(negrita + rojo = enlace interno), y Connie lo notó antes que yo.

## La forma correcta

Si la celda lleva formato dentro del texto, se escribe valor **y** formato juntos:

```
POST google-sheets/v4/spreadsheets/<id>:batchUpdate
{"requests":[{"updateCells":{
  "start":{"sheetId":<gid>,"rowIndex":fila-1,"columnIndex":col},  // A=0, F=5, H=7
  "fields":"userEnteredValue,textFormatRuns",
  "rows":[{"values":[{"userEnteredValue":{"stringValue":"..."},
                      "textFormatRuns":[...]}]}]}}]}
```

Reglas de los `textFormatRuns`:

- Son **offsets de caracteres**; cada tramo rige hasta el `startIndex` del
  siguiente. Para volver a lo normal hay que meter un tramo `{"format":{}}`.
- El primer tramo va **sin** `startIndex` (implícito 0).
- **`startIndex` debe ser `< len(texto)`.** Si el tramo marcado cierra la celda,
  NO se agrega el reseteo final, o devuelve
  `400 TextFormatRun.startIndex must be less than the length`.
- Antes de escribir, **leer los runs que ya están** con
  `?includeGridData=true&fields=sheets(data(rowData(values(formattedValue,textFormatRuns))))`
  y respetarlos: hay negritas que no son anclas (subtítulos numerados).

## Regla de trabajo

**Siempre respaldar valor + formato antes de escribir** (un JSON en la carpeta
del cliente), y **leer de vuelta la celda** después. Ver
[[connie]] y `clientes/cheil-nivea-eucerin/chile-nivea-bb-cc-cream.md`.
