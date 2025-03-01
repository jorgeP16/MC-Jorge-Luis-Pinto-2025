def to_bin_list(n):
    if n < 0:
        n = (1 << 16) + n  
    return [int(bit) for bit in format(n, '016b')] 

def from_bin_list(bin_list):
    bin_str = ''.join(map(str, bin_list))  
    if bin_list[0] == 1:  
        return int(bin_str, 2) - (1 << 16)
    else:
        return int(bin_str, 2)  

def suma_complemento_a_dos(num1, num2):
    bin_num1 = to_bin_list(num1)
    bin_num2 = to_bin_list(num2)
    suma = (int(''.join(map(str, bin_num1)), 2) + int(''.join(map(str, bin_num2)), 2)) % (1 << 16)
    suma_bin_list = to_bin_list(suma)
    return from_bin_list(suma_bin_list)
try:
    num1 = input("Introduce el primer número entero entre -32,768 y 32,767: ")

    if num1.lstrip('-').isdigit():
        num1 = int(num1)
    else:
        raise ValueError("Por favor, introduce un número entero válido.")

    num2 = input("Introduce el segundo número entero entre -32,768 y 32,767: ")

    if num2.lstrip('-').isdigit():
        num2 = int(num2)
    else:
        raise ValueError("Por favor, introduce un número entero válido.")

    if -32768 <= num1 <= 32767 and -32768 <= num2 <= 32767:
        resultado = suma_complemento_a_dos(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    else:
        print("Los números deben estar en el rango entre -32,768 y 32,767.")
except ValueError as e:
    print(e)
