from collections import deque
n,m=map(int,input().split())
M=[[*map(int,input())] for _ in range(n)]
X,Y=[-1,1,0,0],[0,0,-1,1]
q=deque([(0,0)])
M[0][0]=0
while q:x,y=q.popleft();q+=[(x+i,y+j:=y+1-j)]*(0<=x+i<n and 0<=y+j<m and M[x+i][y+j]==1 and (M[x+i][y+j]=M[x][y]+1))
print(M[n-1][m-1]+1)