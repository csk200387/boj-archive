import sys
input = lambda:sys.stdin.readline().rstrip()

eggs, n = map(int, input().split())
customer = sorted([int(input()) for i in range(n)], reverse=1)
result = []
for c in customer:
    t = []
    for i in customer:
        if c <= i:
            t.append(c)
    result.append(t)
r = max(result, key=sum)
print(r[0], sum(r))