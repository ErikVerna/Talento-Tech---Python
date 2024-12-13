#Mensaje de bienvenida al programa
print("░  ░░░░░░░░      ░░░      ░░        ░░      ░░        ░        ░░      ░░░      ░░░░░░░  ░░░░  ░  ░░░░  ░       ░░  ░░░░  ░  ░░░░░░░        ░")
print("▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒")
print("▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓  ▓▓▓   ▓▓▓▓  ▓▓▓▓▓      ▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓        ▓▓▓    ▓▓▓       ▓▓  ▓▓▓▓  ▓  ▓▓▓▓▓▓▓      ▓▓▓")
print("█  ███████  ████  █  ████  ████  ██████████  ████  ███████  ████  ████  █        ██████  ████  ████  ████  ███  ██  ████  █  ███████  ███████")
print("█        ██      ███      ██        ██      █████  ████        ██      ██  ████  ██████  ████  ████  ████  ████  ██      ██        █        █")
print("\n Bienvenido al programa de 'Logistica Hyrule' 😇, utilice nuestro menú para seleccionar la opción que requiera:")
#Registro de Inventario en Lista

inventario = {
    1: {"Nombre": "Laptop", "Descripcion": "Dell XPS 13", "Categoria": "Electrónica", "Cantidad": 5, "Precio": 1200},
    2: {"Nombre": "Teléfono", "Descripcion": "iPhone 13", "Categoria": "Electrónica", "Cantidad": 10, "Precio": 999}
}

#Codigo autoincremental


def alta_productos():
    codigo_producto = len(inventario) + 1
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripcion del producto: ").capitalize()
    categoria = input("Ingrese la categoria del producto: ").capitalize()
    cantidad = 0
    precio = 0.0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad <= 0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("## ERROR ##  \n - Ingrese un valor numerico")
            cantidad = 0
    while precio <= 0:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("## ERROR ##  \n - Ingrese un valor numerico")
            precio = 0
    
    inventario[codigo_producto] = {
        "Nombre": nombre,
        "Descripcion": descripcion,
        "Categoria": categoria,
        "Cantidad": cantidad,
        "Precio": precio
    }
    print("Producto agregado exitosamente!")


def mostrar_productos():
    if len(inventario) > 0:
        print("########-- LISTA DE PRODUCTOS --########")
        print(f"{"Codigo":<10} | {"Nombre":<20} | {"Descripcion":<20} | {"Categoria":<20} | {"Cantidad":<20} | {"Precio":<20}")
        print(f"{"-"*120}")
        for codigo, producto in inventario.items():
            print(f"{codigo:<10} | {producto["Nombre"]:<20} | {producto["Descripcion"]:<20} | {producto["Categoria"]:<20} | {producto["Cantidad"]:<20} | {producto["Precio"]:<20}")
                
    else:
        print("##### NO HAY PRODUCTOS REGISTRADOS PARA MOSTRAR #####")

def actualizar_producto():
    print("Los productos en el inventario son: ")
    mostrar_productos()
    codigo = 0
    while codigo <= 0:
        try:
            codigo = int(input("Ingrese el codigo del producto a modificar: "))
            if codigo <= 0:
                print("Ingrese un numero mayor a 0!")
        except ValueError:
            print("Ingrese un numero")
            codigo = 0
    resultado = inventario.get(1, "No encontrado")
    if resultado == "No encontrado":
        print("Codigo incorrecto, ningun producto con ese codigo.")
    else:
        print(f"{codigo:<10} | {resultado["Nombre"]:<20} | {resultado["Descripcion"]:<20} | {resultado["Categoria"]:<20} | {resultado["Cantidad"]:<20} | {resultado["Precio"]:<20}")
        nombre = input("Ingrese el nombre del producto: ").capitalize()
        descripcion = input("Ingrese la nueva descripcion del producto: ").capitalize()
        categoria = input("Ingrese la nueva categoria del producto: ").capitalize()
        cantidad = 0
        precio = 0.0
        while cantidad <= 0:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("## ERROR ##  \n - Ingrese un valor numerico")
                cantidad = 0
        while precio <= 0:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("## ERROR ##  \n - Ingrese un valor numerico")
                precio = 0
            inventario[codigo] = {"Nombre": nombre, "Descripcion": descripcion, "Categoria": categoria, "Cantidad": cantidad, "Precio": precio}
            print("Producto agregado exitosamente.")
            mostrar_productos()
            
            
actualizar_producto()























# #Menu
# while True:
#     print(":::::::::::-- Menu de Gestion de Productos --::::::::::: \n 1. Alta de productos nuevos ⬆️ ")
#     print(" 2. Listado completo de productos 📋 \n 3. Modificar la cantidad de stock 🔄️")
#     print(" 4. Dar de baja un producto ⬇️ \n 5. Busqueda por producto 🔍")
#     print(" 6. Lista de productos con cantidad baja ⚠️ \n 7. Salir 🏃‍♂️")
#     print(" ======================***********==============================")
#     usuario_input = int(input("Ingrese la opción deseada (1-7): ")) 

# #Salir
#     if usuario_input == 7:
#         print(f"Usted selecciono la opcion: {usuario_input}")
#         print("Fin del programa. ¡Gracias por elegirnos! 👋")
#         break

# #Alta de productos
#     elif usuario_input == 1:
#         print(f"Usted ha seleccionado la opcion: {usuario_input} \n \n ## ALTA DE PRODUCTOS ##")
#         alta_producto = input("Ingrese el producto: ").lower()
#         cantidad_stock = int(input("Ingrese la cantidad del producto: "))
#         inventario.append([alta_producto, cantidad_stock])
#         print("#################################################")
#         print("########-- ALTA DE PRODUCTOS --########")
#         print(f"Producto: {alta_producto}")
#         print(f"Cantidad: {cantidad_stock} \n")

# #Consulta de datos de productos
#     elif usuario_input == 2:
#         print(f"Usted ha seleccionado la opcion: {usuario_input} \n")
        
# #Modificar la cantidad de Stock -------- PENDIENTE
#     elif usuario_input == 3:
#         print(f"Usted ha seleccionado la opcion: {usuario_input}")
#         print(f"OPCION EN PROGRESO...")

# #Dar de baja un producto -------- PENDIENTE 
#     elif usuario_input == 4:
#         print(f"Usted ha seleccionado la opcion: {usuario_input}")
#         print(f"OPCION EN PROGRESO...")

# #Listado completo de productos -------- PENDIENTE
#     elif usuario_input == 5:
#         print(f"Usted ha seleccionado la opcion: {usuario_input}")
#         print(f"OPCION EN PROGRESO...")

# #Lista de producto con cantidad baja -------- PENDIENTE
#     elif usuario_input == 6:
#         print(f"Usted ha seleccionado la opcion: {usuario_input}")
#         print(f"OPCION EN PROGRESO...")
#     else:
#         print("OPCION NO EXISTENTE ❌")
