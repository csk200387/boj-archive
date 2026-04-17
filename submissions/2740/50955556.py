import numpy as np
import sys
input = sys.stdin.readline

arrA = []
arrB = []
n1, n2 = map(int, input().rstrip().split())
for i in range(n1) :
  arrA.append(list(map(int, input().rstrip().split())))
n1, n2 = map(int, input().rstrip().split())
for i in range(n1) :
  arrB.append(list(map(int, input().rstrip().split())))
A = np.array(arrA)
B = np.array(arrB)
ar = np.array(A@B).tolist()
for i in ar :
  print(" ".join(list(map(str,i))))