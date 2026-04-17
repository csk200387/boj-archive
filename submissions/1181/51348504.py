import sys
input = lambda:sys.stdin.readline().rstrip()
num = int(input())
ar = []
for i in range(num) :
    ar.append(input())
ar = list(set(ar))
ar.sort()
ar.sort(key = len)
for i in ar :
    print(i)