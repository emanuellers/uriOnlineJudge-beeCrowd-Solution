#2423 - Receita de Bolo
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
bolo = input().split()
farinha = int(bolo[0])
ovos = int(bolo[1])
leite = int(bolo[2])
div1 = int(farinha/2)
div2 = int(ovos/3)
div3 = int(leite/5)
lista = [div1, div2, div3]
if div1 == div2 == div3:
  print(div1)
else:
  print(min(lista))