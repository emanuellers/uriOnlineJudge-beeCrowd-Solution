#2175 - Qual o Mais Rápido?
#Emanuelle Rodrigues
x =  input ().split ()
o, b, i = x
o = float (o)
b = float (b)
i = float (i)
if o < b and o < i:
    print ("Otavio")
elif b < o and b < i:
    print ("Bruno")
elif i < o  and i < b:
    print ("Ian")
elif i == b or b == o or i == o:
    print ("Empate")