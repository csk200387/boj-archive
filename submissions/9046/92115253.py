import sys
from collections import Counter
input = lambda:sys.stdin.readline().rstrip()

for i in range(int(input())):
    line = input().replace(" ", "")
    tmp = Counter(line).most_common()
    if len(tmp) > 1 and tmp[0][1] == tmp[1][1]:
        print("?")
    else:
        print(tmp[0][0])