import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
tmp = [arr[0]]
for i in range(n):
    if tmp[-1][1] <= arr[i][0]:
        tmp += [arr[i]]
print(len(tmp))