#1153 - Fatorial Simples
#Emanuelle Rodrigues
x = int (input ())
lista = []
multi = 1
for i in range (1, x+1):
    lista +=[i]
for a in lista:
    multi *=a
print (multi)
    
    