import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())) :
    C, G = 0, 0
    for i in range(int(input())) :
        A, B = map(float, input().split())
        C += A
        G += A*B
    c = G/C
    print(f"{C:.0f} {c:.1f}")