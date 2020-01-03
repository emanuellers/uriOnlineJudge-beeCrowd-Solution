#1145 - Sequência Lógica 2
#Emanuelle Rodrigues
a = input().split()
x, y = a
y = int (y)
x = int (x)
v = 0
num = 0
for i in range(1, y+1):
    v +=1
    if v == x:
        print (i, end="\n")
        v = 0
    elif i == num:
      print (i)
    else:
        print (i, end=" ")
    num += 1    
