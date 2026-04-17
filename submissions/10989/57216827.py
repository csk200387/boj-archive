import sys
from collections import Counter
input = lambda:int(sys.stdin.readline().rstrip())
ar = Counter(input()-1 for _ in range(input()))
ar.sort()
for i in ar :
    print((str(i+1)+"\n")*ar[i], end="")