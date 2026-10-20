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




peso = float(input("Ingrese el peso del paquete en kilogramos: "))
zona = input("Ingrese la zona de destino (1, 2, 3): ")
if zona == "1":
    if peso <= 5:
        print("El costo del envío es de $10")
    elif peso <= 10:
        print("El costo del envío es de $20")
    else:
        print("El costo del envío es de $30")
elif zona == "2":
    if peso <= 5:
        print("El costo del envío es de $15")
    elif peso <= 10:
        print("El costo del envío es de $25")
    else:
        print("El costo del envío es de $35")
elif zona == "3":
    if peso <= 5:
        print("El costo del envío es de $20")
    elif peso <= 10:
        print("El costo del envío es de $30")
    else:
        print("El costo del envío es de $40")
else:
    print("Zona de destino no  es valida")


