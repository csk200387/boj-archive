import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0], x[1]))
stack = 0
for i in range(n):
    tmp = [arr[i]]
    for l in range(i+1, n):
        if tmp[-1][1] <= arr[l][0]:
            tmp.append(arr[l])
    if len(tmp) > stack:
        stack = len(tmp)
print(stack)