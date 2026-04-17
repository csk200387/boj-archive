size, n = map(int,input().split())
arr = list(map(int,(input().split(","))))
tmp = []
for i in range(n) :
    for i in range(1,len(arr)) :
        tmp.append(arr[i]-arr[i-1])
    arr = tmp
    tmp = []
print(",".join(list(map(str,arr))))