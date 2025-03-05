def convertir_a_base16(numero): 
    if numero == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"

    resultado = []

    while numero > 0:
        residuo = numero % 16
        resultado.insert(0, hex_digits[residuo])
        numero = numero // 16

    return ''.join(resultado)

numero_base10 = int(input("Introduce un número en base 10: "))
numero_base16 = convertir_a_base16(numero_base10)
print(f"El número {numero_base10} en base 16 es: {numero_base16}")
