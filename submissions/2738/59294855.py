import os
import sys
os.system("pip3 install numpy")
import numpy as np
inp = lambda:sys.stdin.readline().strip().split()
N, M = map(int, inp())
arr1 = np.array([[*map(int, inp())] for _ in range(N)])
arr2 = np.array([[*map(int, inp())] for _ in range(N)])

for i in (arr1+arr2) :
  print(*i)