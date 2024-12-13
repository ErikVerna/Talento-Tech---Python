"""
Desarrollá un programa que permita calcular el promedio de ventas
de la tienda. Para esto:

- Creá una función que reciba como párametro una lista de ventas diarias y
devuelva el promedio de esas ventas.

- Con una función, solicitá a la persona que ingrese las ventas de cada dia durante
la cantidad de dias que elija el usuario.

Usá las funciones para calcular y mostrar el promedio de ventas al finalizar.
"""

def calculo_promedio(ventas = []):
    promedio = 0
    ventas_totales = 0
    for venta in ventas:
        ventas_totales += venta
    cantidad_ventas = len(ventas)
    promedio = ventas_totales / cantidad_ventas
    return promedio

def usuario_ventas(dias):
    ventas = []
    for _ in range(dias):
        ventas_dia = float(input("Ingrese las ventas del dia: "))
        ventas.append(ventas_dia)
    return ventas

while True:
    print("Si desea salir de la aplicación, ingrese como valor 00")
    dias = int(input("¿Cuantos dias desea calcular?: "))
    if dias == 00:
        print("FIN DE PROGRAMA \n ¡Gracias por utilizar la aplicación!")
        break
    else:
        ventas_totales = usuario_ventas(dias)
        promedio = calculo_promedio(ventas_totales)
        print(f"El promedio de {dias} dias es: {promedio:.2f}")