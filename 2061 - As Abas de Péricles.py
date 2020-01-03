#2061 - As Abas de Péricles
#Emanuelle Rodrigues
abas,acoes = input().split()
abas = int(abas)
acoes = int(acoes)
for i in range(acoes):
  entrada = str(input())
  if entrada[0] == "f":
    abas += 1
  else:
    abas -= 1
print(abas)