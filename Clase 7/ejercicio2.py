"""
Ejercicio 2: Consultar el stock de productos

Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto esta en stock.
Si el producto esta en la lista, el programa debe informarlo, sino, debe mostrar un mensaje indicando que no esta disponible.

TIPS: Usa una lista para almacenar los productos en stock.
      Permiti que el usuario ingrese el nombre de un producto a consultar.
      Recorre la lista con un bucle while para verificar si el producto esta en stock.
"""

lista_productos = ["yerba mate", "te", "manzana"]

while True:
    producto = input("Ingrese el producto a buscar o 'salir' si desea terminar el programa: ")
    if producto == "salir":
        print("Gracias por utilizar el programa!")
        break
    else:
        i = 0
        while i < len(lista_productos):
            if producto == lista_productos[i].capitalize():
                print("Producto encontrado")
                break
            else:
                i = i + 1
            if i == len(lista_productos):
                print("Producto no encontrado")