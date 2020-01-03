#1175 - Troca em Vetor I
#Emanuelle Rodrigues
lista = []
a = 0
for i in range(20):
    num = int (input())
    lista.append(num)
lista.reverse()
for i in lista:
    print ("N[%d] = %d" %(a, i))
    a+=1

    