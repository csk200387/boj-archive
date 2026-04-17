import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

c, n = map(int, input().split())
if n == 0:
    print(c)
    exit()

arr = [[0] * (c+1) for i in range(c+1)]
vis = [False] * (c+1)
for i in range(n):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

def bfs(v):
    q = deque([v])
    vis[v] = True
    while q:
        v = q.popleft()
        for i in range(1, c+1):
            if not vis[i] and arr[v][i]:
                q.append(i)
                vis[i] = True
cnt = 0
for i in range(1, c+1):
    if not vis[i]:
        bfs(i)
        cnt += 1
print(cnt)