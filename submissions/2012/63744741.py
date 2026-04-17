import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
ar = [int(input())for _ in range(n)]
ar.sort()
print(sum([abs(i+1-ar[i])for i in range(n)]))