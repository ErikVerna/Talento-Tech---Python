#Registro de Inventario en Lista
inventario = []

while True:
#Mostrar el listado
    print(":::::::::::-- Menu de Gestion de Productos --::::::::::: \n 1. Alta de productos nuevos")
    print(" 2. Consulta de datos de productos \n 3. Modificar la cantidad de stock")
    print(" 4. Dar de baja un producto \n 5. Listado completo de productos")
    print(" 6. Lista de producto con cantidad baja \n 7. Salir")
    print(" ======================***********==============================")
    usuario_input = int(input("Ingrese la opción deseada (1-7): "))  
#Salir
    if usuario_input == 7:
        print(f"Usted selecciono la opcion: {usuario_input}")
        print("Fin del programa")
        break
#Alta de productos
    elif usuario_input == 1:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
        alta_producto = input("Ingrese el producto: ").lower()
        cantidad_stock = int(input("Ingrese la cantidad del producto: "))
        inventario.append(alta_producto)
        inventario.append(cantidad_stock)
#Consulta de datos de procutos
    elif usuario_input == 2:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
        print("########-- LISTA DE PRODUCTOS --########")
        i = 0
        while i < len(inventario):
            print(inventario[i])
            i = i + 1
#Modificar la cantidad de Stock
    elif usuario_input == 3:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
#Dar de baja un producto
    elif usuario_input == 4:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
#Listado completo de productos
    elif usuario_input == 5:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
#Lista de producto con cantidad baja
    elif usuario_input == 6:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
