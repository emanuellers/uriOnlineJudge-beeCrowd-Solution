#1281 - Ida à Feira
#Emanuelle Rodrigues
entrada = int(input())
dic1 = {}
valor = 0
for i in range(entrada):
  produtos = int(input())
  for j in range(produtos):
    produto, preco = input().split()
    dic1[produto] = float(preco)
  entrada2 = int(input())
  for k in range(entrada2):
    p1, p2 = input().split()
    p2 = int(p2)
    valor += dic1[p1]* p2
  print("R$ %.2f" %valor)
  valor = 0