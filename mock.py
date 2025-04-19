import json
import os

# Combinaciones de nombre de archivo y nombre de libro
ARCHIVOS_LIBROS = [
    ("0200-MockNormativaComercial", "Normativa Comercial"),
    ("0300-MockPasesInternacionales", "Pases Internacionales"),
    ("0400-MockPlanDeIgualdadDeGenero", "Plan de Igualdad de Género"),
    ("0500-MockCulturaDeSeguridad", "Cultura de Seguridad"),
    ("0600-MockExperienciaDeUsiario", "Experiencia de Usuario")
]

# Asegurar directorio de salida
os.makedirs("temario", exist_ok=True)

for nombre_archivo, nombre_libro in ARCHIVOS_LIBROS:
    ruta_salida = f"temario/{nombre_archivo}.json"

    # Generar 80 preguntas mock
    mock_preguntas = []
    for i in range(1, 81):
        pregunta = {
            "libro": nombre_libro,
            "capitulo": f"Capítulo Mock {((i - 1) // 10) + 1}",
            "formulaciones": [
                {
                    "texto": f"¿Puedes responder esta mock-pregunta {i}?",
                    "modo": "una_correcta",
                    "tipo": "positiva"
                }
            ],
            "respuestas_correctas": [
                f"respuesta correcta {i}-1",
                f"respuesta correcta {i}-2",
                f"respuesta correcta {i}-3"
            ],
            "respuestas_incorrectas": [
                f"respuesta incorrecta {i}-1",
                f"respuesta incorrecta {i}-2",
                f"respuesta incorrecta {i}-3",
                f"respuesta incorrecta {i}-4"
            ],
            "fragmento_original": f"Este es el fragmento original de la pregunta mock número {i}.",
            "etiquetas": [f"mock", f"pregunta_{i}"]
        }
        mock_preguntas.append(pregunta)

    # Guardar archivo JSON
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(mock_preguntas, f, indent=2, ensure_ascii=False)

    print(f"\n✔ Archivo generado: {ruta_salida}")
