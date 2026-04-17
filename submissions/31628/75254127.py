import sys
input = lambda:sys.stdin.readline().rstrip()
arr = [input().split() for i in range(10)]
for i in range(10):
    if len(set(arr[i])) == 1 or len(set(arr[x][i] for x in range(10))) == 1:
        print(1)
        exit()
print(0)