from collections import deque
import sys
input = lambda:sys.stdin.readline().strip()
def bfs(maze, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))
    maze[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N-1][M-1]+1
N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, list(input()))))
print(bfs(board, N, M))