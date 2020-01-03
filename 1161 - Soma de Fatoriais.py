#1161 - Soma de Fatoriais
#Emanuelle Rodrigues
lista = []
while True:
  try:
    x = input().split()
    a, b = x
    a = int (a)
    b = int (b)
    fatorial = 1
    fatorial2 = 1
    for i in range(1,a+1):
      fatorial *= i
    for i in range(1,b+1):
      fatorial2 *= i
    soma = fatorial + fatorial2
    lista +=[soma]
  except:
    break
for i in lista:
  print(i)
