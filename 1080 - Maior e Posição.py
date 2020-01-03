#1080 - Maior e Posição
#Emanuelle Rodrigues
lista = []
for i in range(100):
    x = int (input())
    lista +=[x]
maior = max(lista)
posi = lista.index(maior) + 1
print ("%d"%maior)
print ("%d"%posi)