import sys
input = lambda:sys.stdin.readline().rstrip()
cs = int(input())
for c in range(cs):
    n = int(input())
    arr = sorted(list(map(int, input().split())) for i in range(n))
    cnt = 0
    m = arr[0][1]
    for i in range(1, n):
        if m > arr[i][1]:
            cnt += 1
            m = arr[i][1]
    print(cnt+1)