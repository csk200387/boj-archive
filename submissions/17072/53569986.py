import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for l in range(n) :
    a = input().split()
    for i in range(m) :
        tmp = 2126*int(a[i*3])+7152*int(a[(i*3)+1])+722*int(a[(i*3)+2])
        if tmp < 510_000 :
            print("#", end="")
        elif tmp < 1_020_000 :
            print("o", end="")
        elif tmp < 1_530_000 :
            print("+", end="")
        elif tmp < 2_040_000 :
            print("-", end="")
        else :
            print(".", end="")
    print()