#1168 - LED
#Emanuelle Rodrigues
x = int (input ())
lista = []
led = 0
for i in range (x):
    num = str (input ())
    um = num.count("1")
    dois = num.count("2")
    tres = num.count("3")
    qua = num.count("4")
    ci = num.count("5")
    seis = num.count("6")
    sete = num.count("7")
    oito = num.count("8")
    nove = num.count("9")
    zero = num.count("0")
    if um > 0:
        led += um * 2
    if dois  > 0:
        led += dois *5
    if tres >0 :
        led += tres * 5
    if qua > 0:
        led += qua * 4
    if ci > 0:
        led += ci * 5
    if seis > 0:
        led += seis * 6
    if sete > 0:
        led += sete * 3
    if oito > 0:
        led += oito * 7
    if nove > 0:
        led += nove * 6
    if zero > 0:
        led += zero * 6
    lista += [led]
    led = 0


for i in lista:
    print ("%d leds" %i)
