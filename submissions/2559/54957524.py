n, a = map(int, input().split())
arr = list(map(int, input().split()))
tmp = []
for i in range(len(arr)) :
    t = arr[i:a+i]
    if len(t) != a :
        break
    else :
        tmp.append(sum(t))
print(max(tmp))