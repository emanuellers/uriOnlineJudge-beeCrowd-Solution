#1072 - Intervalo 2
#Emanuelle Rodrigues
x = int (input ())
soma = 0
soma2 = 0
for i in range (x):
    y = int (input ())
    if y >= 10 and y <= 20:
        soma += 1
    else:
        soma2 += 1

print ("%d in" %soma)
print ("%d out" %soma2)
