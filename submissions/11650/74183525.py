import sys
input = lambda:sys.stdin.readline().rstrip()
num = int(input())
ar = [[*map(int,input().split())] for _ in range(num)]
ar.sort(key=lambda x:(x[0], x[1]))
print("\n".join(ar))