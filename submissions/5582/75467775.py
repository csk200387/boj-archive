import sys
input = lambda:sys.stdin.readline().rstrip()
a = input()
b = input()
al = len(a)
bl = len(b)
dp = [[0]*(al+1) for i in range(bl+1)]
for x in range(1, al+1):
    for y in range(1, bl+1):
        if a[x-1] == b[y-1]:
            dp[y][x] = dp[y-1][x-1] + 1
print(max(map(max, dp)))