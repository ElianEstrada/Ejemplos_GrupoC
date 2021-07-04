##Formas de mostrar información 

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

resultado = num1 + num2

##si num1 = 3 y num2 = 4
##El resultado de sumar 3 con 4 es: 7

##Primera forma -> concatenación con +

print("El resultado de sumar " + str(num1) + " con " + str(num2) + " es: " + str(num1 + num2))

##Segunda forma -> concatenación con ,
print("El resultado de sumar",num1,"con",num2,"es:",num1 + num2)

##Tercera forma -> interpolación con format
print("El resultado de sumar {} con {} es: {}".format(num1, num2, num1 + num2))

##Cuarta forma -> interpolación con string-f
print(f"El resultado de sumar {num1} con {num2} es: {num1 + num2}")

##Quinta forma -> formatos
print("El resultado de sumar %s con %s es: %s" % (num1, num2, resultado))