import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for i in range(n)]
for i in range(1,n-1):
    arr[0] = arr[0] + arr[1]
    arr[1] = arr[0]
    arr.sort()
print(eval("+".join(map(str,arr))))