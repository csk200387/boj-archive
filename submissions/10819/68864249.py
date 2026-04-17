from itertools import permutations

def get_sum(arr):
    r = 0
    for i in range(1, len(arr)):
        r += abs(arr[i-1]-arr[i])
    return r
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
for i in permutations(arr, len(arr)):
    tmp = get_sum(i)
    if tmp > res:
        res = tmp
print(res)