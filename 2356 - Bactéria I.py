#2356 - Bactéria I
#Emanuelle Rodrigues
lista = []
while True:
    try:
        x = str (input ())
        y = str (input ())
        a = x.find(y)
        if a >= 0:
            lista+= ["Resistente"]
        else:
            lista +=["Nao resistente"]
    except:
        break
for i in lista:
    print (i)