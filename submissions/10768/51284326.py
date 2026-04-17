m, d = int(input()), int(input())
print(("Special" if d == 18 else ("After" if d > 18 else "Before")) if m == 2 else ("Before" if m < 2 else "After"))