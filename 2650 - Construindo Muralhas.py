#2650 - Construindo Muralhas
#Emanuelle Rodrigues
lista = []
x = input().split()
num, alt = x
num = int (num)
alt = int (alt)
for i in range(num):
  nome =  input().split()
  nome[-1] = int (nome[-1])
  if nome[-1] > alt:
    del nome[-1]
    lista +=[" ".join(nome)]
for i in lista:
  print (i)