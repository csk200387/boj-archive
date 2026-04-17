import sys
c=sys.stdin.readline
while 1:
 n,m=map(int,input().split())
 if n==m==0:break
 print(len({c()for i in range(n)}&{c()for i in range(m)}))