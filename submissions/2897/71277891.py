import sys
input = lambda:sys.stdin.readline().rstrip()
x, y = map(int, input().split())
arr = [input() for i in range(x)]
res = [0, 0, 0, 0, 0]
for l in range(1, x):
    for i in range(1, y):
        tmp = [arr[l][i], arr[l-1][i], arr[l-1][i-1], arr[l][i-1]]
        if '#' in tmp:
            continue
        res[tmp.count('X')] += 1
print(*res, sep="\n")