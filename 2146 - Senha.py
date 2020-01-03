#2146 - Senha
#Emanuelle Rodrigues
while True:
    try:
        lista = []
        x = int(input ())
        lista+=[x]
        for i in lista:
            print ("%d" %(i - 1))
    except:
        break