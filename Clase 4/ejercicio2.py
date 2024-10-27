#Consumo de combustible

"""
Realizar una aplicacion en Python que; A partir de la cantidad de litros de combustible que consume un coche por cada
100 km de recorrido, el costo de cada litro de combustible y la longitud del viaje realizado (en kilometros), muestra un detalle
de los litros consumidos y el dinero gastado
"""
print("###############-Ejercicio 2-####################")
consumo_litros_100km = float(input("Ingrese el consumo en litros cada 100km recorridos: "))
longitud_recorrido = float(input("Ingrese la distancia recorrida en KM: "))
precio_nafta_litro = 1080

litros_consumidos = (consumo_litros_100km * longitud_recorrido) / 100
dinero_gastado = litros_consumidos * precio_nafta_litro

print(f"Los KM recorridos fueron:{longitud_recorrido}KM \n Los litros consumidos fueron:{litros_consumidos:.2f} Litros \n Dinero gastado ${dinero_gastado}")