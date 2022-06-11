albumSize = int(input())
bought = int(input())
imageNumber = []
for i in range(bought):
    number = input()
    if number not in imageNumber:
        imageNumber.append(number)

print(albumSize - len(imageNumber))
