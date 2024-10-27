#Solicitar al usuario el precio y el % del iva (Entrada de Datos)
precio = float(input("Ingrese el precio del producto: $"))
iva = float(input("Ingrese el porcentaje del iva: %"))

#Calculamos el monto del iva y del precio final (procesamiento de los datos)
monto_iva = (precio * iva) / 100
precio_total = precio + monto_iva

#Mostrar el precio final
print(f"El precio final con IVA es de: ${precio_total}")

