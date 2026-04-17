import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for line in range(1, n+1):
    a, b = map(int, input().split())
    A, B = int(a**(1/3)), int(b**(1/3))
    print(f"Case #{line}:", B-A+(B==b**(1/3))+(A==a**(1/3)))