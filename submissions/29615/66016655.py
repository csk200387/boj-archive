import sys
input = lambda:sys.stdin.readline().rstrip()
n_size, m = map(int, input().split())
N = list(map(int, input().split()))
M = list(map(int, input().split()))
t = len(M)
first = set(N[:t])
while M:
    tmp = M.pop()
    if tmp in first:
        t -= 1
print(t)