#2685 - A Mudança
#Emanuelle Rodrigues
while True:
  try:
    a = int(input())
    if a<90 or a == 360:
      print("Bom Dia!!")
    elif a>= 90 and a < 180:
      print("Boa Tarde!!")
    elif a>= 180 and a < 270:
      print("Boa Noite!!")
    elif a>= 270 and a < 360:
      print("De Madrugada!!")
  except:
    break
    