import sys
from collections import deque

def main():
    input = lambda:sys.stdin.readline().rstrip()
    print_ = print

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    c = list(map(int, input().split()))

    arr = deque()

    for i in range(n):
        if a[i] == 0:arr.appendleft(b[i])

    for i in range(m):
        arr.append(c[i])
        print_(arr.popleft(), end=' ')

main()