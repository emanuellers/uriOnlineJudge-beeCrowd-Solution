#1115 - Quadrante
#Emanuelle Rodrigues
while True:
    x = input ().split ()
    x1, y1 = x
    x1 = int (x1)
    y1 = int (y1)
    if x1 == 0:
        break
    elif y1 == 0:
        break
    elif x1 > 0 and y1 > 0:
        print ("primeiro")
    elif x1 > 0 and y1 < 0:
        print ("quarto")
    elif x1 < 0 and y1 < 0:
        print ("terceiro")
    elif x1 < 0 and y1 > 0:
        print ("segundo")