#2060 - Desafio de Bino
#Emanuelle Rodrigues
x = int(input())
numeros = input()
inteiros = list(map(int, numeros.split()))
dois = 0
tres = 0
quatro = 0
cinco = 0
for i in (inteiros):
  if i%2 == 0:
    dois +=1
  if i %3 == 0:
    tres += 1
  if i %4 == 0:
    quatro +=1
  if i% 5 == 0:
    cinco +=1
print ("%d Multiplo(s) de 2" %dois)
print ("%d Multiplo(s) de 3" %tres)
print ("%d Multiplo(s) de 4" %quatro)
print ("%d Multiplo(s) de 5" %cinco)
