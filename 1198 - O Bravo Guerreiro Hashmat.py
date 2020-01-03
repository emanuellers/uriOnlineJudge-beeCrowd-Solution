#1198 - O Bravo Guerreiro Hashmat
#Emanuelle Rodrigues

lista = []
while True:
    try:
        a = input().split()
        b, c = a
        b = int (b)
        c = int (c)
        if b < c:
            resul = c - b
            lista += [resul]
        else:
            resul = b - c
            lista += [resul]
    except:
        break
for i in lista:
    print (i)
            