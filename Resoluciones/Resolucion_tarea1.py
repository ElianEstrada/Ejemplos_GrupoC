#Ejercicio 1

a = 5 * 2                                   # a = 10
b = 3 + 1                                   # b = 4
c = 4                                       # c = 4
a = c * 2 + b                               # a = 4 * 2 + 4 -> a = 12
b = a * b                                   # b = 12  * 4 -> b = 48
c = b / c + 1                               # c = 48 / 4 + 1 -> c = 13
a = ((2 + 2) * b + a)/c                     # a = ((2 + 2) * 48 + 12) / 13 -> a = 204/13 -> a = 15.69230769
c = b                                       # c = 48
b = a + c                                   # b = 15.69230769 + 48 -> b = 63.69230769

# a = 15.69230769
# b = 63.69230769
# c = 48


#Ejercicio 2

a = 6                                       # a = 6
b = 4                                       # b = 4
c = a < b                                   # c = 6 < 4 -> c = false
d = 5                                       # d = 5
a = b * d                                   # a = 4 * 5 -> a = 20
b = a + b                                   # b = 20 + 4 -> b = 24
d = a + d                                   # d = 20 + 5 -> d = 25
c = not (a < b) and d < a + b or c          # c = not (20 < 24) and 25 < 20 + 24 or false -> c = not(true) and 25 < 44 or false
                                            # c = false and true or false -> c = false or false -> c = false

# a = 20
# b = 24
# c = false
# d = 25



#Ejercicio 3

a = 7                                       # a = 7
b = a * 3                                   # b = 7 * 3 -> b = 21
c = b * 4                                   # c = 21 * 4 -> c = 84
a = a + a + b                               # a = 7 + 7 + 21 -> a = 35
b = a + b + c * b                           # b = 35 + 21 + 84 * 21 -> b = 1820
c = a * b ** c                              # c = 35 * 1820 ** 84 -> 
d = 3                                       # d = 3
a = d + c                                   # a = 3 + 7.87521334133e+202 -> a = 
d = d + a + c                               # d = 3 + ... + 4.13...
b = d * d * b                               # b = .. * ... * 1400


print(a)
print(b)
print(c)
print(d)