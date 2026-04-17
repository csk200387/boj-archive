n, m = map(int, input().split())
arr = list(map(int, input().split()))
mx = []
sm = 0
end = 0
for start in range(n):
    while sm < m and end < n:
        sm += arr[end]
        end += 1
    if m >= sm:
        mx.append(sm)
    sm -= arr[start]
print(max(mx))