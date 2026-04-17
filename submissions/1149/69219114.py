import sys
input = sys.stdin.readline

n = int(input())
R, G, B = [], [],[]
dp = [[0,0,0] for i in range(n+1)]
for i in range(n):
    a,b,c = map(int, input().split())
    R += [a]
    G += [b]
    B += [c]

dp[1] = [R[0], G[0], B[0]]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + R[i-1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + G[i-1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + B[i-1]

print(min(dp[n]))