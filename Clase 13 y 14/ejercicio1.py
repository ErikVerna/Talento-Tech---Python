"""
Crea un programa en Python que inserte varios registros en la
tabla Personas usando una lista de tuplas predefinida. Cada tupla
debe contener un nombre, una edad y una ciudad.

Usá un bucle para recorrer la lista e insertar cada persona
en la base de datos. La lista debe tener al menos cinco
personas nuevas y al finalizar el programa deben mostrarse todos los registros
en la tabla Personas.
"""

import sqlite3



conexion = sqlite3.connect("base-de-datos.db")
cursor = conexion.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Personas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        ciudad TEXT NOT NULL
    )
    '''
)

nuevas_personas = [
    ("Esteban", 32, "Mar del Plata"),
    ("Valeria", 27, "Bahia Blanca"),
    ("Fernando", 41, "Rosario"),
    ("Carolina", 29, "La Plata"),
    ("Juan", 35, "Cordoba")
]


for persona in nuevas_personas:
    cursor.execute(f"INSERT INTO Personas (nombre, edad, ciudad) VALUES ('{persona[0]}', {persona[1]}, '{persona[2]}')")
    conexion.commit()
    
cursor.execute("SELECT * FROM Personas")
resultados = cursor.fetchall()

for registro in resultados:
    print("ID:", registro[0], "|", "Nombre:", registro[1], "|" , "Edad:", registro[2], "|",  "Ciudad:", registro[3]) 
