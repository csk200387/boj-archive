import sys
input = lambda:sys.stdin.readline().rstrip()

def afunc(target, arr):
    start = 0
    end = len(arr) - 1
    result = None
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] >= target:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result
def bfunc(target, arr):
    start = 0
    end = len(arr) - 1
    result = None
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] <= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

_, m = map(int, input().split())

arr = list(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    ar, br = afunc(a, arr), bfunc(b,arr)
    if ar is None:
        ar = 0
    if br is None:
        br = 0
    # print(arr[ar], arr[br])
    print(br-ar + 1)