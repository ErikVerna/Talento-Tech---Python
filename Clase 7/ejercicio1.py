"""
Ejercicio 1:
Vas a implementar un sistema basico para registrar productos en el inventario de una tienda.
El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más.
Luego, deberas mostrar todos los productos ingresados al inventario

TIPS: Usa una lista para almacenar los productos. DIseña la lista pensando en el TFI
"""
condicion = True
productos = []

while condicion:
    producto = input("Ingrese un producto o escriba 'X' para terminar el programa: ").lower()
    if producto == "x":
        condicion = False
    else:
        productos.append(producto)

print(productos)