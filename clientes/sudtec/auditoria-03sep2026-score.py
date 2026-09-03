# Motor de puntaje segun memory/skills/ads-auditoria/references/scoring-system.md
# health = 100 * sum(peso de los PASS) / sum(peso de los controles CONOCIDOS)
# unknown: sale del health, QUEDA en la cobertura. not_applicable: sale de ambos.
W={"critical":5,"high":3,"medium":1,"informational":0}
C=[
 # id, categoria, severidad, estado, evidencia
 ("G42","Medición","high","pass","2 acciones ENABLED, ambas de formulario de contacto"),
 ("G46","Medición","critical","fail","'Formulario de contacto - Enviar' tiene ventana de clic de 1 DIA"),
 ("G48","Medición","medium","fail","las 2 primarias usan modelos de atribución distintos (last-click vs data-driven)"),
 ("G49","Medición","medium","fail","valor por defecto 1 en ambas; no hay valor real por cotización"),
 ("G-CT1","Medición","high","unknown","2 primarias de categoría SUBMIT_LEAD_FORM: posible doble conteo, no verificable por API"),
 ("G-CT2","Medición","medium","unknown","enlace con GA4 no verificado"),
 ("G-CT3","Medición","medium","pass","las conversiones se registran; GTM Kit instalado en el sitio"),
 ("G13","Términos","medium","pass","informe de 1.135 términos revisado hoy 3-sep"),
 ("G14","Términos","high","fail","las 20 negativas previas estaban en EXACTA y no frenaban las variantes"),
 ("G15","Términos","medium","fail","lista de negativas de CUENTA aplicada pero con 0 miembros"),
 ("G16","Términos","critical","fail","77% del gasto de la keyword principal en búsquedas no bomberiles"),
 ("G17","Términos","high","fail","amplia activa sin la lista de negativas apretada que exige el playbook"),
 ("G-WS1","Términos","medium","pass","keywords sin conversión investigadas con histórico mensual"),
 ("G01","Estructura","medium","fail","sin convención de nombres ('Campaña Sudtec', 'Competencias')"),
 ("G02","Estructura","medium","fail","existe un grupo llamado 'Grupo de anuncios 1'"),
 ("G03","Estructura","high","fail","el grupo 'General' es cajón de sastre: EPP, bomberos, botas, mangueras juntos"),
 ("G04","Estructura","medium","pass","solo 2 campañas activas, sin fragmentación"),
 ("G05","Estructura","high","fail","no hay campaña de MARCA separada"),
 ("G08","Estructura","high","fail","una sola keyword se llevó el 61,6% del presupuesto de septiembre"),
 ("G09","Estructura","medium","pass","proyección 285.027 CLP contra tope de 300.000"),
 ("G12","Estructura","medium","fail","Socios de Búsqueda ON en la principal: 146 CLP, 6 clics, 0 conversiones"),
 ("G06","Estructura","informational","not_applicable","la campaña Performance Max está REMOVED"),
 ("G20","Calidad","high","fail","QS 1 en 'improfor' (9.184 CLP) y en 'arnés de seguridad para alturas'"),
 ("G24","Calidad","critical","fail","experiencia de página BELOW_AVERAGE en casi todo el gasto alto"),
 ("G-KW1","Calidad","medium","fail","8 de 14 anuncios con 0 impresiones en 30 días"),
 ("G26","Anuncios","medium","pass","hay RSA en cada grupo activo"),
 ("G27","Anuncios","medium","pass","15 titulares en los anuncios principales"),
 ("G28","Anuncios","medium","pass","4 descripciones"),
 ("G29","Anuncios","medium","fail","fuerza POOR en 2 anuncios de Improfor y otros"),
 ("G-AD2","Anuncios","medium","pass","CTR de cuenta 12,24%; el principal 12,43%"),
 ("G50","Extensiones","medium","pass","6 sitelinks en la campaña principal"),
 ("G51","Extensiones","medium","fail","sin extensiones de texto destacado (callouts)"),
 ("G52","Extensiones","medium","fail","sin fragmentos estructurados"),
 ("G53","Extensiones","medium","pass","4 imágenes"),
 ("G54","Extensiones","medium","fail","sin extensión de llamada"),
 ("G36","Puja","medium","pass","MAXIMIZE_CONVERSIONS activo en ambas campañas"),
 ("G37","Puja","medium","not_applicable","no hay tCPA fijado"),
 ("G39","Puja","high","fail","la campaña gasta el presupuesto completo con CPA inflado"),
]
import collections
cat=collections.defaultdict(lambda: {"pass":0,"known":0,"appl":0,"unk":0,"fail":0})
for cid,c,sev,st,ev in C:
    w=W[sev]
    if st=="not_applicable": continue
    cat[c]["appl"]+=w
    if st=="unknown": cat[c]["unk"]+=w; continue
    cat[c]["known"]+=w
    if st=="pass": cat[c]["pass"]+=w
    else: cat[c]["fail"]+=w
print(f"{'categoría':14}{'salud':>7}{'cobertura':>11}   (peso pass/known · desconocido)")
tp=tk=ta=0
for c,v in cat.items():
    h=100*v["pass"]/v["known"] if v["known"] else 0
    cov=100*v["known"]/v["appl"] if v["appl"] else 0
    tp+=v["pass"]; tk+=v["known"]; ta+=v["appl"]
    print(f"{c:14}{h:6.0f}%{cov:10.0f}%   ({v['pass']}/{v['known']} · {v['unk']})")
print(f"\nSALUD GLOBAL      {100*tp/tk:.0f}%")
print(f"COBERTURA         {100*tk/ta:.0f}%   (evidencia disponible sobre controles aplicables)")
print(f"ventana de datos: 30 días (3-ago a 2-sep-2026) · zona America/Santiago · CLP")
crit=[x for x in C if x[2]=="critical" and x[3]=="fail"]
print(f"\nFALLOS CRÍTICOS: {len(crit)}")
for cid,c,sev,st,ev in crit: print(f"  {cid} · {c} · {ev}")
alt=[x for x in C if x[2]=="high" and x[3]=="fail"]
print(f"\nFALLOS ALTOS: {len(alt)}")
for cid,c,sev,st,ev in alt: print(f"  {cid} · {c} · {ev}")
