t = input()
for i in range(26) :
  tmp = t.count(chr(97+i))
  print(tmp, end=" ")