import sys
input = lambda:sys.stdin.readline().rstrip()
num = int(input())
ar = [input() for _ in range(num)]
ar = list(set(ar))
ar.sort(key=lambda x:(len(x), x))
print("\n".join(ar))