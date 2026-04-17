import sys
input = lambda:sys.stdin.readline().rstrip()
d,r = map(int,input().split())
dic = {}
for _ in range(d):
    a,b = input().split()
    dic[a] = b
for _ in range(r):
    a = input()
    print(dic[a])