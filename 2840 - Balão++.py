diametro, gas = input().split()
diametro = float(diametro)
gas = float(gas)
area = (((4 / 3.0)*3.1415)*(diametro**3))
print(int(gas/area))
