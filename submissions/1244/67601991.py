import sys
input = lambda:sys.stdin.readline().rstrip()


def filp(n):
    if arr[n] == 0:
        arr[n] = 1
    else:
        arr[n] = 0
size = int(input())
arr = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    t, num = map(int, input().split())

    if t == 1:
        for i in range(num-1, size, num):
            filp(i)
    else:
        filp(num-1)
        for i in range(1, size):
            if num-1-i < 0 or num-1+i >= size:
                break
            if arr[num-1-i] == arr[num-1+i]:
                filp(num-1-i)
                filp(num-1+i)
            else:
                break

for i in range(0, size, 20):
    print(*arr[i:i+20])