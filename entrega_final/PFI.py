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
        '''
    )

#Alta de productos
def agregar_producto(nombre, descripcion, categoria, cantidad, precio):
        print(f"Usted ha seleccionado la opcion:  \n \n ## ALTA DE PRODUCTOS ##")
        producto = [nombre, descripcion, categoria, cantidad, precio]
        conexion = sqlite3.connect("./base-datos.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)", producto)
        conexion.commit()
        print("################### PRODUCTO AÑADIDO EXITOSAMENTE: ##############################")
        print("########-- ALTA DE PRODUCTOS --########")
        print(f"{id:<10} | {producto["nombre"]:<20} | {producto["descripcion"]:<20} | {producto["categoria"]:<20} | {producto["cantidad"]:<20} | {producto["precio"]:<20}")
        conexion.close()

def listar_productos(productos = 0):
    if productos == 0:
        conexion = sqlite3.connect("./base-datos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        print(resultados)
        for prod in resultados:
            print(f"{"ID":<10} | {prod["nombre"]:<20} | {prod["descripcion"]:<20} | {prod["categoria"]:<20} | {prod["cantidad"]:<20} | {prod["precio"]:<20}")
            conexion.close()
        else:
            for prod in productos:
                print(f"{"ID":<10} | {prod["nombre"]:<20} | {prod["descripcion"]:<20} | {prod["categoria"]:<20} | {prod["cantidad"]:<20} | {prod["precio"]:<20}")


def actualizar_producto():
    listar_productos()
    id = 0
    while id <= 0:
        try:
            id = int(input("# Ingrese el codigo del producto que desea modificar: "))
            if id <= 0:
                print("DATO INVALIDO ❌. Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero: ")
            id = 0
    nombre = input("# Ingrese un nuevo nombre para el producto: ")
    descripcion = input("# Ingrese la nueva descripcion para el producto: ")
    categoria = input("# Ingrese la nueva descripcion para el producto: ")
    cantidad = 0
    while cantidad < 0:
        try:
            cantidad = int(input("# Ingrese el nuevo precio del producto: "))
            if  cantidad <= 0:
                print("DATO INVALIDO ❌. Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero: ")
            cantidad = 0
    precio = 0
    while precio < 0:
        try:
            cantidad = int(input("# Ingrese el nuevo precio del producto: "))
            if precio <= 0:
                print("DATO INVALIDO ❌. Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero: ")
            cantidad = 0
    conexion = sqlite3.connect("./base-datos.db")
    cursor = conexion.cursor()
    query = f"UPDATE FROM productos SET nombre = {nombre}, descripcion = {descripcion}, categoria = {categoria}, cantidad = {cantidad}, precio = {precio} WHERE id = {id} "
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    listar_productos()


