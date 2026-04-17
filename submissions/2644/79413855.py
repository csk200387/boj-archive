from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

n = int(input())
a, b = map(int, input().split())

arr = [[] for i in range(n+1)]
vis = [-1] * (n+1)

for i in range(int(input())):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        for i in arr[v]: 
            if vis[i] == -1:
                q.append(i)
                vis[i] = vis[v] + 1

vis[a] = 0
bfs(a)
print(vis[b])