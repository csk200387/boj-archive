import sys
input = sys.stdin.readline
for _ in range(int(input())):
    c, m = map(int, input().split())
    a, b = 1, 1
    cnt = 0
    while True:
        a, b = b, (a+b)%m
        cnt += 1
        if a == b == 1:
            break
    print(c, cnt)