import sys
input = lambda:sys.stdin.readline().rstrip()

size = int(input())
m, j = 0, 0
mt, jt = 0, 0
for i in range(size):
    name, score = input().split()
    if name == "M":
        m += int(score)
        mt += 1
    else:
        j += int(score)
        jt += 1

if m/mt > j/jt:
    print("M")
elif m/mt == j/jt:
    print("V")
else:
    print("J")