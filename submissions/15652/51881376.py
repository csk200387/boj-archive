from itertools import combinations_with_replacement
a, b = map(int,input().split())
ar = [*range(1,a+1)]
for i in combinations_with_replacement(ar, b) :
    print(*i)