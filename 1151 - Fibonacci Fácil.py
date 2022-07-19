number = int(input())
x = 0
z = 1
y = 0
for i in range(number):
    if i < number - 1:
        print("%d" % x ,end=' ')
    else:
        print("%d" % x, end='\n')
    x = z
    z += y
    y = x
