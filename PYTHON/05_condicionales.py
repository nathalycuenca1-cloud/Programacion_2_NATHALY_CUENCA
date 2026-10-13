# Condicional if
# simple


combustible = 5
if combustible >= 10:
    print("puedes despegar")


# condicional if-else
creditos = int(input("Ingrese la cantidad de creditos: "))
precio_repuestos =int(input("Ingrese el precio de los repuestos: "))
if creditos >= precio_repuestos:
    print("puedes comprar los repuestos")
else:
    print("no tienes suficientes creditos para comprar los repuestos")

# if anidado
if creditos >= precio_repuestos:
    print("puedes comprar los repuestos")
    if creditos > precio_repuestos:
        print("te sobran creditos")
    else:
        print("no te sobran creditos")
else:
    print("no tienes suficientes creditos para comprar los repuestos")

# condicional if-elif-else
if creditos > precio_repuestos:
    print("puedes comprar los repuestos y te sobran creditos")
elif creditos == precio_repuestos:
    print("puedes comprar los repuestos pero no te sobran creditos")
else:
    print("no tienes suficientes creditos para comprar los repuestos")


tipo_repuesto = input("Ingrese el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuestos and tipo_repuesto == "ala":
    print("puedes comprar el repuesto Y te sobran creditos ")
elif tipo_repuesto == "ala" and creditos >= precio_repuestos :
    print("puedes comprar el repuesto y te sobran creditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuestos:
    print("puedes comprar el repuesto y te sobran creditos")
else:
    print("Tipo de repuesto no es valido")




peso = float(input("Ingresa el peso del paquete en kilogramos: "))
zona = int(input("Ingresa la zona de destino (1, 2 o 3): "))

if zona == 1:
    costo_total = peso * 5.0
    print(f"Zona 1 (América) - Costo final del envío: ${costo_total:.2f}")
elif zona == 2:
    costo_total = peso * 7.5
    print(f"Zona 2 (Europa) - Costo final del envío: ${costo_total:.2f}")
elif zona == 3:
    costo_total = peso * 10.0
    print(f"Zona 3 (Resto del mundo) - Costo final del envío: ${costo_total:.2f}")
else:
    print("Error: Zona de destino no válida. Debe ser 1, 2 o 3.")