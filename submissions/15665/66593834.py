from itertools import product
n, m = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
cmb = list(product(arr, repeat=m))
cmb.sort()
for c in cmb:
    print(*c)