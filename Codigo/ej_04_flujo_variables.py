a = 20
b = 10
c = 30

a = a + 1               # a = 20 + 1 --> a = 21
b = b + a + 2           # b = 10 + 21 + 2 --> b = 33
c = a + b + c + 1       # c = 21 + 33 + 30 + 1 --> c = 85
a = 3                   # a = 3
b = 2                   # b = 2
c = a + b * c           # c = 3 + 2 * 85 --> c = 173
a = c + b               # a = 173 + 2 --> a = 175

#al finalizar a = 175; b = 2; c = 173

print(a, b, c)
