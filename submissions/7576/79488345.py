from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = []

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

bfs()

for i in arr:
    if 0 in i:
        print(-1)
        exit()
    res.append(max(i))

print(max(res) - 1)