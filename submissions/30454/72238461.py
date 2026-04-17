import re
_,*a=open(0)
print(d:=max(t:=list(map(lambda x:len(re.findall('1+',x)),a))),t.count(d))