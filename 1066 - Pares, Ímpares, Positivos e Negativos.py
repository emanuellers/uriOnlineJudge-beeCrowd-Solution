#1066 - Pares, Ímpares, Positivos e Negativos
#Emanuelle Rodrigues
y = int (input ())
x = int (input ())
v = int (input ())
c = int (input ())
w = int (input ())
lista = [y, x, v, c, w]
par = 0
impar = 0
posi = 0
neg = 0
for i in lista:
    if i % 2 ==0:
        par +=1
    elif i % 2 != 0:
        impar +=1
    if i > 0:
        posi +=1
    elif i < 0:
        neg +=1
print ("%d valor(es) par(es)" %(par)) 
print ("%d valor(es) impar(es)" %(impar))
print ("%d valor(es) positivo(s)" %(posi))
print ("%d valor(es) negativo(s)" %(neg))
        