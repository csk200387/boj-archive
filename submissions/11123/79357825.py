import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    q = deque([(a, b)])
    cnt = 1
    arr[a][b] = "." 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if arr[nx][ny] == "#": 
                q.append((nx, ny))
                arr[nx][ny] = "." 
                cnt += 1
    res.append(cnt)

n = int(input())

for i in range(n):
    h, w = map(int, input().split())
    arr = [list(input()) for i in range(h)]
    res = []
    for x in range(h):
        for y in range(w):
            if arr[x][y] == "#":
                bfs(x, y)
    print(len(res))