print("=" * 50)
print("RENOMBRADOR VIGNAUD PRO")
print("=" * 50)

print("¡Hola Mundo!")

input("Presione ENTER para finalizar...")
import os

VERSION = "0.1"

api_key = ""

carpeta = ""

imagenes = []


def limpiar():

    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():

    limpiar()

    print("=" * 58)
    print("              VIGNAUD PRO 2.0")
    print(" Sistema Inteligente de Renombrado de Fotografías")
    print("=" * 58)

    print()

    print("Estado del sistema")

    if api_key == "":
        print("OCR...............NO CONFIGURADO")
    else:
        print("OCR...............CONFIGURADO")

    if carpeta == "":
        print("Carpeta..........NO SELECCIONADA")
    else:
        print("Carpeta..........OK")

    print(f"Imágenes.........{len(imagenes)}")

    print()

    print("-" * 58)

    print("1 - Configurar API OCR")
    print("2 - Seleccionar carpeta")
    print("3 - Buscar imágenes")
    print("4 - Procesar imágenes")
    print("5 - Salir")

    print("-" * 58)


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        api_key = input("\nIngrese la API KEY de OCR.Space:\n")

        print("\nAPI guardada correctamente.")

        input("\nENTER para continuar...")

    elif opcion == "2":

        carpeta = input("\nIngrese la carpeta:\n")

        input("\nENTER para continuar...")

    elif opcion == "3":

        if carpeta == "":

            print("\nPrimero seleccione una carpeta.")

            input("\nENTER...")

            continue

        imagenes = []

        print("\nBuscando imágenes...")

        extensiones = (".jpg", ".jpeg", ".png", ".bmp")

        try:

            for archivo in os.listdir(carpeta):

                if archivo.lower().endswith(extensiones):

                    imagenes.append(archivo)

            print()

            print("Imágenes encontradas:", len(imagenes))

        except:

            print()

            print("La carpeta no existe.")

        input("\nENTER para continuar...")

    elif opcion == "4":

        if len(imagenes) == 0:

            print("\nNo hay imágenes para procesar.")

            input("\nENTER...")

            continue

        print()

        print("Procesamiento iniciado...")

        contador = 1

        for imagen in imagenes:

            print(f"[{contador}/{len(imagenes)}] {imagen}")

            contador += 1

        print()

        print("Proceso finalizado.")

        input("\nENTER para continuar...")

    elif opcion == "5":

        print("\nHasta luego.")

        break

    else:

        print("\nOpción incorrecta.")

        input("\nENTER...")
