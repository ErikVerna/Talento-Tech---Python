"""
Ejercicio 1:
Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock
que hay de cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida
salir, ingresando "salir" como nombre de producto. Después de que el bucle termine, el programa debe mostrar la cantidad
total de productos ingresados.

TIPS: Vas a nececitar un contardor -----> Tené presente las estructuras condicionales
"""
#contador
producto = ""
contador = 0

#bucle while
while producto != "salir":
    producto = input("Bienvenido! \n Ingrese el producto deseado o escriba 'salir: ").lower()
    if producto != "salir":
        cantidad = int(input("Ingrese la cantidad en stock: "))
        contador += 1
        print("########-- ALTA DE PRODUCTOS --########")
    else:
        print(f"Gracias por utilizar el programa. Registró {contador} producto(s)")