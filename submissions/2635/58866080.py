n = int(input())
result, l = [], 0
for i in range(1,n+1) :
    arr = [n, i]
    while True :
        t = arr[-2] - arr[-1]
        if t < 0 :
            break
        arr.append(t)
    if len(arr) > l :
        l = len(arr)
        result = arr
print(l)
print(*result)