import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())) :
    p, q, n = map(int, input().split())
    s = [(p%q)*(i%q)%q for i in range(1, n+1)]
    print(sum(s))