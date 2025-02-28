def to_bin_16bits(n):
    """Convierte un número decimal a su representación binaria de 16 bits en complemento a dos."""
    if n < 0:
        n = (1 << 16) + n  
    return format(n, '016b')  
def from_bin_16bits(b):
    """Convierte una representación binaria de 16 bits en complemento a dos a un número decimal."""
    if b[0] == '1':  
        return int(b, 2) - (1 << 16) 
    else:
        return int(b, 2)  
def suma_complemento_a_dos(num1, num2):
    """Realiza la suma de dos números enteros en complemento a dos de 16 bits."""
    bin_num1 = to_bin_16bits(num1)
    bin_num2 = to_bin_16bits(num2)
    suma_bin = bin((int(bin_num1, 2) + int(bin_num2, 2)) % (1 << 16))[2:].zfill(16) 
    return from_bin_16bits(suma_bin)
try:
    num1 = int(float(input("Introduce el primer número entero entre -32,768 y 32,767: ")))
    num2 = int(input("Introduce el segundo número entero entre -32,768 y 32,767: ").replace(',', '.'))

    if -32768 <= num1 <= 32767 and -32768 <= num2 <= 32767:
        resultado = suma_complemento_a_dos(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    else:
        print("Los números deben estar en el rango entre -32,768 y 32,767.")
except ValueError:
    print("Por favor, introduce números enteros válidos.")
