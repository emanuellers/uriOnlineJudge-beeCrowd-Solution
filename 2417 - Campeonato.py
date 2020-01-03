#Emanuelle Rodrigues
#2417 - Campeonato

lista = input().split()
c1 = int(lista[0]) *3
c2 = int(lista[1])
pontos_c = c1 + c2
c3 = int(lista[2])
f1 = int(lista[3]) *3
f2 = int(lista[4])
pontos_f = f1 + f2
f3 = int(lista[5])

if pontos_c > pontos_f:
  print("C")
elif pontos_c < pontos_f:
  print("F")
elif pontos_c == pontos_f:
  if c3 > f3:
    print ("C")
  elif f3 > c3:
    print("F")
  else:
    print("=")