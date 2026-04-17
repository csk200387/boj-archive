from decimal import *
a,b = map(int,input().split())
getcontext().prec = 2000
print(f"{Decimal(a) / Decimal(b):.2000f}".rstrip('0'))