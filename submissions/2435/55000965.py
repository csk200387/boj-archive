n, a = map(int, input().split())
arr = list(map(int, input().split()))
sample = sum(arr[0:a])
tmp = []
tmp.append(sample)
for i in range(a, n) :
    tmp.append(tmp[-1]-arr[i-a]+arr[i])

print(max(tmp))