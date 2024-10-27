"""
Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. El dueño te pide que
escribas un programa que verifique si hay stock suficiente de un videojuego y, si no hay, que avise que hay
que reponerlo.

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad,
mostrar si se necesita hacer un nuevo pedido o no.
"""
print("##################-Ejercicio 1-##########################")

nombre_juego = input("Ingrese el nombre del juego: ")
stock_juego = int(input("Ingrese la cantidad en stock: "))

if stock_juego > 0:
    print(f"{nombre_juego} - Disponible")
else:
    print(f"{nombre_juego} - Reponer Stock")

print("############################################")