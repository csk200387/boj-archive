import sys
input = lambda:sys.stdin.readline().rstrip()
ar = [[1, 1, 1, 1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6], [5, 5, 5, 5], [6, 6, 6, 6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1], [0, 0, 0, 0]]
n = int(input())
for i in range(n) :
    a,b = map(int, input().split())
    print(ar[(a%10)-1][(b%4)-1])