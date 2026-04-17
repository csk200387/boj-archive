import sys
from itertools import product
input = lambda:sys.stdin.readline().rstrip()

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    data = dict()
    for i in range(n):
        a, b = input().split()
        if data.get(b) == None:
            data[b] = [a]
        else:
            data[b].append(a)
    for key in data:
        data[key].append(None)
    print(len(list(product(*data.values())))-1)