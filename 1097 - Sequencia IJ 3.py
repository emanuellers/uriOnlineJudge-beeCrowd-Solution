#1097 - Sequencia IJ 3
#Emanuelle Rodrigues
I=-1
j = 7
for i in range (1,6):
    i=I+2
    print('I=%d J=%d' %(i,j))
    print('I=%d J=%d' %(i,j-1))
    print('I=%d J=%d' %(i,j-2))
    I=i
    j +=2