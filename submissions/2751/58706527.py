import sys
n = int(sys.stdin.readline())
a = [n for _ in range(n)]
a.sort()
sys.stdout.write("\n".join(list(map(str,a))))