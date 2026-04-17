import sys
input = lambda:sys.stdin.readline().rstrip()
s = int(input())
arr = list(map(int, input().split()))
dp = [0] * (s+1)
for i in range(1, s+1):
    dp[i] = dp[i-1] + arr[i-1]
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(dp[b]-dp[a-1])