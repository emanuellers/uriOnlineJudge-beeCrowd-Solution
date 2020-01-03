#1866 - Conta
#Emanuelle Rodrigues
x = int (input ())
lista = []
for i in range (x):
    y = int (input())
    lista += [y]
for i in lista:
    if i % 2 == 0:
        print ("0")
    elif i % 2 !=0:
        print ("1")