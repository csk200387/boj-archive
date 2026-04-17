import sys
from collections import defaultdict
input = lambda:sys.stdin.readline().rstrip()
d = defaultdict(int)
for i in range(int(input())):
    k,v = input().split()
    d[k] += int(v)
for k,v in d.items():
    if int(v*1.618) in d.values() and [*d.values()].index(int(v*1.618)) != [*d.values()].index(v):
        print("Delicious!")
        exit()
print("Not Delicious...")