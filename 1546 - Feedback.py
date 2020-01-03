#1546 - Feedback
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
  try:
    vezes = int(input())
    for j in range(vezes):
      dias = int(input())
      for i in range(dias):
        tipo = int(input())
        if tipo == 1:
          print("Rolien")
        elif tipo == 2:
          print("Naej")
        elif tipo == 3:
          print("Elehcim")
        elif tipo == 4:
          print("Odranoel")
  except:
    break
    