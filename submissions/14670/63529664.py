import sys
input = lambda:sys.stdin.readline().rstrip()
d = {}
for i in range(int(input())):
    a, b = input().split()
    d[a] = b
for i in range(int(input())) :
    ar = input().split()
    s = []
    for j in ar[1::]:
        if j in d:
            s.append(d[j])
        else:
            print("YOU DIED")
            s = []
            break
    if s:
        print(' '.join(s))