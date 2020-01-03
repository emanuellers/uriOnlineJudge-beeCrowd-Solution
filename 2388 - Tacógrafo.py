#2388 - Tacógrafo
#Emanuelle Rodrigues
entrada = int(input())
total = 0
for i in range(entrada):
  t, v = input().split()
  total += int(t) * int(v)
print(total)
