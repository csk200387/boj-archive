for _ in range(int(input())) :
    numList = list(map(int, input().split()))
    evenNumList = []
    for i in numList :
        if i%2 == 0 :
            evenNumList.append(i)
    print(sum(evenNumList), min(evenNumList))