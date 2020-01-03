#1914 - De Quem é a Vez?
#Emanuelle Rodrigues
x = int (input())
for i in range (x):
    nomes=  input().split()
    n1, es1, n2, es2 = nomes
    nums = input().split()
    a, b = nums
    a = int (a)
    b = int (b)
    soma = a + b
    if soma % 2 == 0:
        if es1 == "PAR":
           print(n1)
        elif es2 == "PAR":
            print(n2)
    elif soma % 2 !=0:
        if es1 == "IMPAR":
            print(n1)
        elif es2 == "IMPAR":
            print(n2)
