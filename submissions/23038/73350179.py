import sys
input = lambda:sys.stdin.readline().rstrip()
n, m = map(int, input().split())
A = [[*input()] for _ in range(n*3)]
for x in range(n):
 for y in range(m):
  ofs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
  for dx, dy in ofs:
   try:
    if A[1+x*3+dx*2][1+y*3+dy*2] == '#':
     A[1+x*3+dx][1+y*3+dy] = '#'
     A[1+x*3][1+y*3] = '#'
   except:pass
for i in A:
 print(*i, sep='')