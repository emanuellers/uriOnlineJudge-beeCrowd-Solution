#1013 - O Maior
#Emanuelle Rodrigues
nums = input().split()
a, b, c = nums
a = int (a)
b = int (b)
c = int (c)
if a > b and a > c:
    print ("%d eh o maior" %a)
elif b > a and b > c:
    print ("%d eh o maior" %b)
elif c > a and c >b:
    print ("%d eh o maior" %c)