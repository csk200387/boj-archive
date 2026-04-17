import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [input() for _ in range(n)]
print(*sorted(arr, key=lambda x: (len(x), x)), sep="\n")