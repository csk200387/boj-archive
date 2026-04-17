from collections import deque
I=input;n,m=map(int,I().split());M=[list(map(int,I()))for _ in range(n)];X,Y=[-1,1,0,0],[0,0,-1,1];q=deque([(0,0)]);M[0][0]=0
while q:
 x,y=q.popleft()
 for i in range(4):
  p,o=x+X[i],y+Y[i]
  if 0<=p<n and 0<=o<m and M[p][o]==1:M[p][o]=M[x][y]+1;q.append((p,o))
print(M[n-1][m-1]+1)