from itertools import *
ran, size = map(int, input().split())
li = list(range(1,ran+1))
ar = sorted(combinations(li, size))
for i in ar :
    print(" ".join(list(map(str,i))))    