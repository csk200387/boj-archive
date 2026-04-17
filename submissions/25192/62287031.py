r,s=0,{}
for i in [*open(0)][1::]:
 if i=="ENTER\n":r+=len(s);s=set()
 else:s.add(i)
print(r+len(s))