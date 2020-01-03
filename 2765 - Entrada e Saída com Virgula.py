#2765 - Entrada e Saída com Virgula
#Emanuelle Rodrigues
while True:
  try:
    x = input()
    novoX = x.split(",")
    print(novoX[0] + "\n" + novoX[1])
  except:
    break