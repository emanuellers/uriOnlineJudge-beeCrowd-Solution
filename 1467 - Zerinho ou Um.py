#1467 - Zerinho ou Um
#Emanuelle Rodrigues
while True:
    try:
        x = input ().split()
        a, b, c = x
        a = int (a)
        b = int (b)
        c = int (c)
        if a == c and a == b and b == c:
            print ("*")
        elif a == b and c != a:
            print ("C")
        elif b == c and b !=a:
            print ("A")
        elif a == c and c != b:
            print ("B")
    except:
        break