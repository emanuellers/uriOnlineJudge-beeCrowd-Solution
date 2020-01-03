#1079 - Médias Ponderadas
#Emanuelle Rodrigues
x = int (input ())
lista = []
for i in range (x):
    notas = input ().split()
    n1, n2, n3 = notas
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    media = (n1*0.2)+ (n2*0.3) + (n3*0.5)
    lista += [media]
for i in lista:
    print ("%.1f" %(i))