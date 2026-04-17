import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = []
def bfs(a, b, vis, target):
    q = deque([(a, b)])
    cnt = 1
    vis[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] > target and not vis[nx][ny]:
                q.append((nx, ny))
                vis[nx][ny] = 1
                cnt += 1
    tmp.append(cnt)

for t in range(1, 10):
    tmp = []
    vis = [[0] * n for i in range(n)]
    for i in range(n):
        for l in range(n):
            if arr[i][l] > t and not vis[i][l]:
                bfs(i, l, vis, t)
    res.append(len(tmp))

print(max(res))