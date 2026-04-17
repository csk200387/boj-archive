input()
s=input()
e,o=0,0
for i in s:
  if int(i) % 2 == 0:e+=1
  else:o+=1
if e<o:print(1)
elif e>o:print(0)
else:print(-1)