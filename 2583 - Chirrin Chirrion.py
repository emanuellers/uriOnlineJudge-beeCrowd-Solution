#2583 - Chirrin Chirrion
#Emanuelle Rodrigues
lista = []
a = []
x = int(input())
for i in range (x):
  vezes = int(input())
  for b in range (vezes):
    frases = input().split()
    coisa, ch = frases
    if ch == "chirrin":
        a+=[coisa]
    else:
        for i in a:
            if ch == "chirrion" and coisa == i:
                a.remove(i)
  a = sorted(set(a))
  if len(a) >= 1:
      lista +=["TOTAL"]
  for i in a:
    lista +=[i]
  a = []
for i in lista:
  print (i)
  