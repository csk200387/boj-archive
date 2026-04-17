from decimal import Decimal
a, b = input().split()
print("{0:f}".format(Decimal(a)**int(b)))