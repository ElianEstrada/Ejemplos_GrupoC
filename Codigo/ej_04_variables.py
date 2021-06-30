numero = 0
_nombre = 'elian'
numero = 1

valor_01 = 10

suma = 2 + 1
resta = 2 - 1
multi = 5 * 4
div = 15 / 3
pot = 2**4
mod = 2 % 2
negativo = -1


mayor = 5 > 4       #-> True o False? : True
mayor_igual = 5 >= 3 #-> True
menor = 5 < 6        # -> True
menor_igual = 5 <= 5 # -> True
igual = 4 == 1      # -> False
diferente = 3 != 2 # -> True


#and -> devuelve true si todas las condiciones son verdaderas
#con una que sea falsa el resultado es falso

#or -> devuelve true si almenos una de sus condiciones es verdadera
#con todas falsas el resultado es falso

#not -> invierte el valor, si es True -> False, False -> True

v_and = True and False and True and True and True          #-> False
v_or = True or False or False or False or False           #-> True
v_not = not True                #-> False


v_compleja = 5 + 2 > 4 and 3 + 1 <= 12

# 5 + 2 = 7 -> 7 > 4 and 3 + 1 <= 12
# 7 > 4 and 3 + 1 <= 12

# 7 > 4 and 4 <= 12
# True and True 
# True

print(v_compleja)

#precedencia de operadores 

"""

1. ()
2. -
3. **
4. *, /, %
5. +, -
6. >, >=, <, <=, ==, !=
7. not
8. and
9. or 

"""