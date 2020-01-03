#1170 - Blobs
#Emanuelle Rodrigues
x = int (input ())
a = 0
lista = []
for i in range (x):
    comida = float (input ())
    if comida <= 1:
        lista +=[0]
    else:
        while True:
            dias = comida * 0.5
            comida = dias
            a +=1
            if dias <= 1:
                break
            
        lista +=[a]
        a = 0
for i in lista:
    print ("%d dias" %i )