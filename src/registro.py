import re


def obtener_registro(texto):

    texto = texto.upper()

    patron = re.compile(
        r'R[\s\-\.:]*([0-9]{3,6})\s*/\s*([0-9]{2})'
    )

    m = patron.search(texto)

    if m:

        numero = m.group(1)

        anio = m.group(2)

        return f"R{numero}-{anio}"

    return ""
