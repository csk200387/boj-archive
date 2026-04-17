import sys
inp = lambda:sys.stdin.readline().strip().split()
N, M = map(int, input())
arr = [[*map(int,input())] for _ in range(N)]
for i in range(N) :
    tmp = list(map(int, inp()))
    for l in range(M) :
        arr[i][l] += tmp[l]
    print(*arr[i])