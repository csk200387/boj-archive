from itertools import  *
a,b=map(int,input().split())
for i in sorted(list(set(permutations(map(int,input().split()), b)))) :
    print(*i)