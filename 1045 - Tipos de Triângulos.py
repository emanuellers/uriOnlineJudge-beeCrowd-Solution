inputValues = input()

values = list(map(float, inputValues.split()))
values.sort()
A = values[2]
B = values[1]
C = values[0]
Aquadrado = A ** 2
Bquadrado = B ** 2
Cquadrado = C ** 2
sumBC = B + C
sumBCquadrado = Bquadrado + Cquadrado 
if A >= sumBC:
    print("NAO FORMA TRIANGULO")
else:
    if Aquadrado == sumBCquadrado:
        print("TRIANGULO RETANGULO")
    if Aquadrado > sumBCquadrado:
        print("TRIANGULO OBTUSANGULO")
    if Aquadrado < sumBCquadrado:
        print("TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or C == B:
        print("TRIANGULO ISOSCELES")
