#1048 - Aumento de Salário
#Emanuelle Rodrigues
salario = float (input())
if salario >= 0 and salario <= 400.0:
    reajuste = salario * 0.15
    novo = salario + reajuste
    percentual = 15
elif salario > 400.0 and salario <= 800.0:
    reajuste = salario * 0.12
    novo = salario + reajuste
    percentual = 12
elif salario > 800.0 and salario <= 1200.0:
    reajuste = salario * 0.10
    novo = salario + reajuste
    percentual = 10
elif salario > 1200.0 and salario <= 2000.0:
    reajuste = salario * 0.07
    novo = salario + reajuste
    percentual = 7
elif salario > 2000.0:
    reajuste = salario * 0.04
    novo = salario + reajuste
    percentual = 4
print ("Novo salario: %.2f"%novo)
print ("Reajuste ganho: %.2f"%reajuste)
print("Em percentual: %d %%" %percentual)