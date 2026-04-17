from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())

def bfs(a, b):
    q = deque([(a, b)])
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


for line in range(n):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)