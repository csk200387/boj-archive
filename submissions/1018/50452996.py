# □ ■
import sys
inp = list(map(int,input().split()))
width = inp[0]
length = inp[1]
origin = []
ch = 0
for i in range(length):
    if i%2 == 1 :
        a = []
        for d in range(width):
            if d%2 == 0 :
                a.append("B")
            if d%2 == 1 :
                a.append("W")
        origin.append("".join(a))
    if i%2 == 0 :
        a = []
        for d in range(width):
            if d%2 == 0 :
                a.append("W")
            if d%2 == 1:
                a.append("B")
        origin.append("".join(a))

for i in range(length):
    a = sys.stdin.readline()
    for l in a:
        if l != origin[i] :
            ch += 1
print(ch)