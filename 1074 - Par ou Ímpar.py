#1074 - Par ou Ímpar
#Emanuelle Rodrigues
x = int (input ())
for i in range (x):
    outro = int (input ())
    if outro %2 ==0 and outro > 0:
        print ("EVEN POSITIVE")
    elif outro % 2 == 0 and outro < 0:
        print ("EVEN NEGATIVE")
    elif outro % 2!=0 and outro > 0:
        print ("ODD POSITIVE")
    elif outro % 2 !=0 and outro < 0:
        print ("ODD NEGATIVE")
    elif outro == 0:
        print ("NULL")
        