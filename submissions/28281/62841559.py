_, p = map(int, input().split())
arr = list(map(int, input().split()))
r = 10**10
for i in range(1, len(arr)):
    r = min(r, (arr[i-1]+arr[i])*p)
print(r)