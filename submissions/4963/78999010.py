from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]


def bfs(a, b):
    q = deque([(a, b)])
    arr[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue 

            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0

while True:
    m, n = map(int, input().split())
    if n == m == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)