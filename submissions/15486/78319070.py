import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
dp = [0] * (n+1)
arr = [tuple(map(int, input().split())) for i in range(n)]
for i in range(n):
    for l in range(i+arr[i][0], n+1):
        if dp[l] < dp[i] + arr[i][1]:
            dp[l] = dp[i] + arr[i][1]
print(dp[n])