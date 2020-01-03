#2006 - Identificando o Chá
#Emanuelle Rodrigues
soma = 0
x = int (input ())
y = input ().split ()
A, B, C, D, E =  y
A = int (A)
B = int (B)
C = int (C)
D = int (D)
E = int (E)
lista = [A, B, C, D, E]
for i in lista:
    if i == x:
        soma +=1
print (soma)
