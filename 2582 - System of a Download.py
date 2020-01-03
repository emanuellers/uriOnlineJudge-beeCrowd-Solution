#2582 - System of a Download
#Emanuelle Rodrigues

x = int (input ())
lista = []
for i in range (x):
    nums= input ().split ()
    a, b = nums
    a = int (a)
    b = int (b)
    soma = a + b
    if soma == 0:
       lista += ["PROXYCITY"]
    elif soma == 1:
        lista += ["P.Y.N.G."]
    elif soma == 2:
       lista += ["DNSUEY!"]
    elif soma == 3:
        lista += ["SERVERS"]
    elif soma == 4:
         lista += ["HOST!"]
    elif soma == 5:
         lista += ["CRIPTONIZE"]   
    elif soma == 6:
         lista += ["OFFLINE DAY"]
    elif soma == 7:
         lista += ["SALT"]
    elif soma == 8:
         lista += ["ANSWER!"]
    elif soma ==9:
         lista += ["RAR?"]
    elif soma == 10:
        lista += ["WIFI ANTENNAS"]
for i in lista:
    print (i)