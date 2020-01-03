#1216 - Getline One
#Emanuelle Rodrigues
lista = []
soma = 0
while True:
    try:
        nome = str (input())
        dis = int (input ())
        lista += [dis]
    except:
        break
for i in lista:
    soma += i
distancia = soma / len(lista)   
print ("%.1f" %distancia)