

import math

inputs = int(input())

for i in range(inputs):
    number = int(input())
    if number == 1:
        print("Prime")
    else:
        isPrime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                isPrime = False
                break
        if isPrime:
            print("Prime")
        else:
            print("Not Prime")
       
