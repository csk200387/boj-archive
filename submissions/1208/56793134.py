from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = sum([list(combinations(arr, i)).count(sub) for i in range(1, N+1) for sub in list(combinations(arr, i)) if sum(sub) == S])
print(count)