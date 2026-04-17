import sys
input = lambda:sys.stdin.readline().rstrip()

dum1, dum2, width, length = map(int, input().split())
ar = []
for i in range(dum1) :
    ar.append(input())

for i in range(len(ar)) :
    tmp = []
    for l in ar[i] :
        for m in range(length) :
            tmp.append(l)
    ar[i] = "".join(tmp)

for i in range(dum1) :
    for _ in range(width) :
        print(ar[i])