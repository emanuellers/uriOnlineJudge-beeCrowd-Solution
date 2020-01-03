#2486 - C Mais ou Menos?
#Emanuelle Rodrigues
total = 0
lista = []
while True:
    num = int (input())
    if num == 0:
        break
    for i in range(num):
        a = input()
        coisas = a.split()
        coisas[0] = int (coisas[0])
        quanti = coisas[0]
        if "suco" in coisas:
            total += 120 * quanti
        elif "morango" in coisas:
            total += 85 * quanti
        elif "mamao" in coisas:
            total += 85 * quanti
        elif "goiaba" in coisas:
            total += 70 * quanti
        elif "manga" in coisas:
          total += 56 * quanti
        elif coisas[1]== "laranja":
            total += 50 * quanti
        elif "brocolis" in coisas:
            total += 34 * quanti
        coisas = []
    lista +=[total]
    total = 0
    
for i in lista:
    if i >= 110 and i<= 130:
        print ("%d mg"%i)
    if i < 110:
        result = 110 - i
        print ("Mais %d mg" %result)
    if i > 130:
        result = i - 130
        print ("Menos %d mg"%result)