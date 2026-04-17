a = ""
b = ""
for i in range(0, 8):
  a += input("")
for i in range(0, 64):
  if i%2 == 1:
    b += a[i]
result = b.count("F")
print(result)