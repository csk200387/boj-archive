import sys
input = lambda:sys.stdin.readline().rstrip()
arr = []
arrSize = int(input().split()[0])
for _ in range(arrSize) :
    arr.append(list(map(int,input().split())))

num = int(input())
for _ in range(num) :
    i,j,x,y = map(int,input().split())
    tmp = 0
    for A in range(i-1,x) :
        for B in range(j-1, y) :
            tmp += arr[A][B]
    print(tmp)