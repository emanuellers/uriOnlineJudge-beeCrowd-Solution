#1174 - Seleçao em Vetor I
#Emanuelle Rodrigues
lista = []
a = 0
for i in range (100):
    numeros = float (input ())
    lista += [numeros]
for i in lista: 
    if i <= 10 :
         print ("A[%d] = %.1f" %(a, i))
         a += 1
    else:
        a +=1