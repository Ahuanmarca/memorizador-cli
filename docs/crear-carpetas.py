import os

carpetas = [
    "01-CondicionesGenerales",
    "02-NormativaComercial",
    "03-PasesInternacionales",
    "04-PlanDelIgualdadDeGenero",
    "05-CulturaDeSeguridad",
    "06-ExperienciaDeCliente"
]

for carpeta in carpetas:
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"Creada: {carpeta}")
    else:
        print(f"Ya existe: {carpeta}")

    # Crear .gitkeep dentro de cada carpeta
    ruta_gitkeep = os.path.join(carpeta, ".gitkeep")
    if not os.path.exists(ruta_gitkeep):
        with open(ruta_gitkeep, "w") as f:
            pass  # crea un archivo vacío
        print(f"  → .gitkeep creado en {carpeta}")
