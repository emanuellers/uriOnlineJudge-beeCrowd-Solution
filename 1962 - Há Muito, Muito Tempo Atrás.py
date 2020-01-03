#1962 - Há Muito, Muito Tempo Atrás
#Emanuelle Rodrigues
vezes = int (input ())
lista = []
for i in range (1,vezes+1):
    anos = int (input ())
    lista += [anos]
for n in lista:
    if n < 2015:
        print ("%d D.C." %(2015 - n))
    else:
        print ("%d A.C." % (n - 2014))
