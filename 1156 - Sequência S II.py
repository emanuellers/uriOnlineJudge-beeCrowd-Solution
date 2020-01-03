#1156 - Sequência S II
#Emanuelle Rodrigues
x = 3
y = 1
soma = 0
for i in range (18):
    div = x /2**y
    soma+=div
    x +=2
    y +=1

print ("%.2f" %(soma+1))    