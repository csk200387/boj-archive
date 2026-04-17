import sys
inp = lambda:int(sys.stdin.readline().strip())
a = [inp() for _ in range(inp())]
a.sort()
print(*a)