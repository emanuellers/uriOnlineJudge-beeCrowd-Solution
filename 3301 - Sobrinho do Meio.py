def intNumber(n):
  return int(n)

readAges = input()
ages = readAges.split(" ")
intAges = list(map(intNumber, ages))
sortedAges = sorted(intAges)

dictonary = {
    intAges[0]: "huguinho",
    intAges[1]: "zezinho",
    intAges[2]: "luisinho"
}

print(dictonary.get(sortedAges[1]))
