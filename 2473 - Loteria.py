#2473 - Loteria
#Emanuelle Rodrigues
flavinho = input().split()
sorteio = input().split()
lista = ["azar", "azar", "azar", "terno","quadra", "quina", "sena"]
a = 0
for i in flavinho:
  if i in sorteio:
    a += 1
print(lista[a])
