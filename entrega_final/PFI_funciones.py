import sqlite3
import os
from colorama import init,Fore,Back

#Se inicia colorama en autoreset = True para evitar que se coloree todo el terminal del mismo color.
init(autoreset=True)

#Mensaje de bienvenida al programa
def log_inicial():
    print(Fore.BLUE + "░  ░░░░░░░░      ░░░      ░░        ░░      ░░        ░        ░░      ░░░      ░░░░░░░  ░░░░  ░  ░░░░  ░       ░░  ░░░░  ░  ░░░░░░░        ░")
    print(Fore.CYAN + "▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒")
    print(Fore.BLUE + "▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓  ▓▓▓   ▓▓▓▓  ▓▓▓▓▓      ▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓        ▓▓▓    ▓▓▓       ▓▓  ▓▓▓▓  ▓  ▓▓▓▓▓▓▓      ▓▓▓")
    print(Fore.CYAN + "█  ███████  ████  █  ████  ████  ██████████  ████  ███████  ████  ████  █        ██████  ████  ████  ████  ███  ██  ████  █  ███████  ███████")
    print(Fore.BLUE + "█        ██      ███      ██        ██      █████  ████        ██      ██  ████  ██████  ████  ████  ████  ████  ██      ██        █        █")
    print(Fore.GREEN + "\n Bienvenido al programa de 'Logistica Hyrule' 😇, utilice nuestro menú para seleccionar la opción que requiera:")

#Ruta de acceso a la db
DB_PATH = os.path.join("db", "inventario.db")

#Si no existe la carpeta, se crea
os.makedirs("db", exist_ok=True)

#Crear tabla en la db si no existe
def init_tabla_db():
    with sqlite3.connect(DB_PATH) as conexion:
        conexion.execute('''
            CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            descripcion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio INTEGER NOT NULL
            )
        ''')      

#Alta de productos (Opcion 1)
def agregar_producto():    
    # Solicitar datos del producto al usuario
    nombre = input("# Ingrese el nombre del producto: ").strip().capitalize()
    descripcion = input("# Ingrese una descripción del producto: ").strip().capitalize()
    categoria = input("# Ingrese la categoría del producto: ").strip().capitalize()
    
    # Validar que cantidad sea un número entero no negativo
    cantidad = -1
    while cantidad < 0:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print(Fore.RED + "DATO INVÁLIDO ❌. La cantidad debe ser mayor o igual a 0.")
        except ValueError:
            print(Fore.RED + "DATO INVÁLIDO ❌. Ingrese un número entero.")
    
    # Validar que precio sea un número entero no negativo
    precio = -1
    while precio < 0:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio < 0:
                print(Fore.RED + "DATO INVÁLIDO ❌. El precio debe ser mayor o igual a 0.")
        except ValueError:
            print(Fore.RED + "DATO INVÁLIDO ❌. Ingrese un número entero.")
    
    # Creamos el diccionario del producto
    producto = [nombre, descripcion, categoria, cantidad, precio]
    
    # Agregar el producto a la base de datos
    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        # Verificar si el nombre ya existe
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        existente = cursor.fetchone()
        if existente:
            print(Fore.RED + f"🚫 Error: Ya existe un producto con el nombre '{nombre}'.")
            return  # Sale de la función si el producto ya existe.
        
        # Insertar el producto si no existe
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)", 
            producto
        )
        conexion.commit()
        nuevo_id = cursor.lastrowid
        print(Fore.GREEN + "################### PRODUCTO AÑADIDO EXITOSAMENTE: ##############################")
        print(Fore.LIGHTMAGENTA_EX + f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
        print(f"{nuevo_id:<10} | {nombre:<20} | {descripcion:<20} | {categoria:<20} | {cantidad:<10} | {precio:<10}")


#Listar todos los productos (Opcion 2)
def listar_productos(productos = 0):
    print(Fore.LIGHTMAGENTA_EX + f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
    print("-" * 120)
    if productos == 0:
        with sqlite3.connect(DB_PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            resultados = cursor.fetchall()
            if len(resultados) == 0:
                print(Fore.RED + "🚫 No hay productos registrados en la base de datos.")
            else:
                for prod in resultados:
                    print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")
    else:
        if len(productos) == 0:
            print(Fore.RED + "🚫 No hay productos para mostrar.")
        else:
            for prod in productos:
                print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")

#Actualizar producto (Opcion 3)
def modificar_producto():
    listar_productos()
    id_producto = 0
    while id_producto <= 0:
        try:
            id_producto = int(input("# Ingrese el código del producto que desea modificar: "))
            if id_producto <= 0:
                print(Fore.RED + "DATO INVÁLIDO ❌. Ingrese un número mayor que 0.")
        except ValueError:
            print(Fore.RED + "❌ - Ingrese un número válido.")
            id_producto = 0

    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM productos WHERE id = ?", (id_producto,))
        if cursor.fetchone()[0] == 0:
            print(Fore.RED + f"❌ - No existe ningún producto con el ID {id_producto}.")
            return

    nombre = input("# Ingrese un nuevo nombre para el producto: ").capitalize()
    descripcion = input("# Ingrese la nueva descripción para el producto: ").capitalize()
    categoria = input("# Ingrese la nueva categoría para el producto: ").capitalize()

    cantidad = -1
    while cantidad < 0:
        try:
            cantidad = int(input("# Ingrese la nueva cantidad del producto: "))
            if cantidad < 0:
                print(Fore.RED + "DATO INVÁLIDO ❌. Ingrese un número mayor o igual a 0.")
        except ValueError:
            print(Fore.RED + "❌ - Ingrese un número válido.")
            cantidad = -1

    precio = -1
    while precio < 0:
        try:
            precio = int(input("# Ingrese el nuevo precio del producto: $"))
            if precio < 0:
                print(Fore.RED + "DATO INVÁLIDO ❌. Ingrese un número mayor o igual a 0.")
        except ValueError:
            print(Fore.RED + "❌ - Ingrese un número válido.")
            precio = -1

    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        query = """
            UPDATE productos 
            SET nombre = ?, descripcion = ?, categoria = ?, cantidad = ?, precio = ? 
            WHERE id = ?
        """
        cursor.execute(query, (nombre, descripcion, categoria, cantidad, precio, id_producto))
        conexion.commit()
        print(Fore.GREEN + f"El producto con ID {id_producto} ha sido actualizado exitosamente.")

#Baja de Producto (Opcion 4)
def baja_producto():
    listar_productos()
    id_producto = 0
    while id_producto <= 0:
        try:
            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
            if id_producto <= 0:
                print(Fore.RED + "❌ DATO INVÁLIDO. Ingrese un número mayor que 0.")
        except ValueError:
            print(Fore.RED + "❌ DATO INVÁLIDO. Ingrese un número valido.")
            id_producto = 0
    
    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.RED + f" ❌ No existe ningún producto con el ID {id_producto}.")
            return
        
        #CONFIRMAR ELIMINACIÓN
        print(Back.LIGHTRED_EX + Fore.WHITE + "\n¿Está seguro de que desea eliminar el siguiente producto?")
        print(Fore.LIGHTBLACK_EX + "#" * 70 + "\n")
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Categoría: {producto[3]}, Cantidad: {producto[4]}, Precio: ${producto[5]} \n")
        print(Fore.LIGHTBLACK_EX + "#" * 70)
        confirmacion = input("Escriba 'SI' para confirmar la eliminación: ").strip().upper()

        if confirmacion == "SI":
            #Eliminamos el producto de la db despues de la confirmación del usuario:
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            print(Fore.LIGHTRED_EX + "## EL PRODUCTO FUE ELIMINADO DE LA BASE DE DATOS EXITOSAMENTE ✅ ##")

#Busqueda por producto (Opcion 5)
def busqueda_producto():
    #Iniciamos submenu para buscar por distintos criterios
    while True:
        print(Fore.GREEN + "\nSeleccione el tipo de búsqueda que desea realizar:")
        print("1. 🔍  Buscar por ID")
        print("2. 🔍  Buscar por Nombre")
        print("3. 🔍  Buscar por Categoría")
        print("4. ⬅️  Volver al menú principal")
        
        try:
            opcion = int(input(Fore.CYAN + "Seleccione una opción (1-4): "))
        except ValueError:
            print(Fore.RED + "❌ DATO INVÁLIDO. Ingrese un número entre 1 y 4.")
            continue
        
        #Busqueda por ID
        if opcion == 1:
            try:
                id_producto = int(input("Ingrese el ID del producto a buscar: "))
                if id_producto <= 0:
                    print(Fore.RED + f" ❌ DATO INVÁLIDO. El ID debe ser un numero mayor que 0 {id_producto}.")
                    continue
            except ValueError:
                (Fore.RED + "❌ DATO INVÁLIDO. Ingrese un número valido.")
                continue
            with sqlite3.connect(DB_PATH) as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
                producto = cursor.fetchone()
                if producto:
                    print("\n## Producto encontrado ✅ ##")
                    print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
                    print("-" * 90)
                    print(f"{producto[0]:<10} | {producto[1]:<20} | {producto[2]:<20} | {producto[3]:<20} | {producto[4]:<10} | {producto[5]:<10}")
                else:
                    print(Fore.RED + f"❌ No se encontró ningún producto con el ID {id_producto}.")
        
        #Busqueda por Nombre
        elif opcion == 2:
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            with sqlite3.connect(DB_PATH) as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre_producto}%",))
                resultados = cursor.fetchall()
                if resultados:
                    print("\n## Productos encontrados ✅ ##")
                    print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
                    print("-" * 90)
                    for prod in resultados:
                        print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")
                else:
                    print(Fore.RED + f"❌ No se encontraron productos con el nombre '{nombre_producto}'.")

        #Busqueda por Categoria
        elif opcion == 3:
            categoria_producto = input("Ingrese la categoria del producto a buscar: ")
            with sqlite3.connect(DB_PATH) as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM productos WHERE categoria LIKE ?", (f"%{categoria_producto}%",))
                resultados = cursor.fetchall()
                if resultados:
                    print("\n## Productos encontrados ✅ ##")
                    print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
                    print("-" * 90)
                    for prod in resultados:
                        print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")
                else:
                    print(Fore.RED + f"❌ No se encontraron productos con el nombre '{categoria_producto}'.")

        # Volver al menú principal
        elif opcion == 4:
            print(Fore.LIGHTCYAN_EX + "Regresando al menú principal...")
            break
        
        else:
            print(Fore.RED + "❌ Opción inválida. Por favor, seleccione un número entre 1 y 4.")

#Lista de productos con stock bajo (Opcion 6)
def listar_bajo_stock():
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad mínima permitida: "))
            if cantidad <= 0:
                print(Fore.RED + "❌ Ingrese un número mayor que 0.")
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Ingrese un número válido.")
            cantidad = 0

    print(Fore.YELLOW + "\n##########################  Productos con cantidad baja ##############################")
    print(Fore.LIGHTMAGENTA_EX + f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
    print("-" * 120)

    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (cantidad,))
        productos_bajo_stock = cursor.fetchall()
        
        if len(productos_bajo_stock) == 0:
            print(Fore.RED + "🚫 No hay productos con cantidad por debajo del mínimo especificado.")
        else:
            for prod in productos_bajo_stock:
                print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")


#Menu
def menu():
    init_tabla_db()
    while True:
        print(Fore.BLUE + "#" * 120)
        print(Fore.LIGHTGREEN_EX + ":::::::::::-- Menu de Gestion de Productos --:::::::::::")
        print(" 1. ⬆️  Alta de productos nuevos")
        print(" 2. 📋 Listado completo de productos  \n 3. 🔄️ Modificar un producto ")
        print(" 4. ⬇️  Dar de baja un producto  \n 5. 🔍 Busqueda por producto ")
        print(" 6. ⚠️  Lista de productos con cantidad baja")
        print(Fore.LIGHTRED_EX + " 7. 🏃‍♂️ Salir")
        print(Fore.BLUE + "#" * 120)
        try:
            opcion = int(input(Fore.CYAN + "Seleccione una opción (1-7): "))
            if opcion == 1:
                print(Fore.LIGHTYELLOW_EX + f"Usted ha seleccionado la opción: {opcion} \n \n ## ALTA DE PRODUCTOS ##")
                agregar_producto()
            elif opcion == 2:
                print(Fore.LIGHTYELLOW_EX + f"Usted ha seleccionado la opción: {opcion} \n \n ## LISTA DE PRODUCTOS ##")
                listar_productos()
            elif opcion == 3:
                print(Fore.LIGHTYELLOW_EX + f"Usted ha seleccionado la opción: {opcion} \n \n ## MODIFICAR PRODUCTO ##")
                modificar_producto()
            elif opcion == 4:
                print(Fore.LIGHTYELLOW_EX + f"Usted ha seleccionado la opción: {opcion} \n \n ## BAJA DE PRODUCTO ##")
                baja_producto()
            elif opcion == 5:
                print(Fore.LIGHTYELLOW_EX + f"Usted ha seleccionado la opción: {opcion} \n \n ## BUSQUEDA DE PRODUCTO(S) ##")
                busqueda_producto()
                
            elif opcion == 6:
                print(Fore.LIGHTYELLOW_EX + f"Usted ha seleccionado la opción: {opcion} \n \n ## PRODUCTOS CON BAJO STOCK! ##")
                listar_bajo_stock()  
            elif opcion == 7:
                print(Fore.LIGHTMAGENTA_EX + " \n ¡Gracias por usar el sistema! Saliendo... 👋")
                break  # Salir del menú
            else:
                print(Fore.RED + "❌ Entrada no válida. Por favor, ingrese un número entre 1 y 7.")
        except ValueError:
            print(Fore.RED + "❌ Entrada no válida. Por favor, ingrese un número entre 1 y 7.")