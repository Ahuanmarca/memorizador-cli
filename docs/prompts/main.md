# PROMPT 1

En base a esta version de main haz estos cambios:
- menu de modos: libre, libro, test corto, test completo
- el modo libre lanza preguntas de todo el temario, como ya esta haciendo
- el modo libro se restringe a preguntas de cierto libro
- el modo test corto retorna un string que explique que el feature esta en construccion
- el modo test completo tambien
- que este menu inicial tambien aproveche readchar

import json
import random
import os
import datetime
import readchar

# Cargar preguntas
with open("temario-completo.json", encoding="utf-8") as f:
    preguntas = json.load(f)

# Mezclar preguntas
random.shuffle(preguntas)

resumen_errores = []

print("\n--- Entrenamiento iniciado. Presiona 1-4 para responder, 'x' para salir. ---\n")

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

    print("\nSelecciona una opción (1-4) o 'x' para salir:")
    while True:
        key = readchar.readkey()
        if key in ['1', '2', '3', '4']:
            indice_usuario = int(key) - 1
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
            break
        elif key.lower() == 'x':
            print("\nSesión interrumpida por el usuario.")
            break
        else:
            print("Entrada inválida. Presiona 1-4 o 'x'.")

    if key.lower() == 'x':
        break

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


# PROMPT 2

Quiero que la opcion 2 tambien funcione con readchar. En general, siempre quiero eso, salvo que sea problematico por algun motivo. Creo que no deberia haber problema en usarlo siempre.

import json
import random
import os
import datetime
import readchar

# Cargar preguntas
with open("temario-completo.json", encoding="utf-8") as f:
    preguntas = json.load(f)

# Obtener libros únicos
libros_disponibles = sorted(set(p["libro"] for p in preguntas))

# Menú inicial con readchar
print("\n--- Selecciona un modo de entrenamiento ---")
print("1. Modo libre")
print("2. Modo por libro")
print("3. Test corto")
print("4. Test completo")
print("Presiona una tecla (1-4) o 'x' para salir")

modo = readchar.readkey()

if modo == "1":
    preguntas_seleccionadas = random.sample(preguntas, len(preguntas))

elif modo == "2":
    print("\nLibros disponibles:")
    for i, libro in enumerate(libros_disponibles):
        print(f"{i + 1}. {libro}")
    try:
        indice = int(input("\nSelecciona un libro: ").strip()) - 1
        libro_elegido = libros_disponibles[indice]
        preguntas_seleccionadas = [p for p in preguntas if p["libro"] == libro_elegido]
        random.shuffle(preguntas_seleccionadas)
    except:
        print("Selección inválida. Saliendo.")
        exit()

elif modo == "3":
    print("\n📌 El modo 'Test corto' está en construcción.")
    exit()

elif modo == "4":
    print("\n📌 El modo 'Test completo' está en construcción.")
    exit()

else:
    print("\nOpción no válida. Saliendo.")
    exit()

resumen_errores = []

print("\n--- Entrenamiento iniciado. Presiona 1-4 para responder, 'x' para salir. ---\n")

for item in preguntas_seleccionadas:
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

    print("\nSelecciona una opción (1-4) o 'x' para salir:")
    while True:
        key = readchar.readkey()
        if key in ['1', '2', '3', '4']:
            indice_usuario = int(key) - 1
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
            break
        elif key.lower() == 'x':
            print("\nSesión interrumpida por el usuario.")
            break
        else:
            print("Entrada inválida. Presiona 1-4 o 'x'.")

    if key.lower() == 'x':
        break

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