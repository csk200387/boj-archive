from math import gcd
import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
arr = [int(input()) for _ in range(n)]
tmp = [arr[i]-arr[i-1] for i in range(1, n)]
tt = len(range(arr[0], arr[-1]+1, gcd(*tmp))) - len(arr)
print(tt)