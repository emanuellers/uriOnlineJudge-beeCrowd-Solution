#2152 - Pepe, Já Tirei a Vela!
#Emanuelle Rodrigues
x = int (input())
for i in range (x):
  hora = input().split()
  horas, minuto, resp = hora
  horas= int (horas)
  minuto = int (minuto)
  if resp == "1":
    print ("%02d:%02d - A porta abriu!" %(horas, minuto))
  else:
    print ("%02d:%02d - A porta fechou!"%(horas,minuto))