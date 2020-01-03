#1157 - Divisores I
#Emanuelle Rodrigues
x = int (input ())
for i in range (1, x+1):
    if x % i == 0:
        print (i)