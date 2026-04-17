import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = []
res = [0] * n
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(3):
    s = [arr[j][i] for j in range(n)]
    for j in range(n):
        if s.count(arr[j][i]) == 1:
            res[j] += arr[j][i]

print(*res, sep="\n")