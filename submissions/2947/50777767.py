arr = list(map(int,input().split()))

for i in range(len(arr)) :
    for l in range(len(arr)-1) :
        if arr[l] > arr[l+1] :
            tmp = arr[l+1]
            arr[l+1] = arr[l]
            arr[l] = tmp
        else :
            continue
        print(" ".join(map(str,arr)))