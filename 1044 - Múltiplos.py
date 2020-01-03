#1044 - Múltiplos
#Emanuelle Rodrigues
val = input ().split ()
a, b = val
a = int (a)
b = int (b)
if a % b == 0 or b % a == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")