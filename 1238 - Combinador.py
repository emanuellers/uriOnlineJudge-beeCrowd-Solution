#1238 - Combinador
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
num_entradas = int(input())
lista = []
lista_final = []
for i in range(num_entradas):
    string = str(input())
    lista +=[string]
nova_palavra = ""
for i in lista:
    break_it = i.split()
    palavra1 = break_it[0]
    palavra2 = break_it[1]
    if len(palavra1) > len(palavra2):
      maior = palavra1
    else:
      maior = palavra2
    for i in range(len(palavra1)+ len(palavra2)):
      if i < len(palavra1) and i < len(palavra2):
          nova_palavra += palavra1[i] + palavra2[i]
      elif i >= len(palavra1) or i >= len(palavra2):
          nova_palavra += maior[i:len(maior)]
          lista_final.append(nova_palavra)
          nova_palavra = ""
          break
for i in lista_final:
  print(i)