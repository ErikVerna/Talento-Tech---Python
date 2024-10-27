
"""
Ejercicio 2: Ingreso promedio
Escribir un programa que guarde en variables elmonto del ingreso de cada uno de los primeros 6
meses del año.

Luego, calcular y guardar en otra variable el promedio de esos valores.

Por último, mostrar una leyenda que diga “Elingreso promedio en el semestre es de xxxxx”, donde “xxxxx” es el valor calculado.
"""

print()
print("**********")

en, feb, mar, abr, may, jun = 20000, 15000, 32000, 45000, 18000, 45000

promedio = (en + feb + mar + may + jun) / 6

print("Resolución Ejercicio 2:")
print("El ingreso promedio en el semestre es de $", round(promedio))