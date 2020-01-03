#2497 - Contando Ciclos
#Emanuelle Rodrigues
a = 0
lista = []
e = 1
while True:
    x = int (input ())
    if x == -1:
        break
    while x > 1:
        dois = x - 2
        x = dois
        a += 1
    lista +=[a]
    a = 0
for i in lista:
    print ("Experiment %d: %d full cycle(s)" %(e,i))
    e +=1