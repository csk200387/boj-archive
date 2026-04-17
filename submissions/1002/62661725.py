import sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(int(input())) :    
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == r1 + r2 or dist == abs(r1 - r2):
        print(1)
    elif dist > r1 + r2 or dist < abs(r1 - r2):
        print(0)
    else:
        print(2)