input()
r = 0
for a in map(int,input().split()) :
  e = 0
  for i in range(2,a+1):
    if a % i == 0 :
      e += 1
      if i == a and e == 1:
        r += 1
print(r)