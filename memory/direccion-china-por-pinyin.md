---
name: direccion-china-por-pinyin
description: La cadena completa de la dirección del hotel de Shanghái en chino, y cómo guiar a Connie por un selector de dirección de app china cuando no lee caracteres.
metadata:
  type: project
---

**9-sep-2026, 19:28 de Shanghái.** Connie estaba agregando una *delivery address* en una app
china y mandó **tres fotos seguidas en 4 minutos** —«cuál es shangai», «cuál es no lo veo»,
«ayuda»— trabada en cada nivel del selector. Es un flujo de 4 pasos y **cada paso es una
lista distinta**.

## La cadena del hotel, para pegar tal cual

| Nivel | Qué elegir |
|---|---|
| Provincia | `上海` |
| Ciudad | `上海市` |
| Distrito (*County*) | `黄浦区` — Huangpu |
| Subdistrito (*Street* / 街道) | `南京东路街道` — Nanjing East Road |

Dirección para chofer / Didi: `南京东路步行街` ([[shanghai-connie]]).

## Por qué se traba, y qué respuesta la destraba

**Las listas van ordenadas por PINYIN, no por lógica ni por tamaño.** Ella miraba la sección
de la **J** (`静安区`) y concluía que `黄浦区` no existía — estaba **más arriba**, en la **H**.

Lo que funcionó, en este orden:

1. **La letra primero.** *«Sube a la H»* la ubica en un segundo; *«busca 黄浦区»* la deja
   barriendo una lista de caracteres que no lee.
2. **El vecino que confunde, nombrado y descartado.** En la H hay `虹口区` (Hongkou) justo al
   lado — se le dijo **cuál NO es** antes de que se equivocara.
3. **Un rasgo visual del carácter**, no el significado: *«el tuyo empieza con 黄»*.
4. **En una grilla, la posición manda sobre el carácter**: `上海市` se le dio como *«el
   segundo de la primera fila, a la derecha de Beijing»*.

**Regla: para alguien que no lee chino, la coordenada útil es la letra pinyin y la posición
en pantalla — el carácter va como confirmación, no como instrucción de búsqueda.**

## Los dos avisos que se adelantaron sin que preguntara

- **Teléfono:** el formulario pide número chino y **el repartidor llama en vez de subir**.
  Con su chileno en roaming ([[telefono-chileno-en-roaming-china]]) no la ubican; se le dijo
  que use un número local o el del anfitrión.
- **Plazo:** se va a Pekín el **domingo 13**. Si la entrega demora más, el paquete llega a un
  homestay donde ya no está.

**Regla: cuando pide ayuda con un formulario, el trabajo no termina en el campo que preguntó
— los dos campos siguientes son los que le van a fallar.**
