#1240 - Encaixa ou Não I
#Emanuelle Rodrigues
casos = int(input())

while casos > 0:
    
    valores = input().split()
    A, B = valores[0], valores[1]
    
    tamanhoA = len(A)
    tamanhoB = len(B)
    
    if tamanhoA >= tamanhoB:
        
        #diferencaAB = tamanhoA - tamanhoB
        
        if A[tamanhoA-tamanhoB:tamanhoA] == B:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
    
    casos -= 1