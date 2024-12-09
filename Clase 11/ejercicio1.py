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


def solicitar_valores(mensaje):
    while True:  
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("### Por favor, ingrese un valor numérico válido ###")

#Generar inputs para precio y descuentos
precio = solicitar_valores(("Ingrese el precio: $"))
descuento = solicitar_valores(("Ingrese el porcentaje de descuento: %"))

#Calcular el precio final
precio_final = calcular_valor_final(precio, descuento)
print(f"El precio final con el descuento del {descuento}% es de: ${precio_final}")