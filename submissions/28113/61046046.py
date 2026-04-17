n, a, b = map(int, input().split())

if a < n + b:
  print("Bus")
elif a == n + b:
  print("Anything")
else:
  print("Subway")
