import sys
input = lambda:sys.stdin.readline().rstrip()
l = [input().split() for _ in range(int(input()))]
l.sort(key=lambda x:x[0])
for i in l :
    print(*i)