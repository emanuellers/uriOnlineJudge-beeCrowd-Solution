#1387 - Og
#Emanuelle Rodrigues
while True:
  num_f = input()
  if num_f == "0 0":
    break
  else:
    num_sep = num_f.split()
    filho = int(num_sep[0])
    filha = int(num_sep[1])
    total = filho + filha
    print(total)