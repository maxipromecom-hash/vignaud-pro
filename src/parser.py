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

    texto = texto.upper()

    # --------------------------------------------------------
    # Acepta:
    #
    # R 1234/26
    # R-1234/26
    # R1234/26
    # r-1234/26
    # R-1234/25
    #
    # También acepta espacios alrededor.
    # --------------------------------------------------------

    patron = r"\bR\s*[-]?\s*(\d{1,6})\s*[/\-]\s*(\d{2})\b"

    encontrado = re.search(patron, texto)

    if encontrado:

        numero = encontrado.group(1)
        año = encontrado.group(2)

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
