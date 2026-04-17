import sys
input = lambda:sys.stdin.readline().rstrip()
t = input()
n = int(input())
s = 0
for i in range(n):
    tmp = input()*2
    if t in tmp:
        s += 1
print(s)