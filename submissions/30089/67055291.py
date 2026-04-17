import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    s = input()
    for i in range(len(s), 0, -1):
        t = s+s[::-1][i:]
        if t == t[::-1]:
            print(t)
            break