import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
arr = [[False] * (n+1) for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = True
    arr[y][x] = True

vdfs = [False] * (n+1)
vbfs = [False] * (n+1)

def dfs(v):
    q = deque([v])
    vdfs[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not vdfs[i] and arr[v][i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    vbfs[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not vbfs[i] and arr[v][i]:
                q.append(i)
                vbfs[i] = True

dfs(v)
print()
bfs(v)