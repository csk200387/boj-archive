import sys
input = lambda:sys.stdin.readline().rstrip()

while True:
    l, w, a = map(int, input().split())
    if l == w == a == 0:
        break
    if a == 0:
        print(l, w, l*w)
        continue
    if l == 0:
        print(int(a/w), w, a)
        continue
    if w == 0:
        print(l, int(a/l), a)
        continue