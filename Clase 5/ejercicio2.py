"""
Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de
artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes
reglas:

Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000,
aplica un descuento del 15%.

Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento
del 10%.

Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.

Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier
descuento o simplemente el monto original si no hay descuento.
"""

print("##################-Ejercicio 2-##########################")
monto_total = int(input("Ingrese el monto total: $"))
cantidad_articulo = int(input("Ingrese la cantidad de articulos: "))
descuento = 0
descuento_aplicado = 0
monto_final = 0

print("\n###-Ticket-####")

if cantidad_articulo >= 5 and monto_total > 10000:
    descuento = 15
    descuento_aplicado = monto_total * (descuento / 100)
    monto_final = monto_total - descuento_aplicado
    print(f"El monto de la compra es de ${monto_final}. Se aplico un descuento del {descuento}%")
elif cantidad_articulo < 5 and cantidad_articulo >= 3:
    descuento = 10
    descuento_aplicado = monto_total * (descuento / 100)
    monto_final = monto_total - descuento_aplicado
    print(f"El monto de la compra es de ${monto_final}. Se aplico un descuento del {descuento}%")
else:
    print(f"El monto de la compra es de ${monto_total:.2f}.")