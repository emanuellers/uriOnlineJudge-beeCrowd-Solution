#1146 - Sequências Crescentes
#Emanuelle Rodrigues
while True:
  n = int (input())
  if (n > 0):

    for i in range(1,n+1):

      if(i < n):
        print(i, end=" ")
      if (i == n):
        print(i)

  if (n == 0):
    break
