import sys
inp = lambda:int(sys.stdin.readline().strip())
a = [inp() for _ in range(inp())]
a.sort()
sys.stdout.write("\n".join(map(str,a)))