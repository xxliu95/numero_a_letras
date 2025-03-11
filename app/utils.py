from num2words import num2words

def numero_a_letras(numero):
    numero = str(numero)
    if "." in numero:
        entero, decimal = numero.split(".")
        entero_letras = num2words(int(entero), lang="es")
        decimal_letras = " ".join(num2words(int(digito), lang="es") for digito in decimal)
        return f"{entero_letras} con {decimal_letras}"
    else:
        return num2words(int(numero), lang="es")
