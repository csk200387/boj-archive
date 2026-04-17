import sys
input = lambda:sys.stdin.readline().rstrip()
arr = [input().split() for i in range(10)]
cnt = 0
for i in range(10):
    if len(set(arr[i])) == 1:
        cnt += 1
    if len(set(arr[x][i] for x in range(10))) == 1:
        cnt += 1
print(cnt)