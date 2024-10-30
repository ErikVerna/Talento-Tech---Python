"""
Ejercicio 2:
Escribí un programa que permita al usuario ingresar el precio de un producto, pero que solo acepte valores
mayores a 0. Si el usuario ingresa un valor invalido (negativo o cero), el programa debe mostrar un mensaje de error, 
y volver a pedir el valor hasta que se ingrese uno valido
"""

precio = 0

while precio <= 0:
    precio = int(input("Ingrese el precio del producto: $"))
    if precio <= 0:
        print("ERROR! - Solamente se permiten valores mayores a 0!")