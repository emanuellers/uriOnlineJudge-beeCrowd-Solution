#1871 - Zero vale Zero
#Emanuelle Rodrigues
lista = []
while True:
    num = input().split()
    a, b = num
    a = int (a)
    b = int (b)
    soma = a + b
    if soma == 0:
        break
    frase = str (soma)
    tira = frase.replace("0", "")
    lista += [tira]
for i in lista:
    print (i)
