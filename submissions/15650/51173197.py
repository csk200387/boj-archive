from itertools import *
ran, size = map(int, input().split())
li = list(range(1,ran+1))
for i in sorted(permutations(li, size)) :
  print(" ".join(list(map(str,i))))