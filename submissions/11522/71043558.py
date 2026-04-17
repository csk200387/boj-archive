import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    line, N = map(int, input().split())
    s1 = N * (N + 1) // 2
    s2 = N ** 2
    s3 = N ** 2 + N
    print(f"{line} {s1} {s2} {s3}")