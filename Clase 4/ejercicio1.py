#Ticket de la compra

"""
1. Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
2. Luego, debe calcular el importe de IVA (21%) de cada producto.
3. Por ultimo, debe mostrar en la terminal el ticket de la opreacion con todos los datos de la compra
"""

#Entrada de datos
print("###############-Ejercicio 1-####################")

#Nombres
nombre1 = input("Ingrese el nombre del primer producto: ")
nombre2 = input("Ingrese el nombre del segundo producto: ")
nombre3 = input("Ingrese el nombre del tercer producto: ")

#Cantidad
cantidad_producto1 = int(input(f"Ingrese la cantidad del producto {nombre1}: "))
cantidad_producto2 = int(input(f"Ingrese la cantidad del producto {nombre2}: "))
cantidad_producto3 = int(input(f"Ingrese la cantidad del producto {nombre3}: "))

#Precios
precio_producto1 = float(input(f"Ingrese el precio del producto {nombre1}: $"))
precio_producto2 = float(input(f"Ingrese el precio del producto {nombre2}: $"))
precio_producto3 = float(input(f"Ingrese el precio del producto {nombre3}: $"))

#Procesamiento de los datos
iva_producto1 = precio_producto1 * 0.21
iva_producto2 = precio_producto2 * 0.21
iva_producto3 = precio_producto3 * 0.21

precio_total_p1 = precio_producto1 * cantidad_producto1
precio_total_p2 = precio_producto2 * cantidad_producto2
precio_total_p3 = precio_producto3 * cantidad_producto3

producto1_final = precio_total_p1 + (iva_producto1 * cantidad_producto1)
producto2_final = precio_total_p2 + (iva_producto2 * cantidad_producto2)
producto3_final = precio_total_p3 + (iva_producto3 * cantidad_producto3)

precio_total = producto1_final + producto1_final + producto3_final

#Salida de los datos
print("Ticket: ")
print(f"{nombre1} || Precio Unitario: ${precio_producto1} || Cantidad: {cantidad_producto1} || %IVA (x unidad): {iva_producto1} || Subtotal = ${producto1_final}")
print(f"{nombre2} || Precio Unitario: ${precio_producto2} || Cantidad: {cantidad_producto2} || %IVA (x unidad): {iva_producto2} || Subtotal = ${producto2_final}")
print(f"{nombre3} || Precio Unitario: ${precio_producto3} || Cantidad: {cantidad_producto3} || %IVA (x unidad): {iva_producto3} || Subtotal = ${producto3_final}")
print(f"Precio Total = ${precio_total}")