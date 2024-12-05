"""
Imaginá que en tu tienda querés implementar un sistema de descuentos automaticos. Vas a desarrollar un
programa que permita calcular el precio final de un producto despues de aplicar el descuento.

Para hacerlo:
- Crea una función que reciba como parámetros el precio original del producto y el porcentaje de descuento,
y que retorne el precio final con el descuento aplicado.

Luego, pedi que se ingrese el precio y el porcentaje de descuento.
Mostra el precio final despues de aplicar el descuento.
"""



def calcular_valor_final(precio, descuento):
    return precio - (precio * descuento / 100)

try: 
    precio = float(input("Ingrese el precio: $"))
    descuento = float(input("Ingrese el porcentaje de descuento: %"))
    precio_final = calcular_valor_final(precio, descuento)
except ValueError as e:
    print(f"ERROR {e} \n ### Por favor, ingrese un valor numerico ###")


print(f"El precio final con el descuento del {descuento}% es de: ${precio_final}")