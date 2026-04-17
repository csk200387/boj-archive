n = int(input())

adj = [[0] for i in range(n+1)]
p = [0] * (n+1)

def dfs(c):
    for i in adj[c]:
        if p[c] == i:
            continue
        p[i] = c
        dfs(i)

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
dfs(1)
for i in range(2, n+1):
    print(p[i])