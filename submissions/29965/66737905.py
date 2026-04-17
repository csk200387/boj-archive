import sys
input = lambda:sys.stdin.readline().rstrip()

size = int(input())

m, j = 0, 0
ms, js = 0, 0

for _ in range(size):
    name, score = input().split()
    if name == 'M':
        m += 1
        ms += int(score)
    else:
        j += 1
        js += int(score)

m_avg = ms/m if m else 0
j_avg = js/j if j else 0

if m_avg == j_avg:
    print("V")
elif m_avg > j_avg:
    print("M")
else:
    print("J")