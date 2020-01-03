#1197 - Volta à Faculdade de Física
#Emanuelle Rodrigues
lista = []
while True:
    try:
        var = input().split()
        v, t = var
        v = int (v)
        t = int (t)
        resul = v * (t*2)
        lista += [resul]
    except:
        break
for i in lista:
    print (i)