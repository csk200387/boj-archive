import sys
from math import factorial
input = lambda:sys.stdin.readline().rstrip()

while True:
    try:
        line = input()
        if line == "0":
            break
        n = 0
        for idx, num in enumerate(line[::-1], start=1):
            n += int(num) * factorial(idx)
        print(n)
    except:
        break