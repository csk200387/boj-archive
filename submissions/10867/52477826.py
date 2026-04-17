import sys
input = lambda:sys.stdin.readline().rstrip()
input()
a = sorted(set(list(map(int,input().split()))))
print(*a)