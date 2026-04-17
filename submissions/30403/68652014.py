input()
data = input()
up = set("ROYGBIV")
low = set("roygbiv")

if set(data) & up == up and set(data) & low == low:print("YeS")
elif set(data) & up == up:print("YES")
elif set(data) & low == low:print("yes")
else:print("NO!")