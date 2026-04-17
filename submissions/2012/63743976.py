import sys
input = lambda:sys.stdin.readline().rstrip()
r = 10**8
for i in range(int(input())):
    s = int(input())
    if abs((i+1)-s) < r:
        r = i+1
print(r)