import sys
from collections import defaultdict
from math import floor
input = lambda:sys.stdin.readline().rstrip()

d = defaultdict(int)
for i in range(int(input())):
    k,v = input().split()
    d[k] += int(v)
t = list(d.values())
for i in t:
    if floor(i*1.618) in t and t.index(floor(i*1.618)) != t.index(i):
        print("Delicious!")
        exit()
print("Not Delicious...")