#2534 - Exame Geral
#Emanuelle Rodrigues
while True:
  try:
    n1 = []
    x, y = input().split()
    x = int (x)
    y = int (y)
    for i in range(x):
      notas = int (input())
      n1 += [notas]
    n1.sort(reverse = True)  
    for i in range (y):
      busca = int (input())
      posi = n1[busca-1]
      print (posi)
  except:
    break