from math import gcd
from itertools import combinations
for _ in range(int(input())) :
  arr = [*map(int, input().split())]
  arr.sort()
  print(sum([gcd(x,y) for x,y in combinations(arr[1:], 2)]))