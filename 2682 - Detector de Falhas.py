#2682 - Detector de Falhas
#Emanuelle Rodrigues
b = int(input())
c=0
j=0
while True:
    try:

        a=int(input())
        if (a<b and c==0):
            c=b+1
            j=1
        b=a
    except:
        break
if(j==1):
   print(c)
if(j==0):
   print(b+1)