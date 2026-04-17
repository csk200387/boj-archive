r=0
for i in [*open(0)][1].split():
 if i == i[::-1]:
  r+=int(i)
print(r)