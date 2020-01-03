#1015 - Distância Entre Dois Pontos
#Emanuelle Rodrigues
import math
p1 = input().split(" ")
p2 = input ().split (" ")
x1, y1 = p1
x2, y2 = p2
distancia = ((float (x2)- float (x1))**2 + (float (y2)- float (y1))**2)
a = math.sqrt (distancia)
print ("%.4f"%a)