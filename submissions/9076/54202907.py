for i in range(int(input())) :
    scoreList = sorted(list(map(int, input().split())))
    scoreSum = sum(scoreList)
    score_mn = scoreList[1:4]
    if max(score_mn)-min(score_mn) > 3 :
        print("KIN")
    else :
        print(sum(score_mn))