import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for i in range(n)]
res = 0
for i in range(0,n-1):
    arr.sort()
    arr[0] = arr[0] + arr[1]
    res += arr[0]
    del arr[1]
print(res)