a,b = input(), input()
dp = [[0]*(len(a)+1) for i in range(len(b)+1)]
for x in range(1, len(a)+1):
    for y in range(1, len(b)+1):
        if a[x-1] == b[y-1]:
            dp[y][x] = dp[y-1][x-1] + 1
print(max(map(max, dp)))