#1046 - Tempo de Jogo
#Emanuelle Rodrigues
x = input ().split ()
y, z = x
y= int (y)
z = int (z)
if y == z:
    print ("O JOGO DUROU 24 HORA(S)")
elif y > z:
    tempo = (24 - y) + z
    print ("O JOGO DUROU %d HORA(S)" %tempo)
elif y < z:
    tempo2 = -(y) + z
    print ("O JOGO DUROU %d HORA(S)" %tempo2)