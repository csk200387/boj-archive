import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
c = int(input())

arr = [[0] * (n+1) for i in range(n+1)]
vis = [False] * (n+1)

for i in range(c):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def bfs(v):
    q = deque([v])
    vis[v] = True
    while q:
        v = q.popleft()
        for i in range(1, n+1):
            if not vis[i] and arr[v][i]:
                q.append(i)
                vis[i] = True
bfs(1)
print(vis.count(True)-1)