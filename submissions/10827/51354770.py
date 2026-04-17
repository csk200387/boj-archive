from decimal import Decimal
a, b = map(str,input().split())
print("{0:f}".format(Decimal(a)**int(b)))