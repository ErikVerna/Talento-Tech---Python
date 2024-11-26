"""
El inventario de una tienda esta almacenando en un diccionario, donde las claves son los nombres de los productos y los valores son las
cantidades disponibles en stock.
Creá un programa que:

- Te permita ingresar el nombre de un producto.
- Utilice el metodo .get() para buscar el stock disponible. Si el producto no existe,
deberá mostrar un mensaje diciendo "Producto no encontrado".
- Si el producto esta disponible, mostrará cuantas unidades quedan en stock.
"""

productos = {
    "manzanas": 50,
    "naranjas": 30,
    "peras": 25
}

mensaje = "PRODUCTO NO ENCONTRADO!"

while True:
    producto = input("Ingrese el nombre del producto o escriba 'salir' si desea finalizar el programa: ").lower()

    if producto == "salir":
        break
    else:
        dato = productos.get(producto, mensaje)
        if dato == mensaje:
            print(mensaje)
        else:
            print(f"La cantidad de {producto} es: {dato}")