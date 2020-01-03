#1985 - MacPRONALTS
#Emanuelle Rodrigues
x = int (input ())
preco = 0
for i in range (x):
    compra = input().split()
    pro, quanti = compra
    pro = str (pro)
    quanti = int (quanti)
    if pro == "1001":
        valor = 1.50 * quanti
    elif pro == "1002":
        valor =  2.50 * quanti
    elif pro == "1003":
        valor = 3.50 * quanti
    elif pro == "1004":
        valor = 4.50 * quanti
    elif pro == "1005":
        valor = 5.50 * quanti
    preco += valor 
print ("%.2f" %preco)