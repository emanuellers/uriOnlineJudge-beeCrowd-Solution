#2764 - Entrada e Saída de Data
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
  try:
    data = input()
    dSep = data.split("/")
    print(dSep[1] + "/" + dSep[0] + "/" + dSep[2])
    print(dSep[2] + "/" + dSep[1] + "/" + dSep[0])
    print(dSep[0] + "-" + dSep[1] + "-" + dSep[2] )
  except:
    break;