from num2words import num2words

def numero_a_letras(numero):
    numero = str(numero)
    if "." in numero:
        entero, decimal = numero.split(".")
        entero_letras = num2words(int(entero), lang="es")
        decimal_letras = num2words(int(decimal), lang="es")
        return f"{entero_letras} con {decimal_letras}"
    else:
        return num2words(int(numero), lang="es")
