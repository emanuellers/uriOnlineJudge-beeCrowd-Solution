#2456 - Cartas
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
cartas = input().split()
c = []
for i in cartas:
  novo_i = int(i)
  c += [novo_i]
if c[0] > c[1] and c[1] > c[2] and c[2] > c[3] and c[3] > c[4]:
  print("D")
elif c[0] < c[1] and c[1] < c[2] and c[2] < c[3] and c[3] < c[4]:
  print("C")
else:
  print("N")
  
