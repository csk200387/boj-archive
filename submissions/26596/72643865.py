import sys
from collections import defaultdict
input = lambda:sys.stdin.readline().rstrip()
d = defaultdict(int)
for i in range(int(input())):
    k,v = input().split()
    d[k] += int(v)
t = sorted(d.values())
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if int(t[i]*1.618) == t[j]:
            print("Delicious!")
            exit()
print("Not Delicious...")