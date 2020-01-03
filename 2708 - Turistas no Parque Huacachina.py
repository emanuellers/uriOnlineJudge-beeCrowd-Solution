#2708 - Turistas no Parque Huacachina
#Emanuelle Rodrigues
somaT = 0
somaJ = 0
while True:
  entrada = input()
  if entrada == "ABEND":
    break
  else:
    status, turistas = entrada.split()   
    turistas = int(turistas)
    if status == "SALIDA":
      somaT += turistas
      somaJ += 1
    else:
      somaJ -= 1
      somaT -= turistas
print(somaT)
print(somaJ)