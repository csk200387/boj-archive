from fractions import Fraction
size = int(input())
arr = list(map(int, input().split()))
tmp = Fraction(1, arr.pop()) + arr.pop()
while arr:
    tmp = Fraction(1, tmp) + arr.pop()
r = 1 - Fraction(1, tmp)
print(r.numerator, r.denominator)