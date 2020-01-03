#1073 - Quadrado de Pares
#Emanuelle Rodrigues
x = int (input ())
for i in range (1, (x+1)):
    if i %2 == 0:
        print ("%d^2 = %d" %(i, i**2))
