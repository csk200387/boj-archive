import sys
input = lambda:sys.stdin.readline().strip()

n, k = map(int, input().split())
dp = [1] + [0] * k
for _ in range(n) :
    c = int(input())
    for i in range(c, k+1) :
        dp[i] += dp[i-c]
print(dp[k])