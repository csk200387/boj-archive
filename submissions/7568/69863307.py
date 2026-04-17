import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [tuple(map(int, input().split())) for i in range(n)]
for i in range(n):
    cnt = 1
    for l in range(n):
        if arr[i][0] < arr[l][0] and arr[i][1] < arr[l][1]:
            cnt += 1
    print(cnt)