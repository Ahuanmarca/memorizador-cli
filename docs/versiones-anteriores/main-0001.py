import json
import random
import os
import datetime

# Cargar preguntas
with open("temario-completo.json", encoding="utf-8") as f:
    preguntas = json.load(f)

# Mezclar preguntas
random.shuffle(preguntas)

resumen_errores = []

print("\n--- Entrenamiento iniciado. Escribe 'x' para salir en cualquier momento. ---\n")

for item in preguntas:
    formulacion = random.choice(item["formulaciones"])
    modo = formulacion["modo"]
    tipo = formulacion["tipo"]
    pregunta = formulacion["texto"]

    correctas = item["respuestas_correctas"]
    incorrectas = item["respuestas_incorrectas"]
    opciones = []
    respuesta_correcta = ""

    if modo == "una_correcta" and tipo == "positiva":
        respuesta_correcta = random.choice(correctas)
        opciones = [respuesta_correcta] + random.sample(incorrectas, 3)
    elif modo == "una_correcta" and tipo == "negativa":
        respuesta_correcta = random.choice(incorrectas)
        opciones = [respuesta_correcta] + random.sample(correctas, 3)
    elif modo == "todas_correctas" and tipo == "positiva":
        seleccionadas = random.sample(correctas, 3)
        respuesta_correcta = "Todas las anteriores son correctas."
        opciones = seleccionadas + [respuesta_correcta]
    elif modo == "todas_correctas" and tipo == "negativa":
        seleccionadas = random.sample(incorrectas, 3)
        respuesta_correcta = "Todas las anteriores."
        opciones = seleccionadas + [respuesta_correcta]

    random.shuffle(opciones)

    print(f"\n{pregunta}\n")
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

    respuesta_usuario = input("\nSelecciona una opción (1-4) o 'x' para salir: ")

    if respuesta_usuario.lower() == 'x':
        break

    try:
        indice_usuario = int(respuesta_usuario) - 1
        if opciones[indice_usuario] == respuesta_correcta:
            print("✅ ¡Correcto!\n")
        else:
            print("❌ Incorrecto.\n")
            resumen_errores.append({
                "pregunta": pregunta,
                "respuesta_usuario": opciones[indice_usuario],
                "respuesta_correcta": respuesta_correcta,
                "fragmento": item["fragmento_original"]
            })
    except:
        print("❌ Entrada no válida.\n")

# Guardar resumen
if resumen_errores:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"logs/{now}-resumen.md"
    os.makedirs("logs", exist_ok=True)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("# Resumen de errores\n\n")
        for i, err in enumerate(resumen_errores, 1):
            f.write(f"## Pregunta {i}\n")
            f.write(f"**Pregunta:** {err['pregunta']}\n\n")
            f.write(f"**Tu respuesta:** {err['respuesta_usuario']}\n\n")
            f.write(f"**Correcta:** {err['respuesta_correcta']}\n\n")
            f.write(f"**Fragmento:**\n{err['fragmento']}\n\n")

    print(f"\nSe ha guardado un resumen de los errores en: {nombre_archivo}\n")
else:
    print("\nNo hubo errores. ¡Buen trabajo!")
