# -*- coding: utf-8 -*-
BASE="https://www.sudtec.cl/product-category/"
COMUNES=["Cotiza en 24 Hrs","Despacho a Todo Chile","Asesoría Técnica Experta",
         "Certificación EN y NFPA","Proveedor Especializado","Cotiza sin Compromiso",
         "Sudtec South Pacific"]
DESC_COMUNES=[
 "Proveedor especializado en equipamiento de emergencia. Cotización en menos de 48 hrs.",
 "Despacho a todo Chile para cuerpos de bomberos, brigadas y empresas. Asesoría técnica.",
 "Equipos certificados bajo norma EN y NFPA. Solicita tu cotización sin compromiso."]

G=[
 # (campaña, grupo, url, keywords, 8 titulares propios, 1 descripcion propia)
 ("Bomberos","Botas","epp/botas/",
  ["botas para bomberos","botas de bombero","botas estructurales","botas lytos","botas bombero chile"],
  ["Botas para Bomberos","Botas Estructurales","Botas Lytos FR","Botas de Bombero Chile",
   "Botas Certificadas","Ver Catálogo de Botas","Botas Jolly y Blauer","Calzado de Emergencia"],
  "Botas Lytos, Jolly y Blauer para bomberos. Revisa el catálogo y pide tu cotización."),
 ("Bomberos","Cascos","epp/cascos/",
  ["cascos para bomberos","casco de bombero","cascos estructurales","casco bombero chile"],
  ["Cascos para Bomberos","Casco Estructural","Cascos Certificados","Casco de Bombero Chile",
   "Ver Catálogo de Cascos","Cascos de Rescate","Protección de Cabeza","Cascos Profesionales"],
  "Cascos certificados para bomberos y rescate. Cotiza el modelo que necesitas."),
 ("Bomberos","Uniformes","epp/uniformes/",
  ["uniformes para bomberos","traje estructural bombero","chaqueta de bombero","jardinera bombero"],
  ["Uniformes para Bomberos","Traje Estructural","Chaqueta de Bombero","Jardinera de Rescate",
   "Uniformes S-GARD","Ver Catálogo Uniformes","Uniforme Certificado","Ropa de Intervención"],
  "Uniformes y trajes estructurales S-GARD para bomberos. Pide tu cotización."),
 ("Bomberos","Guantes","epp/guantes/",
  ["guantes para bomberos","guantes estructurales","guantes de rescate"],
  ["Guantes para Bomberos","Guantes Estructurales","Guantes de Rescate","Guantes Certificados",
   "Ver Catálogo Guantes","Guantes de Extricación","Protección de Manos","Guantes Profesionales"],
  "Guantes estructurales y de rescate certificados. Cotiza en línea sin compromiso."),
 ("Bomberos","Rescate Vehicular","rescate/rescate-vehicular/",
  ["rescate vehicular","herramientas de extricación","separador hidraulico","cizalla de rescate"],
  ["Rescate Vehicular","Equipos de Extricación","Separadores Hidráulicos","Cizallas de Rescate",
   "Herramientas LUKAS","Material de Rescate","Equipo de Excarcelación","Ver Catálogo Rescate"],
  "Equipos LUKAS de rescate vehicular: separadores, cizallas y herramientas combinadas."),
 ("Bomberos","Rescate en Altura","rescate/rescate-en-altura/",
  ["rescate en altura","equipo de rescate vertical","arnes de rescate","cuerdas de rescate"],
  ["Rescate en Altura","Equipo Vertical","Arneses de Rescate","Cuerdas y Descensores",
   "Rescate con Cuerdas","Material de Altura","Ver Catálogo Altura","Equipos Certificados"],
  "Arneses, cuerdas y descensores para rescate vertical. Asesoría técnica incluida."),
 ("Bomberos","Herramientas de Rescate","rescate/herramientas-rescate/",
  ["herramientas de rescate","herramientas para bomberos","hachas para bomberos","herramienta de forzado"],
  ["Herramientas de Rescate","Herramientas Bomberos","Hachas y Barras","Ingreso Forzado",
   "Herramienta Combinada","Material de Rescate","Ver Catálogo Herramientas","Equipo de Demolición"],
  "Hachas, barras y herramientas de forzado para bomberos. Cotiza sin compromiso."),
 ("Bomberos","Cámaras Termales","rescate/camaras-termales-rescate/",
  ["camara termal bomberos","camara termica bomberos","camara termografica rescate"],
  ["Cámaras Termales","Cámara Térmica Bombero","Cámaras de Rescate","Visión Térmica",
   "Cámara Termográfica","Detección de Calor","Ver Catálogo Cámaras","Equipos de Búsqueda"],
  "Cámaras termales para búsqueda y rescate en incendios. Pide tu cotización."),
 ("Bomberos","Estabilización","rescate/estabilizacion/",
  ["estabilizacion vehicular","puntales de estabilizacion","cojines de rescate"],
  ["Estabilización Vehicular","Puntales de Rescate","Cojines de Levante","Sistemas de Apuntalamiento",
   "Estabilizar Vehículos","Material de Estabilización","Ver Catálogo","Equipos de Levante"],
  "Puntales y cojines para estabilización y levante en rescate vehicular."),
 ("Bomberos","Mangueras","material-de-agua/mangueras-de-combate-incendios/",
  ["mangueras de bomberos","manguera contra incendios","manguera de combate"],
  ["Mangueras de Bomberos","Manguera Contra Incendio","Mangueras de Combate","Material de Extinción",
   "Mangueras Certificadas","Ver Catálogo Mangueras","Equipos de Agua","Mangueras Profesionales"],
  "Mangueras de combate contra incendios para cuerpos de bomberos y brigadas."),
 ("Bomberos","Pitones","material-de-agua/pitones/",
  ["pitones para bomberos","pitón contra incendios","lanza de agua bomberos"],
  ["Pitones para Bomberos","Pitón Contra Incendio","Lanzas de Agua","Material de Extinción",
   "Pitones Certificados","Ver Catálogo Pitones","Equipos de Agua","Pitones Profesionales"],
  "Pitones y lanzas de agua para combate de incendios. Cotiza en línea."),
 ("Bomberos","Espuma y CAFS","material-de-agua/cafs/",
  ["sistema cafs","espuma contra incendios","aplicacion de espuma bomberos"],
  ["Sistemas CAFS","Espuma Contra Incendios","Aplicación de Espuma","Equipos de Espuma",
   "CAFS para Bomberos","Material de Extinción","Ver Catálogo CAFS","Espuma Profesional"],
  "Sistemas CAFS y equipos de aplicación de espuma contra incendios."),
 ("Industrial","Rescate Pesado","industrial/rescate-pesado-industrial/",
  ["rescate pesado","rescate industrial","equipos de rescate pesado"],
  ["Rescate Pesado","Rescate Industrial","Equipos de Rescate Pesado","Material Industrial",
   "Rescate en Industria","Equipos Hidráulicos","Ver Catálogo Industrial","Rescate Especializado"],
  "Equipos de rescate pesado para faenas industriales y mineras. Asesoría técnica."),
 ("Industrial","Descontaminación","industrial/descontaminacion/",
  ["descontaminacion hazmat","duchas de descontaminacion","equipos de descontaminacion"],
  ["Descontaminación Hazmat","Duchas de Descontaminación","Equipos Hazmat","Material de Descontaminación",
   "Respuesta a Emergencias","Control de Derrames","Ver Catálogo Hazmat","Equipos Especializados"],
  "Equipos y duchas de descontaminación para respuesta Hazmat. Cotiza sin compromiso."),
 ("Industrial","Tapa Fugas","industrial/tapa-fugas/",
  ["tapa fugas","control de derrames","kit antiderrame"],
  ["Tapa Fugas","Control de Derrames","Kits Antiderrame","Contención de Fugas",
   "Equipos Hazmat","Respuesta a Derrames","Ver Catálogo","Material de Contención"],
  "Sistemas tapa fugas y kits de contención de derrames para emergencias químicas."),
 ("Forestal","Herramientas Forestales","material-forestal/herramientas/",
  ["herramientas forestales","pulaski forestal","rastrillo mcleod","herramientas incendio forestal"],
  ["Herramientas Forestales","Pulaski y McLeod","Combate de Incendios","Material Forestal",
   "Herramientas de Brigada","Incendios Forestales","Ver Catálogo Forestal","Equipos Forestales"],
  "Pulaski, McLeod y herramientas para combate de incendios forestales."),
 ("Forestal","Botas Forestales","material-forestal/botas-material-forestal/",
  ["botas forestales","botas para incendios forestales","calzado forestal"],
  ["Botas Forestales","Botas Incendio Forestal","Calzado Forestal","Botas de Brigada",
   "Botas Certificadas","Material Forestal","Ver Catálogo Botas","Botas Profesionales"],
  "Botas para brigadas de incendios forestales. Certificadas y con despacho a Chile."),
]

PRESU={"Bomberos":6500,"Industrial":1200,"Forestal":800}

def build():
    out=[]
    for camp,grupo,url,kws,props,desc in G:
        heads=props+COMUNES
        descs=DESC_COMUNES+[desc]
        out.append(dict(campana=camp,grupo=grupo,url=BASE+url,keywords=kws,
                        titulares=heads,descripciones=descs))
    return out

if __name__=="__main__":
    errs=[]; data=build()
    for a in data:
        if len(a["titulares"])!=15: errs.append(f"{a['grupo']}: {len(a['titulares'])} titulares")
        if len(a["descripciones"])!=4: errs.append(f"{a['grupo']}: {len(a['descripciones'])} descripciones")
        if len(set(a["titulares"]))!=15: errs.append(f"{a['grupo']}: titulares repetidos")
        for t in a["titulares"]:
            if len(t)>30: errs.append(f"{a['grupo']} TIT {len(t)}>30: {t}")
        for d in a["descripciones"]:
            if len(d)>90: errs.append(f"{a['grupo']} DESC {len(d)}>90: {d}")
    print(f"grupos: {len(data)} | campañas: {len(set(a['campana'] for a in data))}")
    print(f"presupuesto diario: {sum(PRESU.values())} CLP -> mensual {sum(PRESU.values())*30.4:.0f} CLP")
    print(f"keywords totales: {sum(len(a['keywords']) for a in data)}")
    if errs:
        print(f"\n❌ {len(errs)} ERRORES:"); [print("  ",e) for e in errs[:25]]
    else:
        print("\n✅ todos los textos cumplen: 15 titulares ≤30 y 4 descripciones ≤90")
        m=max((len(t),t) for a in data for t in a["titulares"])
        print(f"   titular más largo: {m[0]} chars — «{m[1]}»")
        m=max((len(d),d) for a in data for d in a["descripciones"])
        print(f"   descripción más larga: {m[0]} chars")
