import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
dp = [1, 1, 2, 4]
for i in range(4, 68):
    dp.append(dp[i-4] + dp[i-3] + dp[i-2] + dp[i-1])

for i in range(n):
    l = int(input())
    print(dp[l])