#2540 - Impeachment do Líder
#Emanuelle Rodrigues
lista2 = []
while True:
    try:
        x = int (input ())
        s = input()
        quanti = x *(2/3)
        a = s.count("1")
        if a >= quanti:
            lista2 +=["impeachment"]
        else:
            lista2 += ["acusacao arquivada"]
    except:
        break
for i in lista2:
    print (i)