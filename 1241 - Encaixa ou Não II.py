#1241 - Encaixa ou Não II
#Emanuelle Rodrigues
x = int (input ())
for i in range (x):
    doisnum = input ().split()
    um, dois = doisnum
    um = str (um)
    dois = str (dois)
    achar = um.find(dois)
    if um == dois:
        print ("encaixa")
    elif achar > 0:
        print ("encaixa")
    else:
        print ("nao encaixa")