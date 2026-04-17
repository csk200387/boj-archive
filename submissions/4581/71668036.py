import sys
from collections import Counter
input = lambda:sys.stdin.readline().rstrip()
while True:
    line = input().rstrip()
    if line == '#':
        break
    d = Counter(line)
    if d['A']*2 >= len(line):
        print('need quorum')
    elif d['Y'] > d['N']:
        print('yes')
    elif d['Y'] < d['N']:
        print('no')
    else:
        print('tie')