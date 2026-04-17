import sys
input = lambda:sys.stdin.readline().rstrip()
dp = [0, 1] + [0]*9999
n = int(input())
for i in range(2, 10001):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(n):
    p, q = map(int, input().split())
    r = dp[p]%q
    print(f"Case #{i+1}: {r}")