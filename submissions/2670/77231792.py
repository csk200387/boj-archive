import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = [float(input()) for i in range(n)]

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]*arr[i], arr[i])
print(dp)
print(f"{max(dp):.3f}")