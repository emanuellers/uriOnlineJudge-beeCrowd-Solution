#2311 - Saltos Ornamentais
#Emanuelle Rodrigues
x = int (input())
for i in range (x):
  nome = str (input())
  partida = float (input())
  notas = input()
  n1 = list(map(float, notas.split()))
  n1.sort()
  del n1[-1]
  del n1[0]
  a = sum(n1) * partida
  print ("%s %.2f" %(nome, a))
  