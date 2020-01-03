#1099 - Soma de Ímpares Consecutivos II
#Emanuelle Rodrigues
soma = 0
x = int (input())
for i in range (x):
  a, b = input().split()
  a = int(a)
  b = int (b)
  if a > b:
    for i in range (b+1, a):
      if i %2 !=0:
        soma += i
  else:
    for i in range (a+1, b):
      if i %2 !=0:
        soma += i
  print (soma)
  soma = 0