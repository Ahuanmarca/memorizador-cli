import json
import random
import os
import datetime
import readchar

# Colores ANSI para CLI (modo oscuro)
RESET = "\033[0m"
GREEN = "\033[92m"  # Verde brillante
RED = "\033[91m"  # Rojo brillante

# Cargar preguntas
with open("temario-completo.json", encoding="utf-8") as f:
    preguntas = json.load(f)

# Obtener libros únicos
libros_disponibles = []
for p in preguntas:
    libro = p["libro"]
    if libro not in libros_disponibles:
        libros_disponibles.append(libro)

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
    print("\nPresiona una tecla correspondiente al libro (1-9) o 'x' para salir")
    while True:
        key = readchar.readkey()
        if key.lower() == "x":
            print("\nSesión cancelada.")
            exit()
        if key.isdigit():
            indice = int(key) - 1
            if 0 <= indice < len(libros_disponibles):
                libro_elegido = libros_disponibles[indice]
                preguntas_seleccionadas = [
                    p for p in preguntas if p["libro"] == libro_elegido
                ]
                random.shuffle(preguntas_seleccionadas)
                break
            else:
                print("\nÍndice fuera de rango. Intenta de nuevo.")
        else:
            print("Entrada inválida. Presiona un número válido o 'x'.")

elif modo == "3":
    preguntas_por_libro = (
        ("Condiciones Generales", 5),
        ("Normativa Comercial", 3),
        ("Pases Internacionales", 2),
        ("Plan de Igualdad de Género", 4),
        ("Cultura de Seguridad", 3),
        ("Experiencia de Usuario", 3),
    )

    preguntas_seleccionadas = []
    for nombre_libro, cantidad in preguntas_por_libro:
        preguntas_libro = [p for p in preguntas if p["libro"] == nombre_libro]
        seleccionadas = random.sample(
            preguntas_libro, min(cantidad, len(preguntas_libro))
        )
        preguntas_seleccionadas.extend(seleccionadas)

elif modo == "4":
    preguntas_por_libro = (
        ("Condiciones Generales", 15),
        ("Normativa Comercial", 9),
        ("Pases Internacionales", 6),
        ("Plan de Igualdad de Género", 12),
        ("Cultura de Seguridad", 9),
        ("Experiencia de Usuario", 9),
    )

    preguntas_seleccionadas = []
    for nombre_libro, cantidad in preguntas_por_libro:
        preguntas_libro = [p for p in preguntas if p["libro"] == nombre_libro]
        seleccionadas = random.sample(
            preguntas_libro, min(cantidad, len(preguntas_libro))
        )
        preguntas_seleccionadas.extend(seleccionadas)

else:
    print("\nOpción no válida. Saliendo.")
    exit()

resumen_errores = []

print(
    "\n--- Entrenamiento iniciado. Presiona 1-4 para responder, 'x' para salir. ---\n"
)

for item in preguntas_seleccionadas:
    formulacion = random.choice(item["formulaciones"])
    modo = formulacion["modo"]
    tipo = formulacion["tipo"]
    pregunta = formulacion["texto"]

    correctas = item["respuestas_correctas"]
    incorrectas = item["respuestas_incorrectas"]
    opciones = []
    respuesta_correcta = ""

    todas_texto = "Todas las anteriores son correctas."

    if modo == "una_correcta" and tipo == "positiva":
        respuesta_correcta = random.choice(correctas)
        opciones = [respuesta_correcta] + random.sample(incorrectas, 3)

        # Posibilidad de incluir "Todas las anteriores son correctas" como distractor
        if random.random() < 0.25 and todas_texto not in opciones:
            # Reemplazar una incorrecta por el distractor, que irá como última opción
            opciones = opciones[:3] + [todas_texto]

        else:
            opciones = random.sample(opciones, 4)  # Asegurar mezcla

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

    # Reordenar opciones dejando "Todas las anteriores son correctas." en posición 4 si existe
    if todas_texto in opciones:
        opciones = [opt for opt in opciones if opt != todas_texto]
        opciones = random.sample(opciones, 3) + [todas_texto]
    else:
        random.shuffle(opciones)

    # random.shuffle(opciones)

    print(f"\n{pregunta}\n")
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

    print("\nSelecciona una opción (1-4) o 'x' para salir:")
    while True:
        key = readchar.readkey()
        if key in ["1", "2", "3", "4"]:
            indice_usuario = int(key) - 1
            ahora = datetime.datetime.now().isoformat()
            item["veces_vista"] += 1
            item["ultima_vez_vista"] = ahora

            print("")
            for i, opcion in enumerate(opciones):
                if i == indice_usuario and opciones[i] == respuesta_correcta:
                    print(f"{GREEN}{i+1}. {opcion}{RESET}")
                elif i == indice_usuario:
                    print(f"{RED}{i+1}. {opcion}{RESET}")
                elif opciones[i] == respuesta_correcta:
                    print(f"{GREEN}{i+1}. {opcion}{RESET}")
                else:
                    print(f"{i+1}. {opcion}")

            if opciones[indice_usuario] == respuesta_correcta:
                print("✅ ¡Correcto!\n")
                item["aciertos_consecutivos"] += 1
                item["ultima_vez_acertada"] = ahora
            else:
                print("❌ Incorrecto.\n")
                item["aciertos_consecutivos"] = 0
                item["fallos_totales"] += 1
                resumen_errores.append(
                    {
                        "pregunta": pregunta,
                        "respuesta_usuario": opciones[indice_usuario],
                        "respuesta_correcta": respuesta_correcta,
                        "fragmento": item["fragmento_original"],
                    }
                )
            break
        elif key.lower() == "x":
            print("\nSesión interrumpida por el usuario.")
            break
        else:
            print("Entrada inválida. Presiona 1-4 o 'x'.")

    if key.lower() == "x":
        break

# Guardar archivo actualizado
with open("temario-completo.json", "w", encoding="utf-8") as f:
    json.dump(preguntas, f, indent=2, ensure_ascii=False)

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
