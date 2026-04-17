import re
_,*a=open(0)
t=list(map(lambda x:len(re.findall('1+',x)),a))
print(d:=max(t), t.count(d))