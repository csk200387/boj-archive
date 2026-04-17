arr = []
for i in range(5) :
    arr.append(input())
for i in range(15) :
    for l in range(15) :
        try :
            print(arr[l][i], end="")
        except :
            continue