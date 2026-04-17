from itertools import combinations
size = int(input())
arr = list(map(int, input().split()))
count = 0
for i in combinations(arr, 2):
    a,b = i
    count += a*b
print(count)