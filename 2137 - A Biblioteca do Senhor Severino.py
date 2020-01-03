#2137 - A Biblioteca do Senhor Severino
#Emanuelle Rodrigues
while True:
    try:
        lista = []
        x = int (input())
        for i in range (x):
            codigo = str (input())
            lista +=[codigo]
        lista.sort()
        for i in lista:
            print (i)
    except:
        break
            