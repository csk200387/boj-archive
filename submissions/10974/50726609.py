from itertools import *
a = int(input())
ar = list(range(1,a+1))
l = list(permutations(ar, a))
for i in l :
    print(" ".join(list(map(str,i))))