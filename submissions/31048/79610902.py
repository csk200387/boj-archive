import sys
from math import factorial
input = lambda:sys.stdin.readline().rstrip()
arr = [0] * 11
for i in range(1, 11):
  arr[i] = factorial(i)%10
n = int(input())
for i in range(n):
  print(arr[int(input())])