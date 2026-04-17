import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
arr = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

vis = [False] * (n+1)

def bfs(v):
    q = deque([v])
    vis[v] = True
    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for i in range(1, n+1):
            if not vis[i] and arr[v][i] == 1:
                q.append(i)
                vis[i] = True
    return res
print(*(bfs(r)+[0]), sep="\n")