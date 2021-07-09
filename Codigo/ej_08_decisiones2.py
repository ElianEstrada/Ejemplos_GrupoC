print("\n1. Par o Impar\n2. Calculadora\n3. Salir")
opcion_menu = input("\nIngrese una opción: ")

if (opcion_menu == "1"):
    print("\nUsted esta en Par o Impar")

    num1 = int(input("Ingrese un número entero: "))

    if (num1 != 0):
        if (num1 % 2 == 0):
            print("El número {} es par".format(num1))
        else: 
            print(f"El número {num1} es impar")
    else: 
        print("El número 0 es neutro")

elif (opcion_menu == "2"): 
    print("\nUsted esta en Calculadora")

    print("1. Suma\n2. Multiplicación\n3. Salir")
    opcion_calculadora = input("\nIngrese una opción: ")

    if (opcion_calculadora <= "2"):
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

    if (opcion_calculadora == "1"):
        print("Suma")
        print("\nEl resultado de sumar %s con %s es: %s" % (num1, num2, (num1 + num2)))

    elif (opcion_calculadora == "2"):
        print("Multiplicación")
        print("El resultado de sumar",num1,"con",num2,"es:",(num1 * num2))

    elif (opcion_calculadora == "3"):
        print("Hasta luego")
    else: 
        print("Opción Incorrecta.")

elif (opcion_menu == "3"):
    print("Hasta pronto")
    exit()
else:
    print("Opción incorrecta, escoga una opción del [1-3]")
