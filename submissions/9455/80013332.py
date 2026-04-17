import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(m)]
    res = 0
    for l in range(n):
        tmp = 0
        for i in range(m-1, -1, -1):
            if arr[i][l] == 1:
                res += tmp
            else:
                tmp += 1
    print(res)