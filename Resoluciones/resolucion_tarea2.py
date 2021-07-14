#Declaracion de variables para el precio
#de los helados

precio_cono = 4
precio_vaso = 5
precio_suave = 7
precio_banana = 10

#Variable para el total
total = 0

#Variables para los aditamentos extras
agrandado = 1
chocolate = 1
mani = 2
crema_batida = 2

# a += 1-> a = a + 1
menu_principal = "\nBienvenidos a la Heladería\n1. Helado de cono"
menu_principal += "\n2. Helado de Vaso\n3. Helado Suave\n4. Banana Split\n5. Salir"

print(menu_principal)

opcion_principal = int(input("\nIngrese una opción [1-5]: "))


if (opcion_principal == 1):
    #Helado de Cono
    print("\nHelado de Cono: $" + str(precio_cono))
    total = precio_cono

elif (opcion_principal == 2):
    #Helado de Vaso
    print("\nHelado de Vaso: $" + str(precio_vaso))
    total = precio_vaso

elif (opcion_principal == 3):
    #Helado Suave
    print("\nHelado Suave: $" + str(precio_suave))
    total = precio_suave

elif (opcion_principal == 4):
    #Banan Split
    print("\nBanana Split: $" + str(precio_banana))
    total = precio_banana

elif(opcion_principal == 5):
    print("\nHasta pronto...")
    exit()
else: 
    print("\nIngreso una opción incorrecta.")
    exit()

aditamento = input("\nDesea agrandar su helado? [S/N]: ")

if (aditamento == 'S'):
    total += agrandado

aditamento = input("\nDesea agregar chocolate? [S/N]: ")

if (aditamento == 'S'):
    total += chocolate

aditamento = input("\nDesea agregar maní? [S/N]: ")

if (aditamento == 'S'):
    total += mani

aditamento = input("\nDesea agregar crema batida? [S/N]: ")

if (aditamento == 'S'):
    total += crema_batida

menu_pago = "\n1. Tarjeta de Crédito\n2. Efectivo"
print(menu_pago)
opcion_pago = int(input("\nSeleccione un tipo de pago: "))

if (opcion_pago == 1):
    #Elijio tarjeta de Crédito
    print("\nTarjeta de Crédito")

    #para los descuentos
    # total - (total * porcentaje)
    total = total - (total * 0.05)

    print(f"El total a pagar es de: ${total}")

elif (opcion_pago == 2):
    #Efectivo
    print("\nPago en efectivos")
    print(f"El total a pagar es de: ${total}")

    monto_pagado = float(input("Ingrese el monto a pagar: "))

    if (monto_pagado < total):
        print("\nEl monto ingresado es menor al total, no se puede procesar")
    elif (monto_pagado == total):
        print("\nGracias por su visita, disfrute su helado.")
    else: 
        cambio = monto_pagado - total
        print(f"\nGracias por su visita. Tome su cambio: ${cambio}")

else: 
    print("\nOpción incorrecta")
    exit()