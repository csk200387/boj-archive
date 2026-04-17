from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
vis = [[0]*m for i in range(n)]

def bfs(a, b):
    q = deque([(a, b)])
    vis[a][b] = 1
    while q:
        x, y = q.popleft()
        if arr[x][y] == "-":
            nx, ny = x, y+1
        elif arr[x][y] == "|":
            nx, ny = x+1, y

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if not vis[nx][ny] and arr[nx][ny] == arr[x][y] == "-":
            q.append((nx, ny))
            vis[nx][ny] = 1
        elif not vis[nx][ny] and arr[nx][ny] == arr[x][y] == "|":
            q.append((nx, ny))
            vis[nx][ny] = 1

cnt = 0
for x in range(n):
    for y in range(m):
        if not vis[x][y]:
            bfs(x, y)
            cnt += 1

print(cnt)