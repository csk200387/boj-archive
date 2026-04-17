import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m+1) for i in range(n+1)]
dp[1][1] = arr[0][0]
for x in range(1, n+1):
    for y in range(1, m+1):
        dp[x][y] = max(dp[x-1][y], dp[x][y-1])
        dp[x][y] += arr[x-1][y-1]
print(dp[n][m])