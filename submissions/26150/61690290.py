import sys
input = lambda:sys.stdin.readline().rstrip()
arr = []
for _ in range(int(input())):
    title, num, diff = input().split()
    arr.append((title, int(num), int(diff)))
arr.sort(key=lambda x: (-x[1], x[2], x[0]), reverse=True)
for i in arr:
    t = i[0]
    d = i[2]
    print((t[d-1]).upper(), end="")