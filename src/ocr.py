import requests

URL = "https://api.ocr.space/parse/image"


def leer_imagen(api_key, ruta_imagen):

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
        print("\n================ OCR =================")
        print(datos)
        print("======================================\n")

        if datos["IsErroredOnProcessing"]:
            return ""

        if "ParsedResults" not in datos:
            return ""

        if len(datos["ParsedResults"]) == 0:
            return ""

        return datos["ParsedResults"][0].get("ParsedText", "")

    except Exception as e:
        print("ERROR OCR:", e)
        return ""
