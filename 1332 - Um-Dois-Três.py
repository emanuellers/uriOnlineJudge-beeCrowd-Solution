#1332 - Um-Dois-Três
#Emanuelle Rodrigues
x = int (input())
lista = []
for i in range(x):
  word = str (input())
  if len(word) == 5:
    lista +=["3"]
  elif (word[0] == "o" and word[2]== "e" ) or (word[0]=="o" and word[1] =="n") or (word[1]=="n"
  and word[2]=="e"): 
    lista +=[1]
  else:
    lista +=[2]
    
for i in lista:
  print (i)