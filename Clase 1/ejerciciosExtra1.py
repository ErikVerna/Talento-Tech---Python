"""
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""
print("Ejercicio 1:")
print("Hola Mundo!")

"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
"""
print("Ejercicio 2:")
hola_Mundo = "Hola Mundo!"
print(hola_Mundo)

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""
print("Ejercicio 3:")
nombre = input("Introduce tu nombre: ")
print("Hola," , nombre + "!")


"""
Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((3+2) / (2*5))**2
"""
print("Ejercicio 4:")
resultado = ((3+2) / (2*5))**2
print(resultado)

"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
print("Ejercicio 5:")
horas_trabajadas = float(input("Introduce las horas trabajadas: "))
costeHora = float(input("Introduce el coste por hora: "))
paga = horas_trabajadas*costeHora
print("La paga correspondiente es: $", paga)

