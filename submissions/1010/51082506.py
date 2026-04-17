import math, sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(int(input())) :
    r, n = map(int, input().split())
    print(int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r))))