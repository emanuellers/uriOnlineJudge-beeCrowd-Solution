#2390 - Escada Rolante
#Emanuelle Rodrigues
x = int(input())
lista = []
for i in range (x):
    y = int(input())
    lista +=[y]
a = 1
total = 0
listaResult = []
for i in range(len(lista)):
    sub = lista[a] - lista[i]
    if sub > 10:
      listaResult +=[10]
    else:
      listaResult += [sub]
    if a == len(lista)-1:
        break
    else:
      a += 1
    
print(sum(listaResult)+10)