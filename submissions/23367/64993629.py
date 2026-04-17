r="yuiophjklnm"
w=input()
s=[w[0] in r]
for i in range(1, len(w)):
 s+=[w[i] in r]
 if s[-1]==s[-2]:
  print("no")
  exit()
print("yes")