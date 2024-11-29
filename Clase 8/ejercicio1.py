"""
En una tienda, es necesario actualizar el inventario cuando se venden productos. A continuación, te proporcionamos
un arreglo con una lista de produuctos, donde cada producto tieene un codigo, una descripción y una cantidad en stock.
Escribi un programa que permita:
- Seleccionar un producto a partir de su codigo
- Ingresar la cantidad vendida (que debe ser mayor que cero).
- Actualizar la cantidad en stock de ese producto restando la cantidad vendida.

El arreglo de productos disponibles es el que ves a continuación:
["P001", "Manzanas", 50],
["P002", "Peras", 40],
["P001", "Bananas", 30],
["P001", "Naranjas", 60]

El script que tenes que hacer debe modificar la cantidad en stock de acuerdo a cada venta realizada. Si la cantidad
vendida es mayor que la cantidad disponible en stock, el programa debe mostrar un mensaje de error.
"""

inventario = [
["P001", "Manzanas", 50],
["P002", "Peras", 40],
["P003", "Bananas", 30],
["P004", "Naranjas", 60]
]

activo = True

while activo:
    indice = 0
    producto_encontrado = False
    while indice < len(inventario):
        print(f"Codigo: {inventario[indice][0]} |  Nombre: {inventario[indice][1]} | Cantidad: {inventario[indice][2]}")
        indice += 1
    selector = input("Ingrese el codigo del producto o escriba 'salir' para finalizar el: ").upper()
    indice = 0
    while indice < len(inventario):
        if selector == inventario[indice][0]:
            cantidad_vendida = int(input("Ingrese la cantidad vendida del producto: "))
            if cantidad_vendida <= 0 or cantidad_vendida > inventario[indice][2]:
                print(f"La cantidad vendida no puede ser 0 o mayor que la cantidad disponible ({inventario[indice][2]}) \n")
                activo = False
            else:
                inventario[indice][2] = inventario[indice][2]  - cantidad_vendida
                print(f"La cantidad actual del producto {inventario[indice][1]} es de {inventario[indice][2]} \n")
                producto_encontrado = True
                indice = len(inventario)
        else:
            indice += 1
    if producto_encontrado == False:
        print("El codigo ingresado no existe en la base de datos.")
