import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
c = int(input())
s = {1}
for i in range(c):
    a, b = map(int, input().split())
    if a in s or b in s:
        s.add(a)
        s.add(b)
print(len(s)-1)