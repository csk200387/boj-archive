from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]

dx = [0, 1]
dy = [1, 0]

def bfs():
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or ny >= n:
                continue
            if arr[nx][ny] == 1:
                q.append((nx, ny))
            if nx == m-1 and ny == n-1:
                return "Yes"
    return "No"

print(bfs())