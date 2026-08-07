import re


# ============================================================
# MARCAS CONOCIDAS
# ============================================================

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
    "MOTO MEL"
]


# ============================================================
# BUSCAR MARCA
# ============================================================

def buscar_marca(texto):

    texto = texto.upper()

    for marca in MARCAS:

        if marca in texto:
            return marca.replace(" ", "")

    return "SINMARCA"


# ============================================================
# BUSCAR MODELO
# ============================================================

def buscar_modelo(texto):

    texto = texto.upper()

    patron = r"\b(50|70|90|100|110|125|135|150|180|200|250|300|400|600|650|1000)\b"

    encontrado = re.search(patron, texto)

    if encontrado:
        return encontrado.group(1)

    return ""


# ============================================================
# BUSCAR DOMINIO
# ============================================================

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


# ============================================================
# BUSCAR REGISTRO
# ============================================================

def buscar_expediente(texto):

    if not texto:
        return ""

    texto = texto.upper()

    # --------------------------------------------------------
    # NORMALIZAMOS ALGUNOS ERRORES FRECUENTES DEL OCR
    # --------------------------------------------------------

    texto = texto.replace("R°", "R")
    texto = texto.replace("Rº", "R")

    # --------------------------------------------------------
    # PATRÓN PRINCIPAL
    #
    # Acepta:
    #
    # R 1234/26
    # R-1234/26
    # R1234/26
    # R-1234-26
    # R 1234 / 26
    # R - 1234 / 26
    # R.1234/26
    #
    # También permite números de hasta 6 dígitos.
    # --------------------------------------------------------

    patron = (
        r"\bR\s*[-.:_]?\s*"
        r"(\d{1,6})"
        r"\s*[/\\-]\s*"
        r"(\d{2})\b"
    )

    encontrado = re.search(patron, texto)

    if encontrado:

        numero = encontrado.group(1)
        año = encontrado.group(2)

        return f"R-{numero}-{año}"

    # --------------------------------------------------------
    # SEGUNDA BÚSQUEDA
    #
    # OCR puede confundir:
    #
    # O -> 0
    # I -> 1
    # l -> 1
    #
    # Por eso buscamos una versión más flexible.
    # --------------------------------------------------------

    patron_ocr = (
        r"\bR\s*[-.:_]?\s*"
        r"([0-9OIL]{1,6})"
        r"\s*[/\\-]\s*"
        r"([0-9OIL]{2})\b"
    )

    encontrado = re.search(patron_ocr, texto)

    if encontrado:

        numero = encontrado.group(1)
        año = encontrado.group(2)

        # ----------------------------------------------------
        # CORREGIR ERRORES OCR
        # ----------------------------------------------------

        numero = (
            numero
            .replace("O", "0")
            .replace("I", "1")
            .replace("L", "1")
        )

        año = (
            año
            .replace("O", "0")
            .replace("I", "1")
            .replace("L", "1")
        )

        return f"R-{numero}-{año}"

    return ""

# ============================================================
# GENERAR NOMBRE
# ============================================================

def generar_nombre(texto):

    if not texto:
        return "SIN_IDENTIFICAR"

    # --------------------------------------------------------
    # PRIMERO BUSCAMOS EL REGISTRO
    #
    # Esto es importante.
    #
    # El Registro tiene prioridad sobre el modelo.
    # --------------------------------------------------------

    expediente = buscar_expediente(texto)

    # --------------------------------------------------------
    # Después buscamos el resto de la información.
    # --------------------------------------------------------

    marca = buscar_marca(texto)

    modelo = buscar_modelo(texto)

    dominio = buscar_dominio(texto)

    partes = []

    # --------------------------------------------------------
    # MARCA
    # --------------------------------------------------------

    if marca != "SINMARCA":
        partes.append(marca)

    # --------------------------------------------------------
    # MODELO
    # --------------------------------------------------------

    if modelo:
        partes.append(modelo)

    # --------------------------------------------------------
    # DOMINIO
    # --------------------------------------------------------

    if dominio:
        partes.append(dominio)

    # --------------------------------------------------------
    # REGISTRO
    #
    # Siempre al final.
    # --------------------------------------------------------

    if expediente:
        partes.append(expediente)

    # --------------------------------------------------------
    # SI NO ENCONTRÓ NADA
    # --------------------------------------------------------

    if len(partes) == 0:
        return "SIN_IDENTIFICAR"

    return "_".join(partes)
