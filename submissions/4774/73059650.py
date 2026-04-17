from decimal import*
getcontext().rounding=ROUND_HALF_UP
print(f"${sum(map(lambda x:Decimal(x),open(0)))/12:.2f}")