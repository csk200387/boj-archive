import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
c = int(input())
s = {1}
r = []
for i in range(c):
    a, b = map(int, input().split())
    if a in s or b in s:
        s.add(a)
        s.add(b)
    r.append((a,b))

for x,y in r[::-1]:
    if x in s or y in s:
        s.add(x)
        s.add(y)
print(len(s)-1)