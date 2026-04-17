from collections import deque
n,m=map(int,input().split())
M=[list(map(int,input())) for _ in range(n)]
X,Y=[-1,1,0,0],[0,0,-1,1]
q=deque([(0,0)])
M[0][0]=0
while q:
 x,y=q.popleft()
 for i in range(4):
  nx,ny = x+X[i], y+Y[i]
  if 0<=nx<n and 0<=ny<m and M[nx][ny]==1:
   M[nx][ny]=M[x][y]+1
   q.append((nx,ny))
print(M[n-1][m-1]+1)