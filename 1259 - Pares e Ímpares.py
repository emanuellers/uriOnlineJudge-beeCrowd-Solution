#1259 - Pares e Ímpares
#Emanuelle Rodrigues
vezes = int(input())
pares = []
impares = []
for i in range(vezes):
    numeros = int(input())
    if numeros % 2 == 0:
        pares +=[numeros]
    elif numeros % 2 != 0:
        impares +=[numeros]
order_p = sorted(pares)
order_i = sorted(impares, reverse=True)
for i in order_p:
    print(i)
for i in order_i:
    print(i)