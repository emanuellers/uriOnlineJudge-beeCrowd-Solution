#2544 - Kage Bunshin no Jutsu
#Emanuelle Rodrigues
while True:
    try:
        i = 0
        x = int (input ())
        for i in range (x):
            y = 2 ** i
            if y == x:
                break
            i +=1
        print (i)    
    except:
        break
