tmp = list(map(int, input().split()))
arr = [1, 1, 2, 2, 2, 8];
res = [];
for i in range(6) :
    res.append(arr[i] - tmp[i])
print(*res, sep=" ")