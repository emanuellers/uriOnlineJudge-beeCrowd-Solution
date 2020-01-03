#1038 - Lanche
#Emanuelle Rodrigues
numeros = input ().split (" ")
a, b = numeros
a = int (a)
b = int (b)
if a == 1:
    total = b* 4.00
    print ("Total: R$ %.2f" %total)
elif a == 2:
    total = b * 4.50
    print ("Total: R$ %.2f" %total)
elif a == 3:
    total = b * 5.00
    print ("Total: R$ %.2f" %total)
elif a == 4:
    total = b *2.00
    print ("Total: R$ %.2f" %total)
elif a == 5:
    total = b *1.50
    print ("Total: R$ %.2f" %total)
    