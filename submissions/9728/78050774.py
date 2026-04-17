import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    arr = sorted(map(int, input().split()))
    start, end = 0, n-1
    cnt = 0
    while start <= end:
        tmp = arr[start] + arr[end]
        if tmp < m:
            start += 1
        elif tmp > m:
            end -= 1
        else:
            start += 1
            end -= 1
            cnt += 1
    print(f"Case #{i+1}: {cnt}")