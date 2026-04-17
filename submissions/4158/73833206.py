import sys
input = lambda:sys.stdin.readline().rstrip()
while True:
    n, m = map(int, input().split())
    if n == m == 0:break
    N = {str(i)+'_'+input() for i in range(n)}
    M = {str(i)+'_'+input() for i in range(m)}
    print(len(N & M))