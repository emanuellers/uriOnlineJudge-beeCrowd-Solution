#1140 - Flores Florescem da França
#Emanuelle Rodrigues
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
ok = ''
while True:
    try:
        frase = str(input())
        sep_frase = frase.split()
        mais = ''
        #letra referencial
        if frase == "*":
          for i in ok:
            print(i)
        ref = sep_frase[0][0]
        for i in sep_frase:
            if i[0] == "*":
               break
            elif i[0]== ref.upper() or i[0] == ref.lower():
                mais = 'Y'
            else:
                mais = 'N'
                break
        ok += mais

    except:
        break
