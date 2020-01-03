#2147 - Galopeira
#Emanuelle Rodrigues
y = int (input ())
lista = []
for i in range (y):
    x =  str (input ())
    a = (len (x)* 0.01)
    lista += [a]
for a in lista:
    print ("%.2f" %a)