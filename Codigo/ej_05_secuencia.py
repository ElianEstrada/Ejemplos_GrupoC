#Nota: para convertir 
#un tipo de dato a otro
#debemos colocar el nombre
#del tipo de dato que queremos obtener
# y dentro paraentesis el dato a convertir

#Sintaxis : 
# tipo '(' expresion ')'

#tipo = int|float|bool|str -> string

numero_1 = int(input("Ingrese un número entero: "))
numero_2 = int(input("Ingrese un número entero: "))

restultado_suma = numero_1 + numero_2
restultado_resta = numero_1 - numero_2

print("El restulado de la suma es: " + str(restultado_suma))
print("El restulado de la resta es: " + str(restultado_resta))