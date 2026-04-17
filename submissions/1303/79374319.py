import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a, b, t):
    q = deque([(a, b)])
    cnt = 1
    vis[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if arr[nx][ny] == t and not vis[nx][ny]:
                q.append((nx, ny))
                vis[nx][ny] = 1
                cnt += 1
    return cnt

n, m = map(int, input().split())
w, b = 0, 0
vis = [[0] * n for i in range(m)]
arr = [list(input()) for i in range(m)]

for x in range(m):
    for y in range(n):
        if arr[x][y] == "W" and not vis[x][y]:
            tmp = bfs(x, y, "W")
            w += tmp**2 
        elif arr[x][y] == "B" and not vis[x][y]:
            tmp = bfs(x, y, "B")
            b += tmp**2 

print(w, b)