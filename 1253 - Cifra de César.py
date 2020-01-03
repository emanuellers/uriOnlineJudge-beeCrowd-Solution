#1253 - Cifra de César
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nova_palavra = ""
casos = int(input())
for i in range(casos):
  palavra = str(input())
  posi_c = int(input())
  for j in palavra:
    pesquisa = alfabeto.index(j)
    nova_palavra += alfabeto[pesquisa-posi_c]
  print(nova_palavra)
  nova_palavra = ""