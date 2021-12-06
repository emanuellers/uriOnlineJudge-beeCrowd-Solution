comparable = 0
for i in range(4):
  total = 0 
  numbers = input()
  for j in numbers.split():
    total += int(j)
  if total > comparable:
    comparable = total
binary = "{0:b}".format(comparable)
print(str(comparable) + " = " + binary)
