import sys
input = lambda:sys.stdin.readline().rstrip()
N, M = map(int, input().split())
S = {input() for _ in range(N)}
r = 0
for _ in range(M):
    if input() in S:
        r += 1
print(r)