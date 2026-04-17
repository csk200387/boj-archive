from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input())) for i in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = []

def bfs(a, b):
    q = deque([(a, b)])
    cnt = 1
    arr[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0
                cnt += 1
    res.append(cnt)

for i in range(n):
    for l in range(n):
        if arr[i][l] == 1:
            bfs(i, l)
print(len(res))
print(*sorted(res), sep="\n")