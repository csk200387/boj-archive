import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
pd = [1] * n
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        dp[i] += dp[i-1]
for i in range(1, n):
    if arr[i] <= arr[i-1]:
        pd[i] += pd[i-1]
print(max(max(dp), max(pd)))