#1172 - Substituição em Vetor I
#Emanuelle Rodrigues
lista = []
a = 0
for i in range (10):
    numeros = int (input ())
    lista += [numeros]
for i in lista: 
    if i >0:
         print ("X[%d] = %d" %(a, i))
         a += 1
    else:
         print ("X[%d] = %d" %(a, 1))
         a += 1