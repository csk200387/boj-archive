import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    a, b = 0, 1
    p, q = map(int, input().split())
    for _ in range(p-1):
        a, b = b%q, (a+b)%q
    print(f"Case #{i+1}: {b}")