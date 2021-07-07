print("\nBienvenidos\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
opcion = input("\nIngrese una opción: ")

## 'if' '(' condicion ')' ':' -> obligatorio

## 'elif' '(' condicion ')' ':' -> opcional

## 'else' ':'  -> opcional

## Identación -> Tabulación

if (opcion < "5"):
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro número: "))

if (opcion == "1"):
    #ejecutar instrucciones
    resultado = num1 + num2
    print(f"\nEl resultado de la suma es: {resultado}")
elif (opcion == "2"):
    #ejecutar instrucciones
    resultado = num1 - num2
    print(f"\nEl resultado de la resta es: {resultado}")
elif (opcion == "3"):
    #ejecutar instrucciones
    resultado = num1 * num2
    print(f"\nEl resultado de la multiplicación es: {resultado}")
elif (opcion == "4"):
    #ejecutar instrucciones
    if (num2 != 0):
        resultado = num1 // num2
        print(f"\nEl resultado de la división es: {resultado}")
    else:
        print("No se puede dividir por 0")
elif (opcion == "5"):
    #ejecutar instrucciones
    exit()
else: 
    print("Opción Incorrecta, por favor ingrese una opción [1-5]")
    