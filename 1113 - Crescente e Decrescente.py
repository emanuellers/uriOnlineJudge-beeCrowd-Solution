#1113 - Crescente e Decrescente
#Emanuelle Rodrigues
lista = []
while True:
    x = input().split()
    a, b = x
    a = int (a)
    b = int (b)
    if a > b:
        lista +=["Decrescente"]
    elif b > a:
        lista += ["Crescente"]
    elif a == b:
        break
for i in lista:
    print (i)