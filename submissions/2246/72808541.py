import sys
input = lambda:sys.stdin.readline().rstrip()
arr=[list(map(int,input().split())) for i in range(int(input()))]
arr.sort(key=lambda x:(x[0], x[1]))
c,r=10**8,0
for x,y in arr:
 if y<c:
  c=y
  r+=1
print(r)