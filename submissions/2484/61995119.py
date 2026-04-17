import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
result = []

for i in range(n):
    ip = list(map(int, input().split()))
    c = max(ip, key=ip.count)
    m = ip.count(c)
    if m == 4:
        result.append(50_000 + c * 5_000)
    elif m == 3:
        result.append(10_000 + c * 1_000)
    elif m == 2 and len(set(ip)) == 2:
        result.append(2_000 + sum(set(ip)) * 500)
    elif m == 2:
        result.append(1_000 + c * 100)
    else:
        result.append(max(ip) * 100)
print(max(result))