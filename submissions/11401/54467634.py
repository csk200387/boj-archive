import math

n, k = map(int, input().split())
print(math.comb(n, k)%1_000_000_007)