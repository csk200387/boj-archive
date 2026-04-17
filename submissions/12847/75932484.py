s,n = map(int, input().split())
arr = list(map(int, input().split()))
s = sum(arr[:n])
mx = s
for i in range(n, len(arr)):
    s -= arr[i-n]
    s += arr[i]
    if s > mx:
        mx = s
print(mx)