#1144 - Sequência Lógica
#Emanuelle Rodrigues
x = int (input())
for i in range(1,x+1):
    a =i
    b = i*i
    c = i*i*i
    print ("%d %d %d" %(a, b, c))
    print ("%d %d %d" %(a, b+1, c+1))