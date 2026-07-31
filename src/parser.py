import re


# Marcas conocidas
MARCAS = [
    "HONDA",
    "YAMAHA",
    "MOTOMEL",
    "MONDIAL",
    "CORVEN",
    "KELLER",
    "GILERA",
    "ZANELLA",
    "JINCHENG",
    "BRAVA",
    "GUERRERO",
    "KAWASAKI",
    "SUZUKI",
    "BAJAJ",
    "KYMCO",
    "CERRO",
    "APPIA",
    "MAVERICK",
    "KELLER",
    "MOTO MEL"
]


def buscar_marca(texto):

    texto = texto.upper()

    for marca in MARCAS:

        if marca in texto:
            return marca.replace(" ", "")

    return "SINMARCA"


def buscar_modelo(texto):

    texto = texto.upper()

    patron = r"\b(50|70|90|100|110|125|135|150|180|200|250|300|400|600|650|1000)\b"

    encontrado = re.search(patron, texto)

    if encontrado:
        return encontrado.group(1)

    return ""


def buscar_dominio(texto):

    texto = texto.upper()

    # Dominio nuevo
    patron1 = r"\b[A-Z]{2}[0-9]{3}[A-Z]{2}\b"

    # Dominio viejo
    patron2 = r"\b[A-Z]{3}[0-9]{3}\b"

    dominio = re.search(patron1, texto)

    if dominio:
        return dominio.group(0)

    dominio = re.search(patron2, texto)

    if dominio:
        return dominio.group(0)

    if "S/DOMINIO" in texto:
        return "SDOMINIO"

    if "SIN DOMINIO" in texto:
        return "SDOMINIO"

    return ""


def buscar_expediente(texto):

    texto = texto.upper()

    patron = r"[A-Z]-\d+/\d+"

    encontrado = re.search(patron, texto)

    if encontrado:
        return encontrado.group(0).replace("/", "-")

    return ""


def generar_nombre(texto):

    marca = buscar_marca(texto)

    modelo = buscar_modelo(texto)

    dominio = buscar_dominio(texto)

    expediente = buscar_expediente(texto)

    partes = []

    if marca != "SINMARCA":
        partes.append(marca)

    if modelo:
        partes.append(modelo)

    if dominio:
        partes.append(dominio)

    if expediente:
        partes.append(expediente)

    if len(partes) == 0:
        return "SIN_IDENTIFICAR"

    return "_".join(partes)
