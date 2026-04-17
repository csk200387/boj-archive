import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for line in range(n):
    n, m = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    cnt = 0
    start = 0
    for i in range(n):
        while True:
            if start == m or A[i] <= B[start]:
                cnt += start
                break
            else:
                start += 1
    print(cnt)