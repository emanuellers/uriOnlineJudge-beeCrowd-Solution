#2172 - Evento
#Emanuelle Rodrigues
lista = []
while True:
    xp = input().split()
    num, pontos = xp
    num = int (num)
    pontos = int (pontos)
    if num and pontos !=0:
        xpmais = num * pontos
        lista +=[xpmais]
    else:
        break

for i in lista:
    print (i)
    