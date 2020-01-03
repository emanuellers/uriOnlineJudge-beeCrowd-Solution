#2543 - Jogatina UFPR
#Emanuelle Rodrigues
while True:
  try:
    x = input().split()
    N, I = x
    N = int (N)
    a = 0
    lista = []
    for e in range (N):
      val = input().split()
      i, j = val
      if i == I and j == "0":
        a +=1
    print (a)
    a = 0
  except:
    break
