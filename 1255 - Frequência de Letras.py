entries = int(input())

for i in range(entries):
    map = {}
    max = 0
    text = input().lower()
    for j in text:
        if j.isalpha():
            if  j in map.keys():
                map[j] += 1
                if map[j] > max:
                    max = map[j]
            else:
                map[j] = 1
                if map[j] > max:
                    max = map[j]
    letters = []
    for key, value in map.items():
        if value == max:
            letters.append(key)
    letters.sort()
    print("".join(letters))
