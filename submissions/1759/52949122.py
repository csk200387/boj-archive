from itertools import combinations
L, C = map(int, input().split())
arr = sorted(input().split())
for i in combinations(arr, L) :
    bol = False
    for l in ["a", "i", "u", "e", "o"] :
        if l in i :
            bol = True
    if bol :
        print(*i, sep="")