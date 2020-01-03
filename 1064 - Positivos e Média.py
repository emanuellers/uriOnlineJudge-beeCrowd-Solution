#1064 - Positivos e Média
#Emanuelle Rodrigues
a = float (input ())
b = float (input ())
c = float (input ())
d = float (input ())
e = float (input ())
f = float (input ())
x =0
soma = 0
lista = [a, b, c, d, e, f]
for i in lista:
    if i > 0:
        soma += i
        x +=1
media = soma /x        
print ("%d valores positivos" %x)
print ("%.1f" %media)
        