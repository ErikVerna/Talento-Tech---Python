import sqlite3
import os

#Mensaje de bienvenida al programa
def log_inicial():
    print("░  ░░░░░░░░      ░░░      ░░        ░░      ░░        ░        ░░      ░░░      ░░░░░░░  ░░░░  ░  ░░░░  ░       ░░  ░░░░  ░  ░░░░░░░        ░")
    print("▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒  ▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒")
    print("▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓  ▓▓▓   ▓▓▓▓  ▓▓▓▓▓      ▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓        ▓▓▓    ▓▓▓       ▓▓  ▓▓▓▓  ▓  ▓▓▓▓▓▓▓      ▓▓▓")
    print("█  ███████  ████  █  ████  ████  ██████████  ████  ███████  ████  ████  █        ██████  ████  ████  ████  ███  ██  ████  █  ███████  ███████")
    print("█        ██      ███      ██        ██      █████  ████        ██      ██  ████  ██████  ████  ████  ████  ████  ██      ██        █        █")
    print("\n Bienvenido al programa de 'Logistica Hyrule' 😇, utilice nuestro menú para seleccionar la opción que requiera:")


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

#Alta de productos
def agregar_producto():
    print("Usted ha seleccionado la opción: 1 \n \n ## ALTA DE PRODUCTOS ##")
    
    # Solicitar datos del producto al usuario
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    descripcion = input("Ingrese una descripción del producto: ").strip().capitalize()
    categoria = input("Ingrese la categoría del producto: ").strip().capitalize()
    
    # Validar que cantidad sea un número entero no negativo
    cantidad = -1
    while cantidad < 0:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("DATO INVÁLIDO ❌. La cantidad debe ser mayor o igual a 0.")
        except ValueError:
            print("DATO INVÁLIDO ❌. Ingrese un número entero.")
    
    # Validar que precio sea un número entero no negativo
    precio = -1
    while precio < 0:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio < 0:
                print("DATO INVÁLIDO ❌. El precio debe ser mayor o igual a 0.")
        except ValueError:
            print("DATO INVÁLIDO ❌. Ingrese un número entero.")
    
    # Crear el diccionario del producto
    producto = [nombre, descripcion, categoria, cantidad, precio]
    
    # Agregar el producto a la base de datos
    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        # Verificar si el nombre ya existe
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        existente = cursor.fetchone()
        if existente:
            print(f"Error: Ya existe un producto con el nombre '{nombre}'.")
            return  # Salir de la función si el producto ya existe
        
        # Insertar el producto si no existe
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)", 
            producto
        )
        conexion.commit()
        nuevo_id = cursor.lastrowid
        print("################### PRODUCTO AÑADIDO EXITOSAMENTE: ##############################")
        print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
        print(f"{nuevo_id:<10} | {nombre:<20} | {descripcion:<20} | {categoria:<20} | {cantidad:<10} | {precio:<10}")


#Mostrar todos los productos
def listar_productos(productos=0):
    print("Usted ha seleccionado la opción: 2 \n \n ## LISTA DE PRODUCTOS ##")
    print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
    print("-" * 90)
    if productos == 0:
        with sqlite3.connect(DB_PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            resultados = cursor.fetchall()
            for prod in resultados:
                print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")
    else:
        for prod in productos:
            print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")

def listar_productos(productos=0):
    print("Usted ha seleccionado la opción: 2 \n \n ## LISTA DE PRODUCTOS ##")
    print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
    print("-" * 90)
    if productos == 0:
        with sqlite3.connect(DB_PATH) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            resultados = cursor.fetchall()
            if len(resultados) == 0:
                print("✅ No hay productos registrados en la base de datos.")
            else:
                for prod in resultados:
                    print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")
    else:
        if len(productos) == 0:
            print("✅ No hay productos para mostrar.")
        else:
            for prod in productos:
                print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")



#Actualizar producto
def actualizar_producto():
    print("Usted ha seleccionado la opción: 3 \n \n ## ACTUALIZAR PRODUCTO ##")
    listar_productos()
    id_producto = 0
    while id_producto <= 0:
        try:
            id_producto = int(input("# Ingrese el código del producto que desea modificar: "))
            if id_producto <= 0:
                print("DATO INVÁLIDO ❌. Ingrese un número mayor que 0.")
        except ValueError:
            print("Ingrese un número válido.")
            id_producto = 0

    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM productos WHERE id = ?", (id_producto,))
        if cursor.fetchone()[0] == 0:
            print(f"No existe ningún producto con el ID {id_producto}.")
            return

    nombre = input("# Ingrese un nuevo nombre para el producto: ").capitalize()
    descripcion = input("# Ingrese la nueva descripción para el producto: ").capitalize()
    categoria = input("# Ingrese la nueva categoría para el producto: ").capitalize()

    cantidad = -1
    while cantidad < 0:
        try:
            cantidad = int(input("# Ingrese la nueva cantidad del producto: "))
            if cantidad < 0:
                print("DATO INVÁLIDO ❌. Ingrese un número mayor o igual a 0.")
        except ValueError:
            print("Ingrese un número válido.")
            cantidad = -1

    precio = -1
    while precio < 0:
        try:
            precio = int(input("# Ingrese el nuevo precio del producto: $"))
            if precio < 0:
                print("DATO INVÁLIDO ❌. Ingrese un número mayor o igual a 0.")
        except ValueError:
            print("Ingrese un número válido.")
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
        print(f"El producto con ID {id_producto} ha sido actualizado exitosamente.")

#Baja de Producto
def baja_producto():
    print("Usted ha seleccionado la opción: 4 \n \n ## BAJA DE PRODUCTO ##")
    listar_productos()
    id_producto = 0
    while id_producto <= 0:
        try:
            id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
            if id_producto <= 0:
                print("❌ DATO INVÁLIDO. Ingrese un número mayor que 0.")
        except ValueError:
            print("❌ DATO INVÁLIDO. Ingrese un número valido.")
            id_producto = 0
    
    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto))
        producto = cursor.fetchone()

        if not producto:
            print(f"❌ No existe ningún producto con el ID {id_producto}.")
            return
        
        #CONFIRMAR ELIMINACIÓN
        print("\n¿Está seguro de que desea eliminar el siguiente producto?")
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Categoría: {producto[3]}, Cantidad: {producto[4]}, Precio: ${producto[5]}")
        confirmacion = input("Escriba 'SI' para confirmar la eliminación: ").strip().upper()

        if confirmacion == "SI":
            print("")
#Busqueda por producto
def busqueda_producto():
    print("Usted ha seleccionado la opción: 5 \n \n ## LISTA DE PRODUCTOS ##")
#Lista de productos con cantidad baja
def listar_bajo_stock():
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad mínima permitida: "))
            if cantidad <= 0:
                print("❌ Ingrese un número mayor que 0.")
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número válido.")
            cantidad = 0

    print("\n## Productos con cantidad baja ##")
    print(f"{'ID':<10} | {'Nombre':<20} | {'Descripción':<20} | {'Categoría':<20} | {'Cantidad':<10} | {'Precio ($)':<10}")
    print("-" * 90)

    with sqlite3.connect(DB_PATH) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (cantidad,))
        productos_bajo_stock = cursor.fetchall()
        
        if len(productos_bajo_stock) == 0:
            print("✅ No hay productos con cantidad por debajo del mínimo especificado.")
        else:
            for prod in productos_bajo_stock:
                print(f"{prod[0]:<10} | {prod[1]:<20} | {prod[2]:<20} | {prod[3]:<20} | {prod[4]:<10} | {prod[5]:<10}")


#Menu
def menu():
    init_tabla_db()
    while True:
        print("#####################################################")
        print(":::::::::::-- Menu de Gestion de Productos --::::::::::: \n 1. Alta de productos nuevos ⬆️ ")
        print(" 2. Listado completo de productos 📋 \n 3. Modificar un producto 🔄️")
        print(" 4. Dar de baja un producto ⬇️ \n 5. Busqueda por producto 🔍")
        print(" 6. Lista de productos con cantidad baja ⚠️ \n 7. Salir 🏃‍♂️")
        print(" ======================***********==============================")
        try:
            opcion = int(input("Seleccione una opción (1-7): "))
            
            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                listar_productos()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                baja_producto()
            elif opcion == 5:
                busqueda_producto()
            elif opcion == 6:
                listar_bajo_stock()  
            elif opcion == 7:
                print("¡Gracias por usar el sistema! Saliendo...")
                break  # Salir del menú
            else:
                print("❌ Opción inválida. Por favor, seleccione un número entre 1 y 4.")
        
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingrese un número entre 1 y 4.")


menu()