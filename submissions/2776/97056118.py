import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    input()
    s1 = set(map(int, input().split()))
    input()
    arr = list(map(int, input().split()))
    for n in arr:
        if n in s1:
            print(1)
        else:
            print(0)