"""
Desarrollá una función que calcule la suma de los números naturales hasta un número dado utilizando un bucle for. La suma
de los números naturales hasta el numero n se define como la suma de todos los numeros enteros positivos desde 1 hasta n.
Por ejemplo, la suma de los numeros naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.
La función debe recibir un numero entero n y devolver la suma de los numeros naturales hasta n.

TIPS: ¡Usa range()!
"""

numero = int(input("Ingrese un numero en representación de 'n': "))
suma = 0

for num in range(numero):
    suma = suma + (num + 1) 
print(f"La suma total es de: {suma}")
