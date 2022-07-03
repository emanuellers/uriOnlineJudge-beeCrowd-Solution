while True:
    entries = int(input())
    if entries == 0:
        break
    correctQuestions = ""
    totalTime = 0
    map = {}
    for i in range(entries):
        solution = input().split()
        if solution[0] not in correctQuestions and solution[2] == "incorrect":
            if solution[0] in map.keys():
                map[solution[0]] += 20
            else:
                map[solution[0]] = 20
        else:
            if solution[0] not in correctQuestions:
                correctQuestions += solution[0]
                if solution[0] in map.keys():
                    map[solution[0]] += int(solution[1])
                else:
                    map[solution[0]] = int(solution[1])
    for j in correctQuestions:
        totalTime += map[j]
    print(f"{len(correctQuestions)} {totalTime}")
