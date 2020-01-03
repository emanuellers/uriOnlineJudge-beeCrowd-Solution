#1028 - Figurinhas
#Emanuelle Rodrigues
x = int (input ())
for i in range (x):
    num = input().split()
    n1, n2 = num
    n1 = int (n1)
    n2 = int (n2)
    dividendo = n1
    divisor = n2
    while( dividendo % divisor != 0 ):
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto
    print (divisor)