#1865 - Mjölnir
#Emanuelle Rodrigues
y = int (input ())
for i in range (y):
    x = input ().split()
    v1, v2 = x
    v1 = str (v1)
    v2 = int (v2)
    if v1 == "Thor":
        print ("Y")
    else:
        print ("N")