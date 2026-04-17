import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = []
for _ in range(n):
    a, b = input().split()
    arr.append([a,int(b)])
for line in range(m):
    data = int(input())
    for i in range(n):
        if data <= arr[i][1]:
            print(arr[i][0])
            break
        else:
            continue