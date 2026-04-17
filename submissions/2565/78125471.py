import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
lis = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if arr[i][1] > arr[j][1] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1
print(n - max(lis))