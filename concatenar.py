import os
import json
from pathlib import Path

# Rutas y archivos
directorio_temario = "temario"
archivo_salida = "temario-completo.json"
log_errores = "logs/errores-concatenacion.log"

# Crear carpeta de logs si no existe
Path("logs").mkdir(exist_ok=True)

temario_consolidado = []
errores = []

campos_estudio = {
    "aciertos_consecutivos": 0,
    "fallos_totales": 0,
    "veces_vista": 0,
    "ultima_vez_vista": None,
    "ultima_vez_acertada": None,
    "descartada": False,
    "proxima_revision": None,
    "notas_personales": ""
}

def limpiar_formulaciones_invalidas(item, nombre_archivo, index_item):
    nuevas_formulaciones = []
    for f in item.get("formulaciones", []):
        if f.get("modo") == "una_correcta" and f.get("tipo") == "negativa":
            if len(item.get("respuestas_correctas", [])) < 3:
                errores.append(f"{nombre_archivo} - ítem {index_item}: formulación 'una_correcta' negativa con menos de 3 respuestas_correctas")
                continue
        nuevas_formulaciones.append(f)
    item["formulaciones"] = nuevas_formulaciones
    return item

def agregar_campos_estudio(item):
    for k, v in campos_estudio.items():
        if k not in item:
            item[k] = v
    return item

# Leer archivos del directorio temario
for nombre_archivo in os.listdir(directorio_temario):
    if not nombre_archivo.endswith(".json"):
        continue

    ruta = os.path.join(directorio_temario, nombre_archivo)

    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except Exception as e:
        errores.append(f"{nombre_archivo}: error al leer JSON - {str(e)}")
        continue

    if not isinstance(datos, list) or not datos:
        continue  # Ignorar silenciosamente

    for index, item in enumerate(datos):
        item = limpiar_formulaciones_invalidas(item, nombre_archivo, index)
        item = agregar_campos_estudio(item)
        temario_consolidado.append(item)

# Guardar archivo final
with open(archivo_salida, "w", encoding="utf-8") as f:
    json.dump(temario_consolidado, f, indent=2, ensure_ascii=False)

# Guardar errores si los hubo
if errores:
    with open(log_errores, "w", encoding="utf-8") as f:
        f.write("Errores durante la concatenación:\n\n")
        for err in errores:
            f.write(f"- {err}\n")

# Feedback al usuario
print(f"\n✔ Preguntas válidas concatenadas: {len(temario_consolidado)}")
if errores:
    print(f"⚠ Se registraron errores. Revisa el archivo {log_errores}")
else:
    print("✅ No se encontraron errores.")
