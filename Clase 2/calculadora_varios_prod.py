#Entrada de datos
precio_unitario = float(input("Ingrese el precio del producto: $"))
cantidad = int(input("Ingrese la cantidad de productos: "))

#Procesamiento de los datos
precio_total = precio_unitario * cantidad

#Salida de los datos
print(f"El costo total es de: ${precio_total}")