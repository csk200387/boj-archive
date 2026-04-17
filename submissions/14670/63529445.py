import sys
input = lambda:sys.stdin.readline().rstrip()
d = {}
for i in range(int(input())):
    a, b = input().split()
    d[a] = b
for i in range(int(input())) :
    ar = input().split()

    for j in ar[1::]:
        if j in d:
            print(d[j], end=' ')
        else:
            print("YOU DIED", end=' ')
    print()