import sys
input = lambda:sys.stdin.readline().rstrip()
while True:
    n, m = map(int, input().split())
    if n == m == 0:break
    N = {input() for i in range(n)}
    M = {input() for i in range(m)}
    print(len(N & M))