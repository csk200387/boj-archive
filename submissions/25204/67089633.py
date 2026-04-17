import sys
input = lambda:sys.stdin.readline().rstrip()
case = int(input())
for _ in range(case):
    n = int(input())
    arr = [input() for _ in range(n)]
    arr.sort(key=lambda x: (-len(x.split("-")[0]), x.split("-")[0], x.split("-")[1]))
    print(*arr, sep='\n')