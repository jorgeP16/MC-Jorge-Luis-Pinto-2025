def es_valido_base8(numero):
    for digito in numero:
        if digito not in "01234567":
            return False
    return True

def convertir_base8_a_base10(numero_base8):
    numero_base8 = numero_base8[::-1] 
    numero_base10 = 0
    for i, digito in enumerate(numero_base8):
        numero_base10 += int(digito) * (8 ** i)
    return numero_base10

numero_base8 = input("Introduce un número en base 8: ")

if not es_valido_base8(numero_base8):
    print("El número introducido no es válido en base 8.")
else:
    numero_base10 = convertir_base8_a_base10(numero_base8)
    print(f"El número {numero_base8} en base 8 es: {numero_base10} en base 10.")
