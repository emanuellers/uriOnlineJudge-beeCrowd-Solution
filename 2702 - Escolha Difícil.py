#2702 - Escolha Difícil
#Emanuelle Rodrigues
disponivel = input().split()
necessario = input().split()
soma = 0
for i in range(3):
  a = int(disponivel[i])
  b = int(necessario[i])
  if b > a:
    sub = b - a
    soma += sub
print(soma)