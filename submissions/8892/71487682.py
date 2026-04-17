import sys
from itertools import *
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    cs = int(input())
    arr = [input() for i in range(cs)]
    done = False
    for i in range(2, len(arr)+1):
        for t in permutations(arr, i):
            data = "".join(t)
            if data == data[::-1]:
                print(data)
                done = True
                break
        if done:
            break
    if not done:
        print(0)