#1164 - Número Perfeito
#Emanuelle Rodrigues
y = int (input())
soma = 0
lista2 = []
for i in range (y):
    x = int (input ())
    for i in range (1,x-1):
        div = x % i
        if div == 0:
            soma += i
    if soma== x:
        lista2 +=["%d eh perfeito" %(x)]
    else:
        lista2 +=["%d nao eh perfeito" %(x)] 
    soma = 0
for i in lista2:
    print (i)