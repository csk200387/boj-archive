a = int(input())
res = [int(input()) for _ in range(a)]
print("\n".join(map(str, sorted(res))))