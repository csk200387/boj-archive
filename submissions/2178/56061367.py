from collections import deque
n,m=map(int,input().split())
M=[list(map(int,input())) for _ in range(n)]
X,Y=[-1,1,0,0],[0,0,-1,1]
q=deque([(0,0)])
M[0][0]=0
while q:
 x,y=q.popleft()
 for i in range(4):
  x,y=x+X[i],y+Y[i]
   if 0<=x<n and 0<=y<m and M[x][y]==1:
    M[x][y]=M[x][y]+1
    q.append((x,y))
print(M[n-1][m-1]+1)