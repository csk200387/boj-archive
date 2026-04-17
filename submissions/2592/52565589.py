import sys
from collections import Counter
input = lambda:sys.stdin.readline().rstrip()
ls = []
for i in range(10) :
    ls.append(int(input()))
print(int(sum(ls)/10))
print(Counter(ls).most_common()[0][0])