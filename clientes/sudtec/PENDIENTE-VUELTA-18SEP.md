# Sudtec · Qué hacer cuando Connie vuelva (18-sep-2026)

Consolidado el 3-sep-2026 a pedido suyo (msg 690: *«deja anotado para que veamos eso»*).
**Nada de esto se ejecuta antes de que ella llegue.**

---

## 1 · El tag / GTM — LO PRIMERO, y con procedimiento

**Por qué importa:** con `MAXIMIZE_CONVERSIONS`, romper el tag **no arruina el reporte:
apaga la entrega**. En junio costó **−66% de clics** durante 3 semanas y **−25% de
cotizaciones reales**. Ver [[romper-el-tag-apaga-la-entrega]].

**Procedimiento acordado — no saltarse ningún paso:**

1. Montar el tag nuevo **sin apagar el que funciona**. Los dos conviviendo.
2. Verificar que el nuevo **registre de verdad** (no basta con que "esté publicado").
3. **Recién entonces** cambiar la acción principal.
4. Vigilar **clics diarios**, no conversiones: los clics avisan en 24 h.
5. Termómetro independiente: **cotizaciones del sitio** (12-16/semana es lo normal).

## 2 · Los dos defectos de medición confirmados

- **Ventana de conversión de 1 día** en `Formulario de contacto - Enviar` (la otra
  primaria tiene 30). Todo lo que cotizan al día siguiente, Google no lo ve.
  **Aviso ya dado:** al subirla, las conversiones del reporte **suben sin que el negocio
  cambie**. No es mejora.
- **Sobreconteo de 2,6x en agosto:** Ads reportó 151,5 conversiones; el sitio recibió 58
  cotizaciones. Como las conversiones solo vienen de clics propios, deberían ser
  **menos**. Hay **dos acciones primarias** de la misma categoría — sospecha de doble
  conteo, no verificable por API.

## 3 · La decisión de estructura

**Está todo creado y PAUSADO:** 3 campañas, 18 grupos, 18 anuncios, 73 keywords, cada
grupo con su página de categoría.

**Hay que elegir, no se pueden las dos:**

- **Presupuesto:** lo que corre hoy ya suma **297.920/mes** contra su tope de **300.000**.
  Las nuevas suman **8.500/día**. Prenderlas sin bajar las actuales lleva a **~557.000**.
- **Canibalización:** varias keywords están en los dos lados. Si se activan las nuevas
  con `General` prendido, **General se come el tráfico** (tiene el historial). Es
  exactamente lo que pasó en agosto con el grupo Botas.
- **Fase de aprendizaje:** las campañas nuevas parten sin memoria y tardan **1-3
  semanas**. Ver [[fase-de-aprendizaje-explicada]].

**Orden acordado:** medición primero, estructura después, puja al final. **Un cambio a
la vez.**

## 4 · Cosas chicas que quedaron pendientes

- **Negativas del 26-ago:** aplicar `traje encapsulado` y `epp`.
  **NO aplicar `cotona ignífuga`** — convirtió a CPA 1.031, mejor que la base.
  Corregido el 3-sep.
- **Las 3 negativas frenadas** (`scott`, `holmatro`, `rosenbauer`): su familia de frase
  contiene una búsqueda que sí convierte. Si se quieren, van en **exacta**.
- **Lista de negativas a nivel de cuenta:** existe, está aplicada y tiene **0 miembros**.
  Parece configurada y no hace nada.
- **Hueco de catálogo:** `halligan` es el término que más gasta sin convertir
  (2.532 CLP/30d) y Sudtec tiene **0 productos**. Es la herramienta más clásica del
  bombero. Oportunidad comercial, no una negativa.
- **Auditoría completa:** `clientes/sudtec/auditoria-03sep2026.md` — salud 24%,
  cobertura 94%. El crítico de mayor palanca es **G24**: casi todos los anuncios viejos
  apuntan a `/lista-productos/` genérico, y eso hunde el Nivel de calidad, que define el
  CPC — el que se triplicó.

## 5 · Lo que ya quedó hecho el 3-sep

- **10 negativas de frase** en `Campaña Sudtec` (17.798 CLP/30d recuperados, 0
  conversiones perdidas). Las 20 anteriores estaban en **exacta** y no frenaban nada.
- **Grupo `Botas` viejo pausado** (2 clics, 0 conversiones). `botas bombero` sigue
  intacta en `General`: ahí están sus 16,8 conversiones.
- **Estructura nueva creada y pausada**, con destinos verificados HTTP 200.
