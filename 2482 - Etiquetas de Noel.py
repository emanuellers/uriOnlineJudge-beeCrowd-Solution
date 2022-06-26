mapTranslation = {}
languagesAmount = int(input())
for i in range(languagesAmount):
    language = input()
    merryChristmas = input()
    mapTranslation[language] = merryChristmas
childrenAmount = int(input())
for i in range(childrenAmount):
    name = input()
    language = input()
    print(f'{name}\n{mapTranslation[language]}\n')
