#Mensaje de bienvenida al programa
print("░  ░░░░░░░░      ░░░      ░░        ░░      ░░        ░        ░░      ░░░      ░░░░░░░  ░░░░  ░  ░░░░  ░       ░░  ░░░░  ░  ░░░░░░░        ░")
print("▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒")
print("▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓  ▓▓▓   ▓▓▓▓  ▓▓▓▓▓      ▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓        ▓▓▓    ▓▓▓       ▓▓  ▓▓▓▓  ▓  ▓▓▓▓▓▓▓      ▓▓▓")
print("█  ███████  ████  █  ████  ████  ██████████  ████  ███████  ████  ████  █        ██████  ████  ████  ████  ███  ██  ████  █  ███████  ███████")
print("█        ██      ███      ██        ██      █████  ████        ██      ██  ████  ██████  ████  ████  ████  ████  ██      ██        █        █")
print("\n Bienvenido al programa de 'Logistica Hyrule' 😇, utilice nuestro menú para seleccionar la opción que requiera:")
#Registro de Inventario en Lista
inventario = []

#Menu
while True:
    print(":::::::::::-- Menu de Gestion de Productos --::::::::::: \n 1. Alta de productos nuevos ⬆️ ")
    print(" 2. Listado completo de productos 📋 \n 3. Modificar la cantidad de stock 🔄️")
    print(" 4. Dar de baja un producto ⬇️ \n 5. Busqueda por producto 🔍")
    print(" 6. Lista de productos con cantidad baja ⚠️ \n 7. Salir 🏃‍♂️")
    print(" ======================***********==============================")
    usuario_input = int(input("Ingrese la opción deseada (1-7): ")) 

#Salir
    if usuario_input == 7:
        print(f"Usted selecciono la opcion: {usuario_input}")
        print("Fin del programa. ¡Gracias por elegirnos! 👋")
        break

#Alta de productos
    elif usuario_input == 1:
        print(f"Usted ha seleccionado la opcion: {usuario_input} \n ## ALTA DE PRODUCTOS ##")
        alta_producto = input("Ingrese el producto: ").lower()
        cantidad_stock = int(input("Ingrese la cantidad del producto: "))
        inventario.append([alta_producto, cantidad_stock])
        print("#################################################")
        print("########-- ALTA DE PRODUCTOS --########")
        print(f"Producto: {alta_producto}")
        print(f"Cantidad: {cantidad_stock} \n")

#Consulta de datos de productos
    elif usuario_input == 2:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
        if len(inventario) > 0:
            print("########-- LISTA DE PRODUCTOS --########")
            for producto in inventario:
                print(f"Producto: {producto[0]}")
                print(f"Cantidad: {producto[1]}")
                print("---------------------------")
        else:
            print("##### NO HAY PRODUCTOS REGISTRADOS PARA MOSTRAR #####")
            
#Modificar la cantidad de Stock -------- PENDIENTE
    elif usuario_input == 3:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")

#Dar de baja un producto -------- PENDIENTE 
    elif usuario_input == 4:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")

#Listado completo de productos -------- PENDIENTE
    elif usuario_input == 5:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")

#Lista de producto con cantidad baja -------- PENDIENTE
    elif usuario_input == 6:
        print(f"Usted ha seleccionado la opcion: {usuario_input}")
