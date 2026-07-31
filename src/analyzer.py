import os

from src.ocr import leer_imagen


def analizar_carpeta(carpeta, api_key):

    extensiones = (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".tif",
        ".tiff"
    )

    resultados = []

    for archivo in os.listdir(carpeta):

        if archivo.lower().endswith(extensiones):

            ruta = os.path.join(carpeta, archivo)

            texto = leer_imagen(
                ruta,
                api_key
            )

            resultados.append({

                "archivo": archivo,

                "ruta": ruta,

                "texto": texto

            })

    return resultados
