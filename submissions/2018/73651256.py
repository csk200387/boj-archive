n = int(input())
cnt = 0
for s in range(1, n+1):
    sum = 0
    while sum < n:
        sum += s
        s += 1
    if sum == n:
        cnt += 1
print(cnt)