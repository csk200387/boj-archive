import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())

arr = []

for _ in range(n):
    a, b = input().split()
    arr.append([a,int(b)])

arr.sort(key=lambda x:x[1])

for line in range(m):
    data = int(input())
    right = n
    left = 0
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid][1] >= data:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(arr[res][0])