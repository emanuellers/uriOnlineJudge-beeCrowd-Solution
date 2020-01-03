#2547 - Montanha-Russa
#Emanuelle Rodrigues
while True:
    try:
        x = input ().split()
        num, altmin, altmax = x
        num = int (num)
        altmin = int (altmin)
        altmax = int (altmax)
        per = 0
        for i in range (num):
            alts = int (input())
            if alts >= altmin and alts <= altmax:
                per += 1
        print (per)
    except:
        break