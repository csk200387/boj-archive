n = int(input())
for i in range(1, n + 1):
    input()
    s = list(map(int, input().split()))
    even = sorted(t for t in s if t % 2 == 0)
    odd = sorted([t for t in s if t % 2 == 1], reverse=True)
    res = []
    for t in s:
        if t % 2:res.append(odd.pop())
        else:res.append(even.pop())
    print(f"Case #{i}: {' '.join(map(str, res))}")