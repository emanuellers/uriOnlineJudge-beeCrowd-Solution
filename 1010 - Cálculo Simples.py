#1010 - Cálculo Simples
#Emanuelle Rodrigues
entrada = input().split (" ")
entrada2 = input().split (" ")
a, b, c = entrada 
e, f, g  = entrada2 
preco = (int (b) * float (c)) + (int (f) * float (g))
print ("VALOR A PAGAR: R$ %.2f"%preco)