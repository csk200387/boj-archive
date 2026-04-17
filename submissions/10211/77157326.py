import sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(int(input())):
    s = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (s+1)
    dp[0] = arr[0]
    for i in range(1, s):
        dp[i] = max(dp[i-1]+arr[i], arr[i])
    print(max(dp))