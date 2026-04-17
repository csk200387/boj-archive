from itertools import combinations
n = int(input())
arr = []
for i in range(1, 11) :
    for ar in combinations(range(0, 10), i) :
        ar = sorted(ar, reverse=True)
        arr.append(int("".join(map(str, ar))))
print(sorted(arr)[n] if n < 1023 else "-1")