import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline().strip()))
print("\n".join(sorted(list(map(str,set(a))))))