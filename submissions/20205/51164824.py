import sys
input = lambda:sys.stdin.readline().rstrip()

dum1, dum2 = map(int, input().split())
width, length = dum1, dum2
ar = []
for i in range(dum1) :
    ar.append(input().replace(" ",""))

for i in range(len(ar)) :
    tmp = []
    for l in ar[i] :
        for m in range(length) :
            tmp.append(l)
    ar[i] = " ".join(tmp)

for i in range(dum1) :
    for _ in range(width) :
        print(ar[i])