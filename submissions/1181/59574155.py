import sys
input = lambda:sys.stdin.readline().rstrip()
ar = [*{input() for i in range(int(input()))}]
ar.sort(key=len)
print(*ar)