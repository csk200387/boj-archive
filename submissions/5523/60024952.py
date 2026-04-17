import sys
input = lambda:sys.stdin.readline().rstrip()
A,B = 0, 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        A += 1
    elif b > a:
        B += 1
print(A,B)