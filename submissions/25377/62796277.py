import sys
input = lambda:sys.stdin.readline().rstrip()
r = 10**8
for i in range(int(input())) :
    a,b = map(int,input().split())
    if b-a >= 0:
        r = min(r, b)
if r == 10**8:
    print(-1)
else:
    print(r)