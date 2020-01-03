#1065 - Pares entre Cinco Números
#Emanuelle Rodrigues
x = 0
for i in range (5):
    inteiro = int (input ())
    if inteiro %2 == 0:
        x+=1
print ("%d valores pares" %x)        