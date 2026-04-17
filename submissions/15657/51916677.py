from itertools import *
a, b = map(int,input().split())
ar = sorted(list(map(int,input().split())))
for i in combinations_with_replacement(ar, b) :
    print(*i)