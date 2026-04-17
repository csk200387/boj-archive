import sys
from itertools import combinations_with_replacement

input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
stack = sorted(map(int , input().split()))
ans = sorted(set(list(combinations_with_replacement(stack, m))))
if m == 1:
    for t in range(0, len(ans)):
        s = list(ans[t])
        print(s[0])
else:
    for t in range(0,len(ans)):
        s = list(ans[t])
        for u in range(0,len(s)-1):
            print(s[u],end=" ")
        print(s[len(s)-1])