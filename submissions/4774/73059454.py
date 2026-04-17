from decimal import *
import sys
input = lambda:sys.stdin.readline().rstrip()
getcontext().rounding = ROUND_HALF_UP
s = 0
for i in range(12):
    s += Decimal(input())
print("$", round(s/12, 2), sep="")