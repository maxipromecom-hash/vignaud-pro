from src.ocr import leer_imagen
import customtkinter as ctk
from tkinter import filedialog
import os

imagenes_analizadas = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ===============================
# EXAMINAR CARPETA
# ===============================
def examinar(carpeta_entry, contador_label, consola):

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

    imagenes = [
        f for f in os.listdir(carpeta)
        if f.lower().endswith(extensiones)
    ]
    global imagenes_analizadas
    imagenes_analizadas.clear()

    contador_label.configure(
        text=f"Imágenes encontradas: {len(imagenes)}"
    )

    consola.insert(
        "end",
        f"\nCarpeta seleccionada:\n{carpeta}\n"
    )

    consola.insert(
        "end",
        f"Se encontraron {len(imagenes)} imágenes.\n"
    )

    consola.see("end")


# ===============================
# ANALIZAR
# ===============================
def analizar(api_entry, carpeta_entry, progreso, consola, ventana):
    api = api_entry.get().strip()

    if api == "":
        consola.insert(
            "end",
            "\nDebe ingresar una API OCR.\n"
        )
        consola.see("end")
        return

    carpeta = carpeta_entry.get().strip()

    if carpeta == "":
        consola.insert(
            "end",
            "\nDebe seleccionar una carpeta primero.\n"
        )
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
        f for f in os.listdir(carpeta)
        if f.lower().endswith(extensiones)
    ]

    total = len(imagenes)

    if total == 0:
        consola.insert(
            "end",
            "\nNo se encontraron imágenes.\n"
        )
        consola.see("end")
        return

    progreso.set(0)

    consola.insert(
        "end",
        "\n========== INICIANDO ANÁLISIS ==========\n\n"
    )

    for i, imagen in enumerate(imagenes, start=1):

        progreso.set(i / total)
        ruta = os.path.join(carpeta, imagen)

        texto = leer_imagen(api, ruta)
                    

        consola.insert(
            "end",
            f"[{i}/{total}] Analizando: {imagen}\n"
        )
        imagenes_analizadas.append({
            "archivo": imagen,
            "ruta": os.path.join(carpeta, imagen),
            "texto": texto,
            "nuevo_nombre": ""
        })
        consola.insert(
            "end",
            f"[{i}/{total}] {imagen}\n"
        )

        if texto:
            consola.insert(
                "end",
                f"Texto: {texto[:120]}\n\n"
            )

        else:
            consola.insert(
                "end",
                "Sin texto reconocido.\n\n"
            )
        
       

        consola.see("end")
        ventana.update()

consola.insert(
"end",
f"\nSe almacenaron {len(imagenes_analizadas)} imágenes para OCR.\n"
)
consola.insert(
"end",
"\nAnálisis finalizado correctamente.\n"
)
    
consola.see("end")


# ===============================
# VENTANA PRINCIPAL
# ===============================
def crear_ventana():

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

    # API

    api_label = ctk.CTkLabel(
        ventana,
        text="API OCR"
    )
    api_label.pack(anchor="w", padx=20)

    api_entry = ctk.CTkEntry(
        ventana,
        width=850,
        placeholder_text="Ingrese aquí su API OCR..."
    )
    api_entry.pack(padx=20, pady=(0, 15))

    # Carpeta

    carpeta_label = ctk.CTkLabel(
        ventana,
        text="Carpeta de imágenes"
    )
    carpeta_label.pack(anchor="w", padx=20)

    marco = ctk.CTkFrame(ventana)
    marco.pack(fill="x", padx=20)

    carpeta = ctk.CTkEntry(
        marco,
        width=700,
        placeholder_text="Seleccione una carpeta..."
    )

    carpeta.pack(
        side="left",
        padx=10,
        pady=10
    )

    contador = ctk.CTkLabel(
        ventana,
        text="Imágenes encontradas: 0",
        font=("Segoe UI", 15)
    )

    consola = ctk.CTkTextbox(
        ventana,
        width=850,
        height=220
    )

    progreso = ctk.CTkProgressBar(
        ventana,
        width=850
    )

    progreso.set(0)

    boton_examinar = ctk.CTkButton(
        marco,
        text="Examinar",
        command=lambda: examinar(
            carpeta,
            contador,
            consola
        )
    )

    boton_examinar.pack(
        side="right",
        padx=10
    )

    contador.pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    progreso.pack(padx=20)

    consola.pack(
        padx=20,
        pady=20
    )

    consola.insert(
        "end",
        "Vignaud PRO iniciado correctamente...\n"
    )

    consola.insert(
        "end",
        "Esperando selección de carpeta...\n"
    )

    botones = ctk.CTkFrame(
        ventana
    )

    botones.pack(pady=10)

    boton_analizar = ctk.CTkButton(
        botones,
        text="Analizar",
        width=180,
        command=lambda: analizar(
            api_entry,
            carpeta,
            progreso,
            consola,
            ventana
        )
    )

    boton_analizar.pack(
        side="left",
        padx=20
    )

    boton_renombrar = ctk.CTkButton(
        botones,
        text="Renombrar",
        width=180
    )

    boton_renombrar.pack(
        side="left",
        padx=20
    )

    ventana.mainloop()
