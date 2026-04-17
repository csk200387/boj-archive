a,b,c = map(int, input().split("/"))
if 1 <= a <= 12:
  if 1 <= b <= 12:
    print("either")
  else:
    print("US")
else:
  if 1 <= b <= 12:
    print("EU")
  else:
    print("either")