import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
mx = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        mx = a if mx < a else mx
print(mx if mx else -1)