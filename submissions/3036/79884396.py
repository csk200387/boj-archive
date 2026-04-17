from math import gcd
n = int(input())
s, *arr = list(map(int, input().split()))
for i in arr:
    g = gcd(s, i)
    print(f"{s//g}/{i//g}")