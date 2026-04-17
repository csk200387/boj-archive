import sys
input = lambda:sys.stdin.readline().rstrip()
a = list(map(int,input().split()))
print(sum(range(min(a), max(a)+1)))