#2150 - Vogais Alienígenas
#Emanuelle Rodrigues
while True:
  try:
    entrada = input()
    frase = input()
    soma = 0
    for i in entrada:
      soma += frase.count(i)
    print(soma)
  except:
    break