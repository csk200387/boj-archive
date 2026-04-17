import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for l in range(n) :
    a = input().split()
    for i in range(m) :
        arr[l][i] = 2126*int(a[i*3])+7152*int(a[(i*3)+1])+722*int(a[(i*3)+2])
for i in arr :
    for l in i :
        if l < 510_000 :
            print("#", end="")
        elif l < 1_020_000 :
            print("o", end="")
        elif l < 1_530_000 :
            print("+", end="")
        elif l < 2_040_000 :
            print("-", end="")
        else :
            print(".", end="")
    print()