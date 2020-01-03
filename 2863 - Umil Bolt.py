#Emanuelle Rodrigues
#2863 - Umil Bolt
while True:
  try:
    menor = 11
    vezes = int(input())
    for i in range(vezes):
      tempo = float(input())
      if tempo < menor:
        menor = tempo
    print(menor)
  except:
    break
