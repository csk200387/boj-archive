import sys
input = sys.stdin.readline
tm = []
a = int(input())
arr = input().rstrip().split()
for i in range(a) :
    if arr[i] in tm :
        print(arr[i])
        break
    else :
        tm.append(arr[i])