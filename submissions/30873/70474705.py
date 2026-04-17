import sys
input = lambda:sys.stdin.readline().rstrip()
now = 0
for i in range(int(input())):
    p, c = map(int, input().split())
    if abs(p-now) <= c:
        now += 1
print(now)