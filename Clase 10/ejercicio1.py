"""
En un comercio, se necesita gestionar los productos y sus precios.
Desarrollá un programa que permita:
Ingresar el nombre de tres productos y su precio correspondiente,
guardandolos en un diccionario donde la clave es el nombre del producto y el valor es su precio.
Una vez ingresados, mostrará todos los productos y sus precios en pantalla.
"""

productos = {}

for i in range(3):
    nombre_producto = input("Ingrese el nombre del producto: ").lower()
    valor = float(input("Ingrese el precio del producto: $"))
    productos[nombre_producto] = valor

for prod, precio in productos.items():
    print(f"El producto {prod} tiene un precio de: ${precio}")
