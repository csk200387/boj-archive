import sys
input = sys.stdin.readline
a = input().rstrip().split()
N = int(a[0])
M = int(a[1])
arr = []
for i in range(N) :
    arr.append(list(map(int,input().rstrip().split())))
for i in range(N) :
    tmp = list(map(int,input().rstrip().split()))
    for l in range(M) :
        arr[i][l] += tmp[l]
    print(" ".join(list(map(str,arr[i]))))