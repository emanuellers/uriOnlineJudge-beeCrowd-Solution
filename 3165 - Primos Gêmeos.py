import math

def findPrime(number):
    if number != 5 and number % 5 == 0:
        return 0
    if number % 2 == 0 :
        return 0
    if number != 11 and  number % 11 == 0:
        return 0
    squareRoot = int(math. sqrt(number)) if number >= 1 else 1
    for j in range(3, squareRoot + 1):
        if  number % j == 0 :
            return 0
    else:
        return number
def firstPrimes(number):
    array = []
    for i in range(1, number+1):
        value = findPrime(i)
        if value != 0:
            array.append(value)
    twinPrimes = []
    for i in range(len(array)):
        if i != len(array) -1 and i != 0:
            if array[i +1] - array[i] <=2 or array[i] - array[i-1] <= 2:
                twinPrimes.append(array[i]) 
        elif i == 0:
            twinPrimes.append(array[i])
        elif i == len(array) -1 and array[i ] - array[i -1] == 2:
            twinPrimes.append(array[i])
    if findPrime(number) == number:
        twinPrimes.append(number)
    return twinPrimes


def findNearPrime(number):
    arrayPrimes = firstPrimes(number)[::-1]
    if arrayPrimes[0] - arrayPrimes[1] == 2:
        return arrayPrimes[0:2]
    else:
        return arrayPrimes[1:3]
  
numberInput = int(input())
result = findNearPrime(numberInput)
print(f"{result[1]} {result[0]}")
