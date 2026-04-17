import sys
input = lambda:int(sys.stdin.readline().rstrip())
n = input()
for i in range(n):
    d = input()
    mx = d
    while d != 1:
        if mx < d:
            mx = d
        if d % 2 == 0:
            d //= 2
        elif d % 2 == 1:
            d = d*3 + 1
    print(mx)