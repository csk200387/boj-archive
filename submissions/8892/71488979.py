import sys
from itertools import *
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    cs = int(input())
    arr = [input() for i in range(cs)]
    done = False
    for t in permutations(arr, 2):
        data = "".join(t)
        if data == data[::-1]:
            print(data)
            done = True
            break
    if not done:
        print(0)