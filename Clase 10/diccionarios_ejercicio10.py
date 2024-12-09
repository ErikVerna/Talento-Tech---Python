""""
## EJERCICIO EXTRA ##
Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente 
preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
(4) Listar todos los clientes, (5) Listar clientes preferentes, 
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""





def buscar_cliente(codigo = ""):
    if codigo in clientes:
        print(f"El codigo {codigo} pertenece al cliente: \n Nombre: {clientes[codigo][0]} \n Dirección: {clientes[codigo][1]} \n Telefono: {clientes[codigo][2]} \n Correo: {clientes[codigo][3]} \n Preferente: {"Si" if clientes[codigo][4] == True else "No"}")
    else:
        print("El cliente no existe o se ingresó un codigo erroneo \n")

def listar_clientes(clientes = []):
    if len(clientes) > 0:
        print(f"{"Codigo":<10} | {"Nombre":<20} | {"Direccion":<20} | {"Telefono":<20} | {"Mail":<20} | {"Preferencial":<20}")
        print(f"{"-"*120}")
        for codigo,usuario in clientes.items():
            print(f"{codigo:<10} | {usuario[0]:<20} | {usuario[1]:<20} | {usuario[2]:<20} | {usuario[3]:<20} | {"Si" if usuario[4] == True else "No"}")
    else:
        print("LISTA DE CLIENTES VACIA")

def listar_clientes_preferentes(clientes = []):
    if len(clientes) > 0:
        print("\n --- LISTA DE USUARIOS PREFERENTES ---")
        print(f"{"Codigo":<10} | {"Nombre":<20} | {"Direccion":<20} | {"Telefono":<20} | {"Mail":<20} | {"Preferencial":<20}")
        print(f"{"-"*120}")
        for codigo,usuario in clientes.items():
            if usuario[4] == True:
                print(f"{codigo:<10} | {usuario[0]:<20} | {usuario[1]:<20} | {usuario[2]:<20} | {usuario[3]:<20} | {"Si" if usuario[4] == True else "No"}")
    else:
        print("LISTA DE CLIENTES VACIA")

clientes = {
    "cliente01" : ["Nicolas", "Capital federal", "1111111111", "ejemplo@gmail.com", True],
    "cliente02":["Juan Carlos", "Capital federal", "1111111111", "ejemplo@gmail.com", False]
}

control_menu = True

while control_menu:
    opcion = int(input("(1) - Añadir cliente\n(2) - Eliminar cliente\n(3) - Mostrar cliente\n(4) - Listar todos los clientes\n(5) - Listar clientes preferentes\n(6) - Terminar \n Ingrese una opcion: "))
    if  opcion == 1:
        codigo = input("Ingrese el codigo del cliente: ").lower()
        if codigo in clientes:
            print("CODIGO EXISTENTE!")
            buscar_cliente(codigo)
        else:
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la direccion del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            preferente = input("Ingrese 'si' para el cliente preferente o 'no' en caso contrario: ").lower()
            while preferente != "si" and preferente != "no":
                preferente = input("Error, ingrese 'si' o 'no'").lower()
            if preferente == "si":
                preferente = True
            else: 
                preferente = False
            clientes[codigo] = [nombre, direccion, telefono, correo, preferente]
    elif opcion == 2:
        codigo = input("Ingrese el codigo del cliente a eliminar: ").lower()
        if codigo in clientes:
            cliente_eliminado = clientes.pop(codigo)
            print(f"El cliente con el codigo {codigo} a sido eliminado de la base de datos.")
            print(f"DATOS DEL cliente ELIMINADO: \n Nombre:{cliente_eliminado[0]} \n Dirección:{cliente_eliminado[1]} \n Telefono:{cliente_eliminado[2]} \n Correo:{cliente_eliminado[3]}")
        else:
            print("El codigo del cliente no existe")
    elif opcion == 3:
        codigo = input("Ingrese el codigo para buscar el cliente: ")
        buscar_cliente(codigo)
    elif opcion == 4:
        listar_clientes(clientes)
    elif opcion == 5:
        listar_clientes_preferentes(clientes)
    elif opcion == 6:
        print("FIN DE PROGRAMA \n Gracias por utilizar la aplicación.")
        control_menu = False
    else:
        print("OPCION NO DISPONIBLE, INTRODUZCA UN VALOR NUMERICO DEL 1-9")