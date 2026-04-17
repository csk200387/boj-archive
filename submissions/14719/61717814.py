input()
arr = list(map(int, input().split()))
m = min(arr[0], arr[-1])
rain = 0
for i in range(1, len(arr)-1):
    l = max(arr[:i])
    r = max(arr[i+1:])
    m = min(l, r)
    if m > arr[i]:
        rain += m-arr[i]
print(rain)