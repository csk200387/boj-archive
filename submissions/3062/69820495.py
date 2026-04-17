import sys
inp = sys.stdin.readline
for i in range(int(inp())):
    n = inp().strip()
    if (t:=str(int(n)+int(n[::-1]))) == t[::-1]:
        print("YES")
    else:
        print("NO")