import sys
from itertools import *
input = lambda:sys.stdin.readline().rstrip()

def is_pal(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False

n = int(input())

for _ in range(n):
    cs = int(input())
    arr = [input() for i in range(cs)]
    done = False
    for i in range(2, len(arr)+1):
        for t in permutations(arr, i):
            data = "".join(t)
            if is_pal(data):
                print(data)
                done = True
                break
        if done:
            break
    if not done:
        print(0)