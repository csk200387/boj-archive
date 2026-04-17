import sys
from collections import Counter
input = lambda:sys.stdin.readline().rstrip()
size = int(input())
arr = [input() for _ in range(size)]
t = sorted(Counter(arr).most_common(), key=lambda x: (x[1], x[0]), reverse=True)
print(*t[0])