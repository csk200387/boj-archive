import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
arr = [[] * (n+1) for i in range(n+1)]
vis = [0] * (n+1)
cnt = 1

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(v):
    global cnt
    q = deque([v])
    vis[v] = 1
    while q:
        v = q.popleft()
        arr[v].sort()
        for i in arr[v]:
            if not vis[i]:
                cnt += 1
                q.append(i)
                vis[i] = cnt

bfs(r)
print("\n".join(map(str, vis[1:])))