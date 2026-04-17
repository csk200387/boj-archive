import sys
input = lambda:sys.stdin.readline().rstrip()

arr = []
sar = set()
for i in range(int(input())):
    arr.append(input())
    sar.add(arr[i])

s = arr.index("?")

if 0 < s and s < len(arr)-1:
    start = arr[s-1][-1]
    end = arr[s+1][0]
    n = int(input())
    tmp = [input() for i in range(n)]
    for i in range(n):
        if tmp[i] not in sar:
            if tmp[i].startswith(start) and tmp[i].endswith(end):
                print(tmp[i])
                break

elif s == 0 and len(arr) == 1:
    for _ in range(int(input())):
        print(input())

elif s == 0:
    end = arr[s+1][0]
    n = int(input())
    tmp = [input() for i in range(n)]
    for i in range(n):
        if tmp[i] not in sar:
            if tmp[i].endswith(end):
                print(tmp[i])
                break

elif s == len(arr)-1:
    start = arr[s-1][-1]
    n = int(input())
    tmp = [input() for i in range(n)]
    for i in range(n):
        if tmp[i] not in sar:
            if tmp[i].startswith(start):
                print(tmp[i])
                break