#1131 - Grenais
#Emanuelle Rodrigues
a = 1
x = 0
y = 0
e = 0
c = 0
while True:
    gols = input().split()
    i, g = gols
    i = int (i)
    g = int (g)
    vezes = int (input ())
    c +=1
    if i > g:
        x+=1
    elif g > i:
        y +=1
    elif i == g:
        e +=1
    if vezes == 1:
        a +=1
        continue
    else:
        break
for i in range (c):
    print ("Novo grenal (1-sim 2-nao)")
print ("%d grenais" %a)
print ("Inter:%d" %x)
print ("Gremio:%d" %y)
print ("Empates:%d" %e)
if x > y:
    print ("Inter venceu mais")
elif y > x:
    print ("Gremio venceu mais")
else: 
    print ("Nao houve vencedor")
