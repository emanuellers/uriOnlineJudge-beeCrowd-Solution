#1094 - Experiências
#Emanuelle Rodrigues 
entrada_num = int(input())
rato = 0
sapo = 0
coelho = 0
for i in range (entrada_num):
  num_animal = input().split()
  if num_animal[1] == "S":
    sapo+= int(num_animal[0])
  elif num_animal[1]=="C":
    coelho+= int(num_animal[0])
  else:
    rato+= int(num_animal[0])
total = rato + coelho + sapo
perc_rato = rato*100/total
perc_sapo = sapo*100/total
perc_coelho = coelho*100/total

print("Total: %d cobaias\nTotal de coelhos: %d\nTotal de ratos: %d\nTotal de sapos: %d\nPercentual de coelhos: %.2f %%\nPercentual de ratos: %.2f %%\nPercentual de sapos: %.2f %%" %(total, coelho, rato, sapo, perc_coelho, perc_rato, perc_sapo))