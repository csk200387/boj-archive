import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [int(input()) for i in range(n)]
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(n - max(dp))