import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def crear_ventana():

    ventana = ctk.CTk()

    ventana.title("Vignaud PRO 2.0")

    ventana.geometry("900x600")

    titulo = ctk.CTkLabel(
        ventana,
        text="VIGNAUD PRO 2.0",
        font=("Segoe UI", 28, "bold")
    )

    titulo.pack(pady=25)

    estado = ctk.CTkLabel(
        ventana,
        text="Versión 0.1.0 Foundation",
        font=("Segoe UI", 16)
    )

    estado.pack()

    boton = ctk.CTkButton(
        ventana,
        text="Salir",
        command=ventana.destroy
    )

    boton.pack(pady=40)

    ventana.mainloop()
