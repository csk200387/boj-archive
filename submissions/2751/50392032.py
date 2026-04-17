import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline().strip()))
r = sorted(list(set(a)))
print("\n".join(list(map(str,r))))