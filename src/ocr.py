import requests


URL = "https://api.ocr.space/parse/image"


def leer_imagen(ruta_imagen, api_key):

    try:

        with open(ruta_imagen, "rb") as archivo:

            respuesta = requests.post(
                URL,
                files={
                    "filename": archivo
                },
                data={
                    "apikey": api_key,
                    "language": "spa",
                    "OCREngine": 2
                }
            )

        datos = respuesta.json()

        if datos["IsErroredOnProcessing"]:

            return ""

        return datos["ParsedResults"][0]["ParsedText"]

    except Exception:

        return ""
