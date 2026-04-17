import sys, math
input = lambda:sys.stdin.readline().rstrip()
c = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr = [tuple(map(int, input().split())) for i in range(n)]
        print(f"Menu {c}:",min(arr, key=lambda x:x[1]/(math.pi*(x[0]/2)**2))[0])
    c += 1