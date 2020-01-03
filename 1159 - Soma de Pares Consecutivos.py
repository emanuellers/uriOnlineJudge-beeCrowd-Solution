#1159 - Soma de Pares Consecutivos
#Emanuelle Rodrigues
lista = []
while True:
    x = int (input ())
    soma = x
    par = x + 1
    soma3 = par
    if x ==0:
        break
    if x %2 == 0:
        for i in range (4):
            a = x+2
            soma +=a
            x = a
        lista += [soma]
    elif x % 2 !=0:
        for i in range (4):
            b = par +2
            soma3 +=b
            par = b
        lista +=[soma3]    
for i in lista:
    print (i)