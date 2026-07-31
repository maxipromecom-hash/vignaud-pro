import customtkinter as ctk
from tkinter import filedialog
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def examinar(carpeta_entry, contador_label, consola):
    def analizar(carpeta_entry, progreso, consola):

    carpeta = carpeta_entry.get().strip()

    if not carpeta:
        consola.insert("end", "\nNo hay una carpeta seleccionada.\n")
        consola.see("end")
        return

    extensiones = (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".tif",
        ".tiff"
    )

    imagenes = [
        archivo
        for archivo in os.listdir(carpeta)
        if archivo.lower().endswith(extensiones)
    ]

    total = len(imagenes)

    if total == 0:
        consola.insert("end", "\nNo se encontraron imágenes.\n")
        consola.see("end")
        return

    progreso.set(0)

    consola.insert("end", "\n===== INICIANDO ANÁLISIS =====\n")

    for i, imagen in enumerate(imagenes, start=1):

        porcentaje = i / total
        progreso.set(porcentaje)

        consola.insert(
            "end",
            f"[{i}/{total}] {imagen}\n"
        )

        consola.see("end")
        ventana.update()

    consola.insert(
        "end",
        "\nAnálisis finalizado correctamente.\n"
    )

    consola.see("end")

    carpeta = filedialog.askdirectory()

    if not carpeta:
        return

    carpeta_entry.delete(0, "end")
    carpeta_entry.insert(0, carpeta)

    extensiones = (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".tif",
        ".tiff"
    )

    cantidad = 0

    for archivo in os.listdir(carpeta):

        if archivo.lower().endswith(extensiones):
            cantidad += 1

    contador_label.configure(
        text=f"Imágenes encontradas: {cantidad}"
    )

    consola.insert(
        "end",
        f"\nCarpeta seleccionada:\n{carpeta}\n"
    )

    consola.insert(
        "end",
        f"Se encontraron {cantidad} imágenes.\n"
    )

    consola.see("end")


def crear_ventana():
    global ventana
    ventana = ctk.CTk()

    ventana.title("Vignaud PRO 2.0")
    ventana.geometry("900x650")
    ventana.resizable(False, False)

    titulo = ctk.CTkLabel(
        ventana,
        text="VIGNAUD PRO 2.0",
        font=("Segoe UI", 30, "bold")
    )
    titulo.pack(pady=(20, 10))

    # ----- API -----
    api_label = ctk.CTkLabel(ventana, text="API OCR")
    api_label.pack(anchor="w", padx=20)

    api_entry = ctk.CTkEntry(
        ventana,
        width=850,
        placeholder_text="Ingrese aquí su API OCR..."
    )
    api_entry.pack(padx=20, pady=(0, 15))

    # ----- Carpeta -----
    carpeta_label = ctk.CTkLabel(ventana, text="Carpeta de imágenes")
    carpeta_label.pack(anchor="w", padx=20)

    marco = ctk.CTkFrame(ventana)
    marco.pack(fill="x", padx=20)

    carpeta = ctk.CTkEntry(
        marco,
        width=700,
        placeholder_text="Seleccione una carpeta..."
    )
    carpeta.pack(side="left", padx=10, pady=10)

    boton_examinar = ctk.CTkButton(
    marco,
    text="Examinar",
    command=lambda: examinar(
        carpeta,
        contador,
        consola
    )
)
    
    boton_examinar.pack(side="right", padx=10)

    # ----- Contador -----
    contador = ctk.CTkLabel(
        ventana,
        text="Imágenes encontradas: 0",
        font=("Segoe UI", 15)
    )
    contador.pack(anchor="w", padx=20, pady=(20, 5))

    # ----- Barra de progreso -----
    progreso = ctk.CTkProgressBar(ventana, width=850)
    progreso.pack(padx=20)
    progreso.set(0)

    # ----- Consola -----
    consola = ctk.CTkTextbox(
        ventana,
        width=850,
        height=220
    )
    consola.pack(padx=20, pady=20)

    consola.insert("end", "Vignaud PRO iniciado correctamente...\n")
    consola.insert("end", "Esperando selección de carpeta...\n")

    # ----- Botones -----
    botones = ctk.CTkFrame(ventana)
    botones.pack(pady=10)

    analizar = ctk.CTkButton(
    botones,
    text="Analizar",
    width=180,
    command=lambda: analizar(
        carpeta,
        progreso,
        consola
    )
)
    analizar.pack(side="left", padx=20)

    renombrar = ctk.CTkButton(
        botones,
        text="Renombrar",
        width=180
    )
    renombrar.pack(side="left", padx=20)

    ventana.mainloop()
