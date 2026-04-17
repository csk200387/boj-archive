import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, 101):
    dp.append(dp[i-1]+dp[i-5])

for _ in range(n):
    tmp = int(input())
    print(dp[tmp-1])