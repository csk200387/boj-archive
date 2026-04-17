from itertools import combinations
L, C = map(int, input().split())
arr = sorted(input().split())
for i in combinations(arr, L) :
    j = 0
    m = 0
    for l in ["a", "i", "u", "e", "o"] :
        if l in i :
            m += 1
        else :
            j += 1
    if j >= 2 and m >= 1 :
        print(*i, sep="")