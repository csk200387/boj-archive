import sys
input = lambda:sys.stdin.readline().rstrip()

def afunc(target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end 
def bfunc(target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1 

_, m = map(int, input().split())

arr = sorted(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    print(bfunc(a)+afunc(b)+1)