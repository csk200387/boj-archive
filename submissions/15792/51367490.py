from decimal import *
a,b = map(int,input().split())
print(f"{Decimal(a) / Decimal(b):.2000f}".rstrip('0'))