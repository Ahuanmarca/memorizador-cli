import os
import json
from pathlib import Path

# Rutas y archivos
directorio_temario = "temario"
archivo_salida = "temario-completo.json"
log_errores = "logs/errores-concatenacion.log"

# Crear carpeta de logs si no existe
Path("logs").mkdir(exist_ok=True)

# Definir campos de estudio
def campos_estudio():
    return {
        "aciertos_consecutivos": 0,
        "fallos_totales": 0,
        "veces_vista": 0,
        "ultima_vez_vista": None,
        "ultima_vez_acertada": None,
        "descartada": False,
        "proxima_revision": None,
        "notas_personales": ""
    }

# Configuración para generación de preguntas mock
MOCK_CONFIG = [
    ("Condiciones Generales", 20),
    ("Normativa Comercial", 20),
    ("Pases Internacionales", 20),
    ("Plan de Igualdad de Género", 20),
    ("Cultura de Seguridad", 20),
    ("Experiencia de Usuario", 20),
]

# Funciones auxiliares
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
    for k, v in campos_estudio().items():
        if k not in item:
            item[k] = v
    return item

def generar_hash(item):
    clave = (
        item.get("libro"),
        item.get("capitulo"),
        json.dumps(item.get("formulaciones", []), sort_keys=True, ensure_ascii=False),
        json.dumps(item.get("respuestas_correctas", []), sort_keys=True, ensure_ascii=False),
        json.dumps(item.get("respuestas_incorrectas", []), sort_keys=True, ensure_ascii=False),
        item.get("fragmento_original")
    )
    return hash(clave)

def generar_mock_items(libro, existentes):
    existentes_mock = [p for p in existentes if p.get("libro") == libro and "mock" in p.get("etiquetas", [])]
    count_real = len([p for p in existentes if p.get("libro") == libro and "mock" not in p.get("etiquetas", [])])

    # Eliminar mocks si hay suficientes reales
    if count_real >= 20:
        return [p for p in existentes if not (p.get("libro") == libro and "mock" in p.get("etiquetas", []))]

    # Generar nuevos mocks si faltan
    cantidad_faltante = 20 - count_real
    nuevos_mocks = []
    for i in range(1, cantidad_faltante + 1):
        nuevos_mocks.append(agregar_campos_estudio({
            "libro": libro,
            "capitulo": f"Capítulo Mock {((i - 1) // 5) + 1}",
            "formulaciones": [{
                "texto": f"¿Puedes responder esta mock-pregunta {i}?",
                "modo": "una_correcta",
                "tipo": "positiva"
            }],
            "respuestas_correctas": [f"respuesta correcta {i}-1", f"respuesta correcta {i}-2", f"respuesta correcta {i}-3"],
            "respuestas_incorrectas": [
                f"respuesta incorrecta {i}-1",
                f"respuesta incorrecta {i}-2",
                f"respuesta incorrecta {i}-3",
                f"respuesta incorrecta {i}-4"
            ],
            "fragmento_original": f"Este es el fragmento original de la pregunta mock número {i}.",
            "etiquetas": ["mock", f"pregunta_{i}"]
        }))

    return [p for p in existentes if p.get("libro") != libro or "mock" not in p.get("etiquetas", [])] + nuevos_mocks

# Leer contenido existente (si lo hay)
if os.path.exists(archivo_salida):
    with open(archivo_salida, encoding="utf-8") as f:
        existentes = json.load(f)
else:
    existentes = []

# Indexar preguntas existentes
hash_existentes = {generar_hash(p): p for p in existentes}
temario_consolidado = []
errores = []

# Leer y ordenar archivos alfabéticamente
archivos_json = sorted([
    nombre for nombre in os.listdir(directorio_temario)
    if nombre.endswith(".json")
])

# Procesar cada archivo en orden
for nombre_archivo in archivos_json:
    ruta = os.path.join(directorio_temario, nombre_archivo)

    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except Exception as e:
        errores.append(f"{nombre_archivo}: error al leer JSON - {str(e)}")
        continue

    if not isinstance(datos, list) or not datos:
        continue

    for index, item in enumerate(datos):
        item = limpiar_formulaciones_invalidas(item, nombre_archivo, index)
        item = agregar_campos_estudio(item)
        h = generar_hash(item)
        if h in hash_existentes:
            temario_consolidado.append(hash_existentes[h])
        else:
            temario_consolidado.append(item)

# Aplicar lógica de mocks libro por libro
for libro, _ in MOCK_CONFIG:
    temario_consolidado = generar_mock_items(libro, temario_consolidado)

# Guardar archivo final
with open(archivo_salida, "w", encoding="utf-8") as f:
    json.dump(temario_consolidado, f, indent=2, ensure_ascii=False)

# Guardar errores si los hubo
if errores:
    with open(log_errores, "w", encoding="utf-8") as f:
        f.write("Errores durante la concatenación:\n\n")
        for err in errores:
            f.write(f"- {err}\n")

# Feedback
preexistentes = len([item for item in temario_consolidado if generar_hash(item) in hash_existentes])
nuevas = len(temario_consolidado) - preexistentes
total = len(temario_consolidado)

print(f"\n📄 Preguntas preexistentes conservadas: {preexistentes}")
print(f"🆕 Preguntas nuevas agregadas: {nuevas}")
print(f"📚 Total de preguntas en temario-completo.json: {total}")

if errores:
    print(f"⚠ Se registraron errores. Revisa el archivo {log_errores}")
else:
    print("✅ No se encontraron errores.")
