"""
Ejercicio 3:
Escribí un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares
desde 1 hasta ese numero separados por comas menos el ultimo numero, que debera ir sin coma.
"""

condicion = True
numero = 0
indice = 1

while condicion:
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero > 0:
        condicion = False
        resultado = numero % 2
        if resultado == 1:
            numero = numero - 1
        while indice != numero:
            resultado2 = indice % 2
            if resultado2 == 1:
                print(indice, ", ")
                
            indice = indice + 1
        print(numero)
    else:
        print("ERROR: Ingresaste un numero negativo o igual a 0.")