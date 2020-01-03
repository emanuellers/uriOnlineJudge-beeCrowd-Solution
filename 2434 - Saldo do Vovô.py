#2434 - Saldo do Vovô
#Emanuelle Rodrigues
num, saldo = input().split()
num = int(num)
saldo = int(saldo)
menor = saldo
for i in range(num):
  nova = int(input())
  saldo += nova
  if saldo < menor:
    menor = saldo
print(menor)
