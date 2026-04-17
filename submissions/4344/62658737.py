import sys
input = lambda:sys.stdin.readline().rstrip()

for i in range(int(input())) :
    n, *arr = map(int, input().split())
    avg = sum(arr) / n
    cnt = 0
    for j in arr :
        if j > avg :
            cnt += 1
    print(f'{cnt / n * 100:.3f}%')