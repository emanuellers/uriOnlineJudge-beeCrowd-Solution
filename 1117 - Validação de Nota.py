#1117 - Validação de Nota
#Emanuelle Rodrigues
a = 0
b = 0
soma = 0
lista = []
while True:
    nota = float (input ())
    if nota < 0 or nota >10:
        b +=1
        continue
    elif nota >= 0 and nota <= 10:
        a +=1
        lista += [nota]
        if a == 2:
            break
        
for n in lista:
    soma+=n
    media = soma/2        
for i in range (b):
    print ("nota invalida")

print ("media = %.2f" %media) 