arr = [*map(int, list(input()))]
for i in range(len(arr)-1, 0, -1):
    if arr[i] >= 5:
        arr[i] = 0
        arr[i-1] += 1
    else :
        arr[i] = 0
    if arr[i-1] == 10:
        arr[i-1] = 0
        if i-2 < 0:
            arr.insert(0, 1)
        else:
            arr[i-2] += 1
print(*arr, sep="")