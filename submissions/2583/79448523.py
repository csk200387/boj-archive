from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

m, n, k = map(int, input().split())
arr = [[0] * n for i in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = []

def bfs(a, b):
    q = deque([(a, b)])
    cnt = 1
    arr[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = 1
                cnt += 1
    res.append(cnt)

for x in range(m):
    for y in range(n):
        if arr[x][y] == 0:
            bfs(x,y)

print(len(res))
print(*sorted(res))