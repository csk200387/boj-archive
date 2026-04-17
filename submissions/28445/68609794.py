from itertools import product
d = set()
for i in range(2):
    d.update(input().split())
for line in sorted(product(d, d)):
    print(*line)