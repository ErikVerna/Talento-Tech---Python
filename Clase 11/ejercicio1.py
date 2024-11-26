def calcular_valor_final(precio, descuento):
    return precio - (precio * descuento / 100)

precio = float(input("Ingrese el precio: $"))
descuento = float(input("Ingrese el porcentaje de descuento: " + "%"))

try: 
    calcular_valor_final(precio, descuento)
except:
    

precio_final = calcular_valor_final(precio, descuento)

print(f"El precio final con el descuento es de : ${precio_final}")