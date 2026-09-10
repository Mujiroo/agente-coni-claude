# «Ya hay un puente activo» puede ser mentira: verifica el pid

Al despertar el 10-sep-2026, `bash bin/tg_bridge.sh` salió de inmediato con:

> `[BRIDGE] Ya hay un puente activo (pid 123). No levanto otro.`

**No había ningún puente.** `ps -p 123` no devolvía nada y `ps -eo args | grep tg_`
solo mostraba el watchdog. El candado (`~/.claude/tgstate/tg_bridge.lock.d`) era
del 9-sep: vive en un bind mount, **sobrevive al reinicio del contenedor**, y
tras reiniciar los PIDs arrancan bajos, así que el pid huérfano del candado
**coincidió con un proceso transitorio vivo** justo cuando el script hizo
`kill -0`. Ese es el único chequeo que hace el script, y le dio verde.

## La regla

Si el puente dice «ya hay un puente activo», **no le creas y no te quedes
tranquilo**: confirma con

```bash
ps -eo pid,etime,cmd | grep '[t]g_bridge.sh'
```

Si no aparece ningún `tg_bridge.sh`, el candado es huérfano:

```bash
rm -rf /home/agent/.claude/tgstate/tg_bridge.lock.d
```

y levanta el puente de nuevo con **Monitor**. Después **verifica otra vez con
`ps`** que quedó corriendo y que el pid del candado es el del proceso nuevo —
salir en silencio es justo lo que hace este fallo.

## Por qué importa tanto

Este es el modo de falla más caro que tengo: el contenedor queda en `Up`, la
sesión viva, y yo **sordo sin saberlo**. Constanza escribe y cree que estoy
caído. Un `[BRIDGE]` que parece tranquilizador («el que corre sigue entregando
los mensajes») describe algo que no existe.

El watchdog (`bin/tg_watchdog.sh`) sabe limpiar este candado, pero solo actúa
cada 120 s y con 300 s de gracia inicial: en el arranque **el que tiene que
darse cuenta soy yo**.

Relacionado: [[canal-y-formato]], [[getfile-lento-no-caido]]
