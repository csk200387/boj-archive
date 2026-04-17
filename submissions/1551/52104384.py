t, n = input().split()
arr = [*map(int,(input().split(",")))]
tmp = []
for _ in range(int(n)) :
    for i in range(1,len(arr)) :
        tmp += [arr[i]-arr[i-1]]
    arr = tmp
    tmp = []
print(*arr, sep=",")