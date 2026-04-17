from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
stack = 0
for i in range(1, N+1) :
    t = combinations(arr, i)
    arr_t = [sum(l) for l in t]
    stack += arr_t.count(S)
print(stack)