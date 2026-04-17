import sys
input = lambda:sys.stdin.readline().rstrip()

def afunc(target, arr):
    start = 0
    end = len(arr) - 1
    result = None
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end 
def bfunc(target, arr):
    start = 0
    end = len(arr) - 1
    result = None
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
    ar, br = bfunc(a, arr), afunc(b,arr)
    print(br-ar + 1)