a = []
b = ""
result = 0
for i in range(0, 8):
  a.append(input(""))
for i in range(0, 8):
  if i%2 == 0:
    b += a[i]
  else:
    b += a[i][::-1]
result = b[::2].count("F")
print(result)