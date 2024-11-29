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
["P001", "Bananas", 30],
["P001", "Naranjas", 60]
]


