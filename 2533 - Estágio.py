#2533 - Estágio
#Emanuelle Rodrigues
while True:
  try:
    entrada = int(input())
    cTotal = 0
    sup = 0
    for i in range(entrada):
      n, c = input().split()
      n = int(n)
      c = int(c)
      sup += n*c
      cTotal += c
    resultado = sup / (cTotal*100)
    print("%.4f" %resultado)
  except:
    break