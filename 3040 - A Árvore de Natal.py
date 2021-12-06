rangeNumber = int(input())
def integerFunc(x):
  return int(x)

for i in range(rangeNumber):
  specifications = input()
  listTrees =  list(map(integerFunc, specifications.split()))
  size = listTrees[0]
  thickness = listTrees[1]
  branchs = listTrees[2]
  if (size >= 200 and size <= 300) and (thickness >= 50) and (branchs >= 150):
    print("Sim")
  else:
    print("Nao")
