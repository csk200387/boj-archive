n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print("\n".join(sorted(list(map(str,set(a))))))