import os

for nombre in os.listdir("temario"):
    if nombre.endswith(".json"):
        ruta = os.path.join("temario", nombre)
        with open(ruta, "r+", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                f.seek(0)
                f.write("[]")
                f.truncate()
