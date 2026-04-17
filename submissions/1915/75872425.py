import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
dp = [[0]*m for i in range(n)]
r = 0
for x in range(n):
    for y in range(m):
        if x == 0 or y == 0:
            dp[x][y] = int(arr[x][y])
        elif arr[x][y] == "0":
            dp[x][y] = 0
        else:
            dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
        r = max(dp[x][y], r)
print(r*r)