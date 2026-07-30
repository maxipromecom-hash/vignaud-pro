"""
===========================================================
VIGNAUD PRO 2.0
Versión: 0.1.0 Alpha
Autor: Maximiliano Rivero + ChatGPT

Sistema inteligente para renombrado de fotografías.
===========================================================
"""

import os
from pathlib import Path

# ===========================================================
# CONFIGURACIÓN
# ===========================================================

VERSION = "0.1.0 Alpha"

api_key = ""
carpeta = ""
imagenes = []

EXTENSIONES = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff"
)

# ===========================================================
# FUNCIONES
# ===========================================================

def limpiar():
    """Limpia la pantalla."""

    os.system("cls" if os.name == "nt" else "clear")


def titulo():

    print("=" * 65)
    print("                 VIGNAUD PRO 2.0")
    print("          Sistema Inteligente de Renombrado")
    print(f"                Versión {VERSION}")
    print("=" * 65)


def estado():

    print("\nESTADO DEL SISTEMA\n")

    print("OCR API ............",
          "CONFIGURADA" if api_key else "NO CONFIGURADA")

    print("Carpeta ............",
          carpeta if carpeta else "NO SELECCIONADA")

    print("Imágenes ...........",
          len(imagenes))


def menu():

    print("\n" + "-" * 65)

    print("1 - Configurar API OCR")
    print("2 - Seleccionar carpeta")
    print("3 - Buscar imágenes")
    print("4 - Procesar (Demo)")
    print("5 - Acerca de")
    print("6 - Salir")

    print("-" * 65)


def configurar_api():

    global api_key

    api_key = input("\nPegue aquí su API KEY:\n\n").strip()

    print("\nAPI guardada correctamente.")


def seleccionar_carpeta():

    global carpeta

    carpeta = input("\nIngrese la ruta de la carpeta:\n\n").strip()

    print("\nCarpeta seleccionada.")


def buscar_imagenes():

    global imagenes

    imagenes = []

    if carpeta == "":

        print("\nPrimero debe seleccionar una carpeta.")
        return

    ruta = Path(carpeta)

    if not ruta.exists():

        print("\nLa carpeta no existe.")
        return

    for archivo in ruta.iterdir():

        if archivo.suffix.lower() in EXTENSIONES:

            imagenes.append(archivo)

    print(f"\nSe encontraron {len(imagenes)} imágenes.")


def procesar_demo():

    if len(imagenes) == 0:

        print("\nNo existen imágenes para procesar.")
        return

    print()

    total = len(imagenes)

    for indice, imagen in enumerate(imagenes, start=1):

        porcentaje = int((indice / total) * 100)

        print(f"[{indice}/{total}] {imagen.name}   {porcentaje}%")

    print("\nProceso finalizado.")


def acerca_de():

    print("""
========================================================

VIGNAUD PRO 2.0

Proyecto desarrollado para automatizar el
renombrado de fotografías de vehículos.

Versión: 0.1.0 Alpha

Estado:
✔ Base creada
✔ GitHub Actions funcionando
✔ Compilación automática del EXE

========================================================
""")


# ===========================================================
# PROGRAMA PRINCIPAL
# ===========================================================

while True:

    limpiar()

    titulo()

    estado()

    menu()

    opcion = input("\nSeleccione una opción: ").strip()

    limpiar()

    titulo()

    if opcion == "1":

        configurar_api()

    elif opcion == "2":

        seleccionar_carpeta()

    elif opcion == "3":

        buscar_imagenes()

    elif opcion == "4":

        procesar_demo()

    elif opcion == "5":

        acerca_de()

    elif opcion == "6":

        print("\nHasta luego.")
        break

    else:

        print("\nOpción incorrecta.")

    input("\nPresione ENTER para continuar...")
