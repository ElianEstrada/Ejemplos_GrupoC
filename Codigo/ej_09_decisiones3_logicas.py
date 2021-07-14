#Operadores lógicos
#and
#or
#not

#si hay coca-cola o pepsi comprar sino no.

b_coca = False
b_pepsi = True

if (b_coca or b_pepsi):
    print("Compre una bebida")
else:
    print("No compre nada")

#Tabla de verdad del or

"""

2^n -> donde n es el número de opciones

  a       b        a or b
False   False       False
False   True        True
True    False       True
True    True        True
"""


#Si hay coca y pepsi compras las dos sino no.

b_coca = False
b_pepsi = True

if (b_coca and b_pepsi):
    print("Compre ambas bebidas")
elif (b_coca and b_pepsi):
    print("No habia pepsi")
elif (b_pepsi):
    print("No había coca")
else: 
    print("No había ninguna")


#Tabla de verdad del or

"""

2^n -> donde n es el número de opciones

  a       b        a and b
False   False       False
False   True        False
True    False       False
True    True        True
"""


b_coca = 13

if (not b_coca < 20):
    print("no hay")
else: 
    print("Compre coca")
    