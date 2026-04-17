num = int(input(""))
for i in range(0,num):
    score = 0
    result = 0
    data = input("")
    for i in data:
        if(i == "O"):
            score += 1
            result += score
        else :
            score = 0
    print(result)