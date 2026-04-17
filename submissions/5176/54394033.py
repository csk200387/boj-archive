import sys
input = lambda:int(sys.stdin.readline().rstrip().split()[0])
for _ in range(input()) :
    arr = []
    for _ in range(input()) :
        arr.append(input())
    print(len(arr)-len(set(arr)))