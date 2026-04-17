from itertools import combinations
_, g = map(int, input().split())
ar = [*map(int, input().split())]
comb = [*combinations(ar, 3)]
t = sorted([sum(i) for i in comb])
print(min(t, key=lambda x:abs(x-g)))