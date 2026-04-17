import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = [input() for i in range(n)]
arr_s = [arr[i].replace("G", "R") for i in range(n)]
visT = [[0]*n for i in range(n)]
visF = [[0]*n for i in range(n)]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def bfs(a, b, target, vis, arr):
    q = deque([(a, b)])
    vis[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if vis[nx][ny] == 0 and arr[nx][ny] == target:
                vis[nx][ny] = 1
                q.append((nx, ny))

T, F = 0, 0
for i in range(n):
    for j in range(n):
        if visT[i][j] == 0:
            bfs(i, j, arr[i][j], visT, arr)
            T += 1
        if visF[i][j] == 0:
            bfs(i, j, arr_s[i][j], visF, arr_s)
            F += 1

print(T, F)