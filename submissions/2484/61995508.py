r=[]
a=lambda n:r.append(n)
for i in [*open(0)][1:]:
 ip=[*map(int, i.split())]
 c=max(ip,key=ip.count)
 m=ip.count(c)
 if m==4:a(50000+c*5000)
 elif m==3:a(10000+c*1000)
 elif m==2 and len(set(ip))==2:a(2000+sum(set(ip))*500)
 elif m==2:a(1000+c*100)
 else:a(max(ip)*100)
print(max(r))