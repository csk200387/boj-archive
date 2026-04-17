num = int(input())
for i in range(num):
    score, result = 0, 0
    data = input()
    for i in data:
        if i == "O":
            score += 1
            result += score
        else:
            score = 0
    print(result)