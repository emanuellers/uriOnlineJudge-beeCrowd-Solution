#1329 - Cara ou Coroa
#Emanuelle Rodrigues
Mary = 0
John = 0
lista = []
while True:
  x = int(input())
  if x == 0:
    break
  entrada = input().split()
  for i in entrada:
    if i =="0":
      Mary +=1
    if i == "1":
      John+= 1
  lista +=["Mary won %d times and John won %d times"%(Mary,John)]
  Mary = 0
  John = 0
for i in lista:
  print (i)